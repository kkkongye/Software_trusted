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
        <button class="upload-button" @click="uploadFile">上传文件</button>
      </div>
      <div class="file-info" v-if="fileName">
        <p class="file-name">文件名: {{ fileName }}</p>
        <p class="file-status" v-if="uploadStatus">状态: <span :class="{ 'success': uploadStatus === '已上传', 'error': uploadStatus === '上传失败' }">{{ uploadStatus }}</span></p>
      </div>
      
      <div class="select-container">
        <label>生成的SBOM清单类型:</label>
        <select v-model="sbomType" class="styled-select">
          <option value="SPDX">SPDX</option>
          <option value="CDX">CDX</option>
          <option value="SWID">SWID</option>
        </select>
      </div>
      <button class="generate-button" @click="generateSBOM">生成SBOM清单</button>
      <button class="generate-button" @click="generatevul">生成漏洞清单</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const fileName = ref('');
const uploadStatus = ref('');
const sbomType = ref('SPDX');

const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    if (!file.name.endsWith('.tgz')) {
      alert('请选择.tgz格式的文件');
      event.target.value = ''; // 清空文件选择
      fileName.value = '';
      return;
    }
    fileName.value = file.name;
    uploadStatus.value = ''; // 清除之前的上传状态
  }
};

const uploadFile = async () => {
  if (!fileName.value) {
    alert('请先选择文件');
    return;
  }
  try {
    // 模拟上传逻辑
    uploadStatus.value = '已上传';
  } catch (error) {
    uploadStatus.value = '上传失败';
  }
};

const generateSBOM = () => {
  if (!fileName.value || uploadStatus.value !== '已上传') {
    alert('请先上传文件');
    return;
  }
  alert(`将生成 ${sbomType.value} 类型的SBOM清单`);
};

const generatevul = () => {
  if (!fileName.value || uploadStatus.value !== '已上传') {
    alert('请先上传文件');
    return;
  }
  alert(`将生成 ${sbomType.value} 类型的漏洞清单`);
};

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
  margin: 0 0 15px 0;
  font-size: 18px;
  color: #2c3e50;
  font-weight: 500;
  text-align: center;
}

.content-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 15px;
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

.upload-button:hover {
  background-color: #218838;
  transform: translateY(-1px);
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
}

.generate-button:hover {
  background-color: #138496;
  transform: translateY(-1px);
}
</style>