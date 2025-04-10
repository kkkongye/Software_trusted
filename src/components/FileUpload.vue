<template>
  <div class="file-upload">
    <h3>文件上传</h3>
    <div class="content-container">
    <div class="file-input-container">
      <label for="file-input" class="custom-file-upload">
          <i class="upload-icon">📄</i>
        选择文件
      </label>
        <input id="file-input" type="file" @change="handleFileChange" accept=".tgz" />
        <button class="upload-button" @click="uploadFile" :disabled="isUploading">
          {{ isUploading ? '上传中...' : '上传文件' }}
        </button>
      </div>
      <div class="file-info" v-if="fileName">
        <p class="file-name">文件名: {{ fileName }}</p>
        <p class="file-status" v-if="uploadStatus">状态: 
          <span :class="{ 'success': uploadStatus === '已上传', 'error': uploadStatus === '上传失败' }">
            {{ uploadStatus }}
          </span>
        </p>
    </div>

        <div class="select-container">
          <label>生成的SBOM清单类型:</label>
          <select v-model="sbomType" class="styled-select">
          <option value="spdx">SPDX</option>
          <option value="cdx">CDX</option>
          <option value="swid">SWID</option>
          </select>
        </div>
      <button class="generate-button" @click="generateSBOM" :disabled="!fileName || uploadStatus !== '已上传' || isGenerating">
        {{ isGenerating ? 'SBOM生成中...' : '生成SBOM清单' }}
      </button>
      <button class="generate-button" @click="generateVuln" :disabled="!sbomFile || isScanning">
        {{ isScanning ? '漏洞扫描中...' : '生成漏洞清单' }}
      </button>
      
      <div class="result-info" v-if="sbomFile">
        <p>SBOM文件: {{ sbomFile }}</p>
        <button class="download-button" @click="downloadSBOM">下载SBOM</button>
      </div>
      
      <div class="result-info" v-if="vulnFile">
        <p>漏洞报告: {{ vulnFile }}</p>
        <button class="download-button" @click="downloadVuln">下载漏洞报告</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import apiService from '../api/index';

const emit = defineEmits(['vulnerabilityDataUpdated']);

const fileName = ref('');
const fileObject = ref(null);
const uploadStatus = ref('');
const sbomType = ref('spdx');
const sbomFile = ref('');
const vulnFile = ref('');
const vulnerabilityData = ref({
  critical: 0,
  high: 0,
  medium: 0,
  low: 0,
  unknown: 0
});

const isUploading = ref(false);
const isGenerating = ref(false);
const isScanning = ref(false);

// 当漏洞数据变化时，通知父组件
watch(vulnerabilityData, (newValue) => {
  emit('vulnerabilityDataUpdated', newValue);
}, { deep: true });

// 当文件选择改变时触发
const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    if (!file.name.endsWith('.tgz')) {
      alert('请选择.tgz格式的文件');
      event.target.value = ''; // 清空文件选择
      fileName.value = '';
      fileObject.value = null;
      return;
    }
    fileName.value = file.name;
    fileObject.value = file;
    uploadStatus.value = ''; // 清除之前的上传状态
    sbomFile.value = ''; // 清除之前的SBOM文件
    vulnFile.value = ''; // 清除之前的漏洞文件
  }
};

// 上传文件
const uploadFile = async () => {
  if (!fileObject.value) {
    alert('请先选择文件');
    return;
  }
  
  try {
    isUploading.value = true;
    const response = await apiService.uploadFile(fileObject.value);
    
    if (response.data && response.data.message === '上传成功') {
    uploadStatus.value = '已上传';
    } else {
      uploadStatus.value = '上传失败';
      alert('文件上传失败: ' + (response.data.error || '未知错误'));
    }
  } catch (error) {
    console.error('上传文件出错:', error);
    uploadStatus.value = '上传失败';
    alert('文件上传失败: ' + (error.response?.data?.error || error.message || '未知错误'));
  } finally {
    isUploading.value = false;
  }
};

// 生成SBOM清单
const generateSBOM = async () => {
  if (!fileName.value || uploadStatus.value !== '已上传') {
    alert('请先上传文件');
    return;
  }
  
  try {
    isGenerating.value = true;
    const response = await apiService.generateSBOM(fileName.value, sbomType.value);
    
    if (response.data && response.data.sbom_file) {
      sbomFile.value = response.data.sbom_file;
      
      // 保存到 localStorage 并触发事件通知其他组件
      localStorage.setItem('currentSBOMFile', response.data.sbom_file);
      window.dispatchEvent(new StorageEvent('storage', {
        key: 'currentSBOMFile',
        newValue: response.data.sbom_file,
        url: window.location.href
      }));
      
      alert('SBOM清单生成成功!');
    } else {
      alert('SBOM清单生成失败: ' + (response.data.error || '未知错误'));
    }
  } catch (error) {
    console.error('生成SBOM清单出错:', error);
    alert('SBOM清单生成失败: ' + (error.response?.data?.error || error.message || '未知错误'));
  } finally {
    isGenerating.value = false;
  }
};

