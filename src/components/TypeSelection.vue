<template>
  <div class="type-selection">
    <h3>类型选择</h3>
    <div class="select-container">
      <label>上传文件类型:</label>
      <select v-model="fileType" class="styled-select">
        <option value="Java">Java</option>
        <option value="NodeJS">NodeJS</option>
      </select>
    </div>
    <div class="select-container">
      <label>生成的SBOM清单类型:</label>
      <select v-model="sbomType" class="styled-select">
        <option value="SPDX">SPDX</option>
        <option value="CDX">CDX</option>
        <option value="SWID">SWID</option>
      </select>
    </div>
    <button class="generate-button" @click="generateSBOM">生成清单</button>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const fileType = ref('Java');
const sbomType = ref('SPDX');

// 模拟后端请求
const generateSBOM = async () => {
  const payload = {
    fileType: fileType.value,
    sbomType: sbomType.value,
  };

  try {
    // 发送请求到后端
    const response = await fetch('/api/generate-sbom', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      throw new Error('请求失败');
    }

    const data = await response.json();

    // 假设后端返回的漏洞信息是一个数组
    const vulnerabilities = data.vulnerabilities;

    // 将漏洞信息传递到漏洞清单组件
    emit('update-vulnerabilities', vulnerabilities);
  } catch (error) {
    console.error('生成清单失败:', error);
    alert('生成清单失败，请稍后重试');
  }
};

// 定义 emit 函数
const emit = defineEmits(['update-vulnerabilities']);
</script>

<style scoped>
.type-selection {
  border: 1px solid #ccc;
  padding: 15px;
  margin: 10px;
  background-color: #ffffff;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 300px; /* 固定宽度 */
  height: 150px; /* 固定高度 */
  display: flex;
  flex-direction: column;
  justify-content: space-between; /* 内容均匀分布 */
}

.type-selection h3 {
  margin: 0 0 10px 0;
  font-size: 16px;
  color: #333;
}

.select-container {
  margin-bottom: 10px;
}

.select-container label {
  display: block;
  margin-bottom: 5px;
  font-size: 14px;
  color: #555;
}

.styled-select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
  font-size: 14px;
  color: #333;
  cursor: pointer;
  transition: border-color 0.3s ease;
}

.type-selection h3 {
  align-self: flex-start; /* 标题靠左对齐 */
  margin: 0 0 10px 0; /* 调整标题的 margin */
  font-size: 20px;
  color: #333;
}
.styled-select:hover {
  border-color: #007bff;
}

.styled-select:focus {
  outline: none;
  border-color: #007bff;
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
}

.generate-button {
  width: 80%;
  padding: 9px;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  /* 添加以下属性以实现水平居中 */
  display: block;
  margin: 0 auto;
}

.generate-button:hover {
  background-color: #218838;
}
</style>