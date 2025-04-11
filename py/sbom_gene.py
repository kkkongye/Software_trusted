import os
import tarfile
import tempfile
import json
import hashlib
from datetime import datetime
from packageurl import PackageURL
from spdx_tools.spdx.model.spdx_no_assertion import SpdxNoAssertion
from spdx_tools.spdx.model import (
    Document,
    Package,
    Relationship,
    RelationshipType,
    File,
    FileType,
    CreationInfo,
    Actor,
    ActorType,
    Checksum,
    ChecksumAlgorithm,
)
from license_expression import get_spdx_licensing
#from spdx_tools.common.spdx_licensing import spdx_licensing
from spdx_tools.spdx.validation.document_validator import validate_full_spdx_document
from spdx_tools.spdx.writer.write_anything import write_file

from cyclonedx.model.bom import Bom
from cyclonedx.model.component import Component, ComponentType
from cyclonedx.model.contact import OrganizationalEntity

from cyclonedx.output import make_outputter
from cyclonedx.validation import make_schemabased_validator

def sanitize_spdx_id(package_name):
    """
    将软件包名称转换为符合 SPDX 标准的 spdx_id。
    - 移除不允许的字符（如 @ 和 /）。
    - 替换特殊字符为合法字符。
    """
    sanitized_name = package_name.replace("@", "").replace("/", "-")
    return f"SPDXRef-{sanitized_name}"
# 从 tgz 文件中提取依赖项和元数据
def extract_dependencies_from_tgz(package_path):
    dependencies = {}
    package_metadata = {}

    with tempfile.TemporaryDirectory() as tmpdir:
        with tarfile.open(package_path, "r:gz") as tar:
            tar.extractall(path=tmpdir)

        pkg_json_path = os.path.join(tmpdir, 'package', 'package.json')
        lock_json_path = os.path.join(tmpdir, 'package', 'package-lock.json')

        if os.path.exists(pkg_json_path):
            with open(pkg_json_path, 'r', encoding='utf-8') as f:
                pkg_data = json.load(f)
                package_metadata = pkg_data
                dependencies.update(pkg_data.get('dependencies', {}))

        if os.path.exists(lock_json_path):
            with open(lock_json_path, 'r', encoding='utf-8') as f:
                lock_data = json.load(f)
                dependencies.update(lock_data.get('dependencies', {}))

    return dependencies, package_metadata

# 生成 SPDX SBOM
def generate_spdx_sbom(package_path):
    filename = os.path.basename(package_path)
    dependencies, meta = extract_dependencies_from_tgz(package_path)

    creation_info = CreationInfo(
        spdx_version="SPDX-2.3",
        spdx_id="SPDXRef-DOCUMENT",
        name=f"SBOM for {filename}",
        data_license="CC0-1.0",
        document_namespace=f"https://sbom.record.com/{filename}", 
        creators=[Actor(ActorType.TOOL, "sbom-generator", None)],
        created=datetime.now()
    )
    document = Document(creation_info)

    main_package = Package(
        name=meta.get("name", "unknown"),
        spdx_id="SPDXRef-Package-Main",
        download_location=SpdxNoAssertion(),
        version=meta.get("version", "UNKNOWN"),
        supplier=Actor(ActorType.ORGANIZATION, meta.get("author", "NOASSERTION"), None),
        originator=Actor(ActorType.ORGANIZATION, meta.get("author", "NOASSERTION"), None),
        files_analyzed=False,
        #license_concluded=get_spdx_licensing().parse("MIT and GPL-2.0"),
        license_concluded=SpdxNoAssertion(),
        license_declared=SpdxNoAssertion(),
        copyright_text="NOASSERTION"
    )
    document.packages = [main_package]
    document.relationships = [
        Relationship("SPDXRef-DOCUMENT", RelationshipType.DESCRIBES, "SPDXRef-Package-Main")
    ]

    # 添加依赖包
    for dep_name, dep_ver in dependencies.items():
        spdx_id = sanitize_spdx_id(dep_name)
        dep_pkg = Package(
            name=dep_name,
            #spdx_id=f"SPDXRef-{dep_name}",
            spdx_id=spdx_id,
            download_location=SpdxNoAssertion(),
            version=dep_ver if isinstance(dep_ver, str) else "UNKNOWN",
            files_analyzed=False,
            #license_concluded=get_spdx_licensing().parse("MIT and GPL-2.0")
            license_concluded=SpdxNoAssertion(),
            license_declared=SpdxNoAssertion(),
            copyright_text="NOASSERTION"
        )
        document.packages.append(dep_pkg)
        document.relationships.append(
            Relationship("SPDXRef-Package-Main", RelationshipType.DEPENDS_ON, dep_pkg.spdx_id)
        )


    # 验证 SPDX 格式合法性
    errors = validate_full_spdx_document(document)
    if errors:
        for err in errors:
            print(f"[!] SPDX validation error: {err.validation_message}")
    else:
        output_path = f"sboms/{filename}.spdx.json"
        write_file(document, output_path)
        return output_path

    return None
    

#生成 CycloneDX SBOM
def generate_cyclonedx_sbom(package_path):
    filename = os.path.basename(package_path)
    dependencies, meta = extract_dependencies_from_tgz(package_path)

    components = []
    for name, version in dependencies.items():
        version_str = version if isinstance(version, str) else "UNKNOWN"
        component = Component(
            name=name,
            version=version_str,
            type=ComponentType.LIBRARY,
            purl=PackageURL(type="npm", name=name, version=version),
            #purl=f"pkg:npm/{name}@{version_str}",
            #licenses=[LicenseChoice(license_expression="NOASSERTION")],
            supplier=OrganizationalEntity(name="NOASSERTION")
        )
        components.append(component)

    bom = Bom(components=components)
    outputter = make_outputter(bom=bom, output_format="json")

    # 验证 CycloneDX 合规性
    validator = make_schemabased_validator(bom, output_format="json", schema_version=outputter.schema_version)
    if not validator.is_valid():
        for err in validator.validation_errors:
            print(f"[!] CycloneDX validation error: {err}")
    else:
        output_file = f"sboms/{filename}.cyclonedx.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(outputter.output_as_string())
        return output_file

    return None

# 生成 SBOM
def generate_sbom(package_path, sbom_format):
    os.makedirs("sboms", exist_ok=True)
    if sbom_format.lower() == 'spdx':
        return generate_spdx_sbom(package_path)
    elif sbom_format.lower() == 'cyclonedx':
        return generate_cyclonedx_sbom(package_path)
    else:
        raise ValueError("Unsupported SBOM format. Choose 'spdx' or 'cyclonedx'")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate SPDX or CycloneDX SBOM from NPM .tgz package.")
    parser.add_argument("package_path", help="Path to the .tgz package file")
    parser.add_argument(
        "--format", choices=["spdx", "cyclonedx"], default="spdx", help="SBOM format to generate"
    )
    args = parser.parse_args()

    sbom_file = generate_sbom(args.package_path, args.format)
    if sbom_file:
        print(f"[+] SBOM successfully generated: {sbom_file}")
    else:
        print("[!] SBOM generation failed. Check validation errors above.")