// 生成漏洞清单
const generateVuln = async () => {
  if (!sbomFile.value) {
    alert('请先生成SBOM清单');
    return;
  }
  
  try {
    isScanning.value = true;
    const response = await apiService.scanVulnerabilities(sbomFile.value);
    
    if (response.data && response.data.vuln_file) {
      vulnFile.value = response.data.vuln_file;
      
      // 更新漏洞统计数据
      if (response.data.summary) {
        const summary = response.data.summary;
        vulnerabilityData.value = {
          critical: summary.CRITICAL || 0,
          high: summary.HIGH || 0,
          medium: summary.MEDIUM || 0,
          low: summary.LOW || 0,
          unknown: summary.UNKNOWN || 0
        };
        
        // 发出事件通知
        emit('vulnerabilityDataUpdated', vulnerabilityData.value);
      }
      
      alert('漏洞扫描完成!');
    } else {
      alert('漏洞扫描失败: ' + (response.data.error || '未知错误'));
    }
  } catch (error) {
    console.error('漏洞扫描出错:', error);
    alert('漏洞扫描失败: ' + (error.response?.data?.error || error.message || '未知错误'));
  } finally {
    isScanning.value = false;
  }
};

// 下载SBOM文件
const downloadSBOM = () => {
  if (sbomFile.value) {
    apiService.downloadFile('sboms', sbomFile.value);
  }
};

// 下载漏洞报告
const downloadVuln = () => {
  if (vulnFile.value) {
    apiService.downloadFile('scanResult', vulnFile.value);
  }
};

defineExpose({
  vulnerabilityData
});
</script>

<style scoped>
.file-upload {
  border: 1px solid #e0e0e0;
  padding: 15px;
  margin: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  box-sizing: border-box;
}

.file-upload h3 {
  margin-top: 0;
  margin-bottom: 15px;
  text-align: center;
  font-size: 16px;
  color: #333;
  font-weight: bold;
}

.content-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 15px;
  width: 100%;
}

.file-input-container {
  display: flex;
  gap: 10px;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 15px;
  width: 100%;
}

.custom-file-upload {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 8px 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.3s ease;
  min-width: 120px;
}

.custom-file-upload:hover {
  background-color: #0069d9;
  transform: translateY(-1px);
}

.upload-icon {
  font-size: 16px;
}

#file-input {
  display: none;
}

.upload-button {
  padding: 8px 16px;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.3s ease;
  min-width: 120px;
}

.upload-button:hover:not(:disabled) {
  background-color: #218838;
  transform: translateY(-1px);
}

.upload-button:disabled {
  background-color: #6c757d;
  cursor: not-allowed;
  opacity: 0.7;
}

.file-info {
  margin-bottom: 15px;
  padding: 8px;
  background-color: #f8f9fa;
  border-radius: 4px;
  border: 1px solid #e9ecef;
  width: 100%;
  text-align: center;
}

.file-name, .file-status {
  margin: 4px 0;
  font-size: 14px;
  color: #495057;
}

.success {
  color: #28a745;
  font-weight: 500;
}

.error {
  color: #dc3545;
  font-weight: 500;
}

.select-container {
  margin-bottom: 10px;
  width: 100%;
  max-width: 300px;
  align-self: center;
}

.select-container label {
  display: block;
  margin-bottom: 5px;
  font-size: 14px;
  color: #495057;
  font-weight: 500;
  text-align: center;
}

.styled-select {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #ced4da;
  border-radius: 4px;
  background-color: white;
  font-size: 14px;
  color: #495057;
  cursor: pointer;
  transition: all 0.3s ease;
  text-align: center;
}

.styled-select:hover {
  border-color: #007bff;
}

.styled-select:focus {
  outline: none;
  border-color: #007bff;
  box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.25);
}

.generate-button {
  width: 100%;
  max-width: 300px;
  padding: 10px;
  background-color: #17a2b8;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  text-align: center;
  align-self: center;
}

.generate-button:hover:not(:disabled) {
  background-color: #138496;
  transform: translateY(-1px);
}

.generate-button:disabled {
  background-color: #6c757d;
  cursor: not-allowed;
  opacity: 0.7;
}

.result-info {
  margin-top: 10px;
  padding: 10px;
  background-color: #e9f7fb;
  border-radius: 4px;
  border: 1px solid #bee5eb;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.result-info p {
  margin: 0;
  font-size: 14px;
  color: #0c5460;
}

.download-button {
  padding: 5px 10px;
  background-color: #17a2b8;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.download-button:hover {
  background-color: #138496;
}
</style>