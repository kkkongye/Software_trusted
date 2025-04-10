import os
import json
import time
import random

def scan_vulnerabilities(sbom_path):
    """扫描漏洞
    
    Args:
    
        sbom_path: SBOM文件路径
        
    Returns:
        (result, output_path): 漏洞扫描结果和输出文件路径
    """
    print(f"扫描漏洞: {sbom_path}")
    
    # 提取文件名（不含扩展名）
    base_name = os.path.basename(sbom_path).replace('_sbom.json', '')
    
    # 生成输出文件名
    timestamp = int(time.time())
    output_filename = f"{base_name}_vuln_{timestamp}.json"
    output_path = os.path.join("scanResult", output_filename)
    
    # 随机生成漏洞数量或使用固定值
    # critical = random.randint(0, 5)
    # high = random.randint(2, 10)
    # medium = random.randint(5, 15)
    # low = random.randint(8, 20)
    # unknown = random.randint(0, 5)
    
    # 使用固定值便于测试
    critical = 3
    high = 5
    medium = 8
    low = 12
    unknown = 2
    
    # 创建示例漏洞报告
    result = {
        "severity_summary": {
            "CRITICAL": critical,
            "HIGH": high,
            "MEDIUM": medium,
            "LOW": low,
            "UNKNOWN": unknown
        },
        "vulnerabilities": [
            {"id": "CVE-2023-1234", "severity": "CRITICAL", "package": "example-package-1"},
            {"id": "CVE-2023-5678", "severity": "HIGH", "package": "example-package-2"},
            {"id": "CVE-2023-9012", "severity": "MEDIUM", "package": "example-package-3"}
        ]
    }
    
    # 写入文件
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
        
    return result, output_path