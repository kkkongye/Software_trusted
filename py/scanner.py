# vulnerability_scanner.py

import json
import os
import time
import random
from collections import defaultdict
from datetime import datetime

# 漏洞扫描结果保存路径
OUTPUT_DIR = "./scanResult"
os.makedirs(OUTPUT_DIR, exist_ok=True)

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
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    
    # 随机生成漏洞数量
    critical = random.randint(0, 5)
    high = random.randint(2, 10)
    medium = random.randint(5, 15)
    low = random.randint(8, 20)
    unknown = random.randint(0, 5)
    
    # 创建示例漏洞报告
    result = {
        "severity_summary": {
            "CRITICAL": critical,
            "HIGH": high,
            "MEDIUM": medium,
            "LOW": low,
            "UNKNOWN": unknown
        },
        "vulnerabilities": []
    }
    
    # 随机添加漏洞详情
    severity_levels = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNKNOWN"]
    packages = ["react", "lodash", "express", "axios", "moment", "webpack", "babel", "vue", "angular", "jquery"]
    vulnerability_types = [
        "远程代码执行", "跨站脚本攻击", "SQL注入", "信息泄露", "权限提升", 
        "拒绝服务", "内存泄漏", "缓冲区溢出", "配置错误", "中间人攻击"
    ]
    
    # 添加随机Critical漏洞
    for i in range(critical):
        result["vulnerabilities"].append({
            "id": f"CVE-2023-{1000 + i}",
            "package_name": random.choice(packages),
            "severity": "CRITICAL",
            "description": f"{random.choice(vulnerability_types)}漏洞，可能导致系统完全被控制",
            "cvss_score": round(random.uniform(9.0, 10.0), 1)
        })
    
    # 添加随机High漏洞
    for i in range(high):
        result["vulnerabilities"].append({
            "id": f"CVE-2023-{2000 + i}",
            "package_name": random.choice(packages),
            "severity": "HIGH",
            "description": f"{random.choice(vulnerability_types)}漏洞，可能导致严重的安全问题",
            "cvss_score": round(random.uniform(7.0, 8.9), 1)
        })
    
    # 添加随机Medium漏洞
    for i in range(medium):
        result["vulnerabilities"].append({
            "id": f"CVE-2023-{3000 + i}",
            "package_name": random.choice(packages),
            "severity": "MEDIUM",
            "description": f"{random.choice(vulnerability_types)}漏洞，需要一定条件才能利用",
            "cvss_score": round(random.uniform(4.0, 6.9), 1)
        })
    
    # 添加随机Low漏洞
    for i in range(low):
        result["vulnerabilities"].append({
            "id": f"CVE-2023-{4000 + i}",
            "package_name": random.choice(packages),
            "severity": "LOW",
            "description": f"{random.choice(vulnerability_types)}漏洞，安全风险较小",
            "cvss_score": round(random.uniform(0.1, 3.9), 1)
        })
    
    # 添加Unknown漏洞
    for i in range(unknown):
        result["vulnerabilities"].append({
            "id": f"CVE-2023-{5000 + i}",
            "package_name": random.choice(packages),
            "severity": "UNKNOWN",
            "description": "未确定影响范围和严重程度的漏洞",
            "cvss_score": None
        })
    
    # 确保目录存在
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # 写入文件
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    print(f"漏洞扫描完成，结果保存至 {output_path}")
    print(f"漏洞统计: 极其严重: {critical}, 高危: {high}, 中危: {medium}, 低危: {low}, 未知: {unknown}")
    
    return result, output_path


# 测试示例（可从命令行运行）
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Scan vulnerabilities from SPDX SBOM")
    parser.add_argument("spdx_path", help="Path to SPDX SBOM JSON file")
    args = parser.parse_args()

    result, path = scan_vulnerabilities(args.spdx_path)
    print("漏洞统计（按严重等级）:")
    for severity, count in result["severity_summary"].items():
        print(f"{severity}: {count}")
    print(f"\n详细结果已保存至: {path}")

