<template>
  <div class="software-identifier-page">
    <!-- 左列 - 软件标识管理 -->
    <div class="column left-column">
      <div class="form-container">
        <h3>软件标识管理</h3>
        <div class="button-container">
          <button class="action-button" @click="showSearchDialog">搜索</button>
          <button class="action-button" @click="issueIdentifier">标识颁发</button>
          <button class="action-button" @click="revokeIdentifier">标识注销</button>
          <button class="action-button" @click="updateKey">标识密钥更新</button>
          <button class="action-button" @click="updateDocument">更新标识文档</button>
        </div>
      </div>
    </div>

    <!-- 右列 - 软件标识表格 -->
    <div class="column right-column">
      <div class="table-container">
        <h3>软件标识列表</h3>
        <div class="table-wrapper">
          <el-table 
            :data="tableData" 
            style="width: 100%; height: 100%" 
            border
            :cell-style="{textAlign: 'center'}"
            :header-cell-style="{textAlign: 'center', backgroundColor: '#f5f7fa'}"
          >
            <el-table-column prop="name" label="软件名" :width="tableColumnWidth" />
            <el-table-column prop="id" label="标识ID" :width="tableColumnWidth" />
            <el-table-column prop="version" label="具体信息" :width="tableColumnWidth" />
          </el-table>
        </div>
      </div>
    </div>

    <!-- 搜索弹框 -->
    <el-dialog
      v-model="dialogVisible"
      title="软件搜索"
      width="30%"
      center
      draggable
      :close-on-click-modal="false"
    >
      <div class="search-dialog-content">
        <el-input v-model="searchKeyword" placeholder="请输入软件名或标识ID" />
        <div class="search-result" v-if="searchResultVisible">
          <div v-if="searchResultData">
            <h4>搜索结果：</h4>
            <p><strong>软件名：</strong> {{ searchResultData.name }}</p>
            <p><strong>标识ID：</strong> {{ searchResultData.id }}</p>
            <p><strong>具体信息：</strong> {{ searchResultData.version }}</p>
          </div>
          <div v-else class="no-result">
            未找到匹配结果
          </div>
        </div>
      </div>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button type="primary" @click="performSearch">
            搜索
          </el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const searchResult = ref('');
const showSearchResult = ref(false);
const dialogVisible = ref(false);
const searchKeyword = ref('');
const searchResultVisible = ref(false);
const searchResultData = ref(null);

// 计算每列宽度
const tableColumnWidth = computed(() => {
  return 'calc(100% / 3)';
});

const tableData = ref([
  {
    name: '新软件_001',
    id: 'id_0i2om',
    version: '1.0.0'
  },
  {
    name: '新软件_056',
    id: 'id_9ierw',
    version: '2.1.0'
  },
  {
    name: '新软件_327',
    id: 'id_75fyb',
    version: '3.0.1'
  }
]);

const showSearchDialog = () => {
  searchKeyword.value = '';
  searchResultVisible.value = false;
  dialogVisible.value = true;
};

const performSearch = () => {
  if (!searchKeyword.value.trim()) {
    alert('请输入搜索关键词');
    return;
  }

  const keyword = searchKeyword.value.toLowerCase();
  const result = tableData.value.find(
    item => 
      item.name.toLowerCase().includes(keyword) || 
      item.id.toLowerCase().includes(keyword)
  );

  searchResultVisible.value = true;
  searchResultData.value = result || null;
};

const issueIdentifier = () => {
  const newSoftware = {
    name: '新软件_' + Math.floor(Math.random() * 1000),
    id: 'id_' + Math.random().toString(36).substr(2, 5),
    version: '1.0.' + Math.floor(Math.random() * 10)
  };
  tableData.value.push(newSoftware);
  alert('已颁发新标识');
};

const revokeIdentifier = () => {
  if (tableData.value.length > 0) {
    tableData.value.pop();
    alert('已注销最后一个标识');
  } else {
    alert('没有可注销的标识');
  }
};

const updateKey = () => alert('标识密钥更新');
const updateDocument = () => alert('更新标识文档');
</script>

<style scoped>
.software-identifier-page {
  display: flex;
  width: 100%;
  height: 100%;
  position: relative;
  background-color: #f0f0f0;
  margin: 0;
  padding: 0;
}

.column {
  padding: 15px;
  box-sizing: border-box;
  height: 100%;
}

.left-column {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.right-column {
  flex: 2;
}

.form-container {
  background-color: #ffffff;
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 15px;
  box-sizing: border-box;
  overflow: auto;
  display: flex;
  flex-direction: column;
  width: 90%;
  max-height: 400px;
}

.table-container {
  background-color: #ffffff;
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 20px;
  height: 100%;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
}

.table-wrapper {
  flex: 1;
  overflow: auto;
  height: calc(100% - 40px);
}

/* 确保表格内内容居中 */
:deep(.el-table__cell) {
  text-align: center;
}

h3 {
  margin-top: 0;
  margin-bottom: 15px;
  text-align: center;
  font-size: 16px;
  color: #333;
  font-weight: bold;
}

.button-container {
  display: flex;
  flex-direction: column;
  gap: 12px;
  width: 100%;
  padding: 5px 0;
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
  width: 65%;
  display: block;
  margin: 0 auto;
}

.action-button:hover {
  background-color: #0056b3;
}

.search-dialog-content {
  margin-bottom: 20px;
}

.search-result {
  margin-top: 20px;
  padding: 15px;
  background-color: #f8f9fa;
  border-radius: 5px;
  border: 1px solid #eee;
}

.search-result h4 {
  margin-top: 0;
  margin-bottom: 10px;
  color: #333;
}

.search-result p {
  margin: 5px 0;
}

.no-result {
  color: #dc3545;
  text-align: center;
  font-weight: bold;
}

.dialog-footer {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}
</style>



