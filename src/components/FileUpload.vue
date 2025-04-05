<template>
  <div class="file-upload">
    <h3>文件上传</h3>
    <div class="file-input-container">
      <label for="file-input" class="custom-file-upload">
        选择文件
      </label>
      <input id="file-input" type="file" @change="handleFileChange" />
      <button class="upload-button" @click="uploadFile">上传文件</button>
    </div>
    <p v-if="fileName">文件名: {{ fileName }}</p>
    <p v-if="uploadStatus">状态: {{ uploadStatus }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const fileName = ref('');
const uploadStatus = ref('');

const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    fileName.value = file.name;
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
</script>

<style scoped>
.file-upload {
  border: 1px solid #ccc;
  padding: 10px;
  margin: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: flex-start; /* 内容靠左对齐 */
  background-color: #ffffff;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  position: relative; /* 为标题定位提供参考 */
  box-sizing: border-box;
}

.file-upload h3 {
  align-self: flex-start; /* 标题靠左对齐 */
  margin: 0 0 10px 0; /* 调整标题的 margin */
  font-size: 20px;
  color: #333;
}

.file-input-container {
  display: flex;
  gap: 10px; /* 按钮之间的间隙 */
  margin-top: 30px;
}

.custom-file-upload {
  padding: 9px 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s ease;
}

.custom-file-upload:hover {
  background-color: #0056b3;
}

#file-input {
  display: none; /* 隐藏默认的文件输入框 */
}

.upload-button {
  padding: 8px 16px;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s ease;
}

.upload-button:hover {
  background-color: #218838;
}

p {
  margin: 0px 0;
  margin-top: 20px;
  font-size: 14px;
  color: #555;
}
</style>