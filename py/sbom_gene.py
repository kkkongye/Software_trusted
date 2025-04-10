import os
import json
import time

def generate_sbom(package_path, sbom_format='spdx'):
    """生成SBOM清单
    
    Args:
        package_path: 软件包路径
        sbom_format: SBOM格式，可选值：spdx, cdx, swid
        
    Returns:
        生成的SBOM文件路径
    """
    print(f"生成SBOM清单: {package_path}, 格式: {sbom_format}")
    
    # 提取文件名（不含扩展名）
    base_name = os.path.basename(package_path).replace('.tgz', '')
    
    # 生成输出文件名
    timestamp = int(time.time())
    output_filename = f"{base_name}_{sbom_format}_{timestamp}_sbom.json"
    output_path = os.path.join("sboms", output_filename)
    
    # 创建示例SBOM内容
    sbom_data = {
        "name": f"{base_name} SBOM",
        "format": sbom_format,
        "created": time.ctime(),
        "packages": [
            {"name": "example-package-1", "version": "1.0.0"},
            {"name": "example-package-2", "version": "2.3.1"},
            {"name": "example-package-3", "version": "0.9.5"}
        ]
    }
    
    # 写入文件
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(sbom_data, f, indent=2, ensure_ascii=False)
        
    return output_path