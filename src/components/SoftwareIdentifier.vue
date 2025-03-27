<template>
  <div class="software-identifier">
    <h3>软件标识管理</h3>
    <div class="search-container">
      <input v-model="searchQuery" placeholder="搜索软件标识" class="search-input" />
      <button class="search-button" @click="performSearch">搜索</button>
    </div>
    <div class="button-container">
      <button class="action-button" @click="issueIdentifier">标识颁发</button>
      <button class="action-button" @click="revokeIdentifier">标识注销</button>
      <button class="action-button" @click="updateKey">标识密钥更新</button>
      <button class="action-button" @click="updateDocument">更新标识文档</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const searchQuery = ref('');
const searchResult = ref('');
const showSearchResult = ref(false);

const performSearch = () => {
  if (searchQuery.value.trim()) {
    // 模拟搜索逻辑
    const result = `找到与 "${searchQuery.value}" 相关的结果`;
    alert(result);
  } else {
    alert('请输入搜索内容');
  }
};

const issueIdentifier = () => alert('标识颁发');
const revokeIdentifier = () => alert('标识注销');
const updateKey = () => alert('标识密钥更新');
const updateDocument = () => alert('更新标识文档');
</script>

<style scoped>
.software-identifier {
  border: 1px solid #ccc;
  padding: 15px;
  margin: 10px;
  background-color: #ffffff;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 440px; /* 固定宽度 */
  height: auto; /* 自动高度 */
  display: flex;
  flex-direction: column;
  align-items: center; /* 内容居中 */
}

.software-identifier h3 {
  margin: 0 0 10px 0;
  font-size: 18px;
  color: #333;
}

.search-container {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
  width: 100%;
}

.search-input {
  flex: 1;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 14px;
  color: #333;
  outline: none;
  margin-right: 10px;
}

.search-input:focus {
  border-color: #007bff;
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
}

.search-button {
  padding: 8px 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.search-button:hover {
  background-color: #0056b3;
}

.button-container {
  display: flex;
  flex-direction: column;
  gap: 30px; /* 按钮之间的间隙 */
  margin-top:20px;
  width: 100%;
}

.action-button {
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  width: 60%; /* 宽度占满容器 */
  display: block;
  margin: 0 auto;
}

.action-button:hover {
  background-color: #0056b3;
}

.software-identifier h3 {
  align-self: flex-start; /* 标题靠左对齐 */
  margin: 0 0 10px 0; /* 调整标题的 margin */
  font-size: 20px;
  color: #333;
}
</style>



