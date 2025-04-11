from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import time
import json
import glob
from werkzeug.utils import secure_filename

from sbom_gene import generate_sbom
from scanner import scan_vulnerabilities

app = Flask(__name__)
CORS(app)  # 允许跨域请求，便于前端联调

UPLOAD_FOLDER = 'test_packages'
SBOM_FOLDER = 'sboms'
SCAN_FOLDER = 'scanResult'

# 存储最近的扫描结果
latest_scan_result = None

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(SBOM_FOLDER, exist_ok=True)
os.makedirs(SCAN_FOLDER, exist_ok=True)


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if not file or not file.filename.endswith('.tgz'):
        return jsonify({'error': '必须上传 .tgz 文件'}), 400

    filename = secure_filename(file.filename)
    save_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(save_path)
    return jsonify({'message': '上传成功', 'filename': filename})


@app.route('/generate_sbom', methods=['POST'])
def generate_sbom_api():
    data = request.json
    filename = data.get('filename')
    sbom_format = data.get('format', 'spdx')

    if not filename:
        return jsonify({'error': '未提供文件名'}), 400

    package_path = os.path.join(UPLOAD_FOLDER, filename)

    try:
        output_path = generate_sbom(package_path, sbom_format)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'SBOM 生成失败', 'detail': str(e)}), 500

    download_name = os.path.basename(output_path)
    return jsonify({
        'message': 'SBOM 生成成功',
        'sbom_file': download_name,
        'download_url': f'/download/sboms/{download_name}'
    })


@app.route('/scan_vuln', methods=['POST'])
def scan_vuln_api():
    global latest_scan_result
    
    data = request.json
    sbom_file = data.get('sbom_file')

    if not sbom_file:
        return jsonify({'error': '未提供 SBOM 文件名'}), 400

    sbom_path = os.path.join(SBOM_FOLDER, sbom_file)

    try:
        result, output_path = scan_vulnerabilities(sbom_path)
        # 保存最近的扫描结果
        latest_scan_result = result
    except Exception as e:
        return jsonify({'error': '漏洞扫描失败', 'detail': str(e)}), 500

    download_name = os.path.basename(output_path)
    return jsonify({
        'message': '漏洞扫描完成',
        'vuln_file': download_name,
        'download_url': f'/download/scanResult/{download_name}',
        'summary': result.get('severity_summary', {}),
        'vulnerabilities': result.get('vulnerabilities', [])
    })


@app.route('/vulnerabilities', methods=['GET'])
def get_vulnerabilities():
    """获取最近的漏洞扫描结果"""
    global latest_scan_result
    
    # 如果有存储的结果，返回它
    if latest_scan_result:
        return jsonify(latest_scan_result)
    
    # 否则尝试读取最新的扫描结果文件
    scan_files = glob.glob(os.path.join(SCAN_FOLDER, '*.json'))
    if not scan_files:
        return jsonify({'message': '没有可用的漏洞扫描结果'}), 404
    
    # 按文件修改时间排序，获取最新的文件
    latest_file = max(scan_files, key=os.path.getmtime)
    
    try:
        with open(latest_file, 'r', encoding='utf-8') as f:
            result = json.load(f)
            latest_scan_result = result  # 缓存结果
            return jsonify(result)
    except Exception as e:
        return jsonify({'error': f'读取漏洞扫描结果失败: {str(e)}'}), 500


@app.route('/download/<folder>/<filename>', methods=['GET'])
def download_file(folder, filename):
    if folder == 'sboms':
        path = SBOM_FOLDER
    elif folder == 'scanResult':
        path = SCAN_FOLDER
    else:
        return jsonify({'error': '无效目录'}), 400

    return send_from_directory(path, filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
