<template>
    <div class="sbom-list">
      <h3>SBOM清单</h3>
      <div class="content">
        <div v-if="loading" class="loading">
          <p>加载中...</p>
        </div>
        <div v-else-if="!currentSbomFile" class="empty-state">
          <p>暂无SBOM清单。请先上传软件包并生成SBOM清单。</p>
        </div>
        <div v-else class="sbom-details">
          <h4>SBOM文件信息</h4>
          <p>文件名: {{ currentSbomFile }}</p>
          <button class="view-btn" @click="loadSbomDetails">查看详情</button>
          
          <div v-if="sbomDetails" class="details-container">
            <h5>软件包依赖列表</h5>
            <ul class="packages-list">
              <li v-for="(pkg, index) in sbomDetails.packages" :key="index">
                <strong>{{ pkg.name }}</strong> - 版本: {{ pkg.version }}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  
  const loading = ref(false);
  const currentSbomFile = ref('');
  const sbomDetails = ref(null);
  
  // 监听LocalStorage变化
  const handleStorageChange = (event) => {
    if (event.key === 'currentSBOMFile') {
      currentSbomFile.value = event.newValue;
    }
  };
  
  // 从LocalStorage获取当前SBOM文件
  const loadCurrentSbomFile = () => {
    const storedFile = localStorage.getItem('currentSBOMFile');
    if (storedFile) {
      currentSbomFile.value = storedFile;
    }
  };
  
  // 加载SBOM文件详情
  const loadSbomDetails = async () => {
    if (!currentSbomFile.value) return;
    
    loading.value = true;
    try {
      // 模拟API调用，实际项目中应从后端获取SBOM详情
      await new Promise(resolve => setTimeout(resolve, 500));
      
      // 模拟SBOM详情数据
      sbomDetails.value = {
        name: currentSbomFile.value.split('_')[0] + ' SBOM',
        format: currentSbomFile.value.includes('_spdx_') ? 'SPDX' : 
                currentSbomFile.value.includes('_cdx_') ? 'CDX' : 'SWID',
        created: new Date().toLocaleString(),
        packages: [
          { name: "example-package-1", version: "1.0.0" },
          { name: "example-package-2", version: "2.3.1" },
          { name: "example-package-3", version: "0.9.5" },
          { name: "react", version: "17.0.2" },
          { name: "lodash", version: "4.17.21" },
          { name: "axios", version: "0.24.0" }
        ]
      };
    } catch (error) {
      console.error('加载SBOM详情失败:', error);
    } finally {
      loading.value = false;
    }
  };
  
  onMounted(() => {
    loadCurrentSbomFile();
    window.addEventListener('storage', handleStorageChange);
  });
  </script>
  
  <style scoped>
  .sbom-list {
    border: 1px solid #ccc;
    padding: 15px;
    height: 100%;
    box-sizing: border-box;
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
  }
  
  h3 {
    margin-top: 0;
    margin-bottom: 15px;
    text-align: center;
    font-size: 16px;
    color: #333;
    font-weight: bold;
  }
  
  .content {
    flex: 1;
    overflow: auto;
  }
  
  .empty-state, .loading {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    color: #888;
    font-style: italic;
  }
  
  .sbom-details {
    padding: 10px;
  }
  
  h4, h5 {
    margin-top: 10px;
    margin-bottom: 10px;
    color: #444;
  }
  
  .view-btn {
    margin-top: 10px;
    padding: 5px 10px;
    background-color: #4285f4;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .view-btn:hover {
    background-color: #3367d6;
  }
  
  .details-container {
    margin-top: 15px;
    border-top: 1px solid #eee;
    padding-top: 10px;
  }
  
  .packages-list {
    list-style-type: none;
    padding: 0;
    margin: 0;
  }
  
  .packages-list li {
    padding: 5px 0;
    border-bottom: 1px dotted #eee;
  }
  
  .packages-list li:last-child {
    border-bottom: none;
  }
  </style>