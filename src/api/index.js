import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000'; // 后端API基础URL，可以根据实际环境配置

const apiService = {
  // 上传文件
  uploadFile(file) {
    const formData = new FormData();
    formData.append('file', file);
    
    return axios.post(`${API_BASE_URL}/upload`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
  },
  
  // 生成SBOM清单
  generateSBOM(filename, format = 'spdx') {
    return axios.post(`${API_BASE_URL}/generate_sbom`, {
      filename,
      format
    });
  },
  
  // 扫描漏洞
  scanVulnerabilities(sbomFile) {
    return axios.post(`${API_BASE_URL}/scan_vuln`, {
      sbom_file: sbomFile
    });
  },
  
  // 下载文件的URL生成
  getDownloadUrl(folder, filename) {
    return `${API_BASE_URL}/download/${folder}/${filename}`;
  },
  
  // 直接下载文件
  downloadFile(folder, filename) {
    window.open(this.getDownloadUrl(folder, filename), '_blank');
  }
};

export default apiService; 