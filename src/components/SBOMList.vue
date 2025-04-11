<template>
    <div class="sbom-list">
      <h3>SBOM清单</h3>
      <div class="content">
        <div v-if="loading" class="loading">
          <p>加载中...</p>
        </div>
        <div v-else-if="!sbomGenerated || !currentSbomFile" class="empty-state">
          <p>暂无SBOM清单</p>
          <div class="instruction">
            请先上传软件包，然后点击"生成SBOM清单"按钮进行软件物料清单生成。
          </div>
        </div>
        <div v-else class="sbom-details">
          <h4>SBOM文件信息</h4>
          <p>文件名: {{ currentSbomFile }}</p>
          
          <button class="view-btn" @click="showDetailList = !showDetailList">
            {{ showDetailList ? '隐藏详情' : '查看详情' }}
          </button>
          
          <div v-if="showDetailList" class="details-container">
            <h5>软件包依赖列表</h5>
            <ul class="packages-list">
              <li v-for="(pkg, index) in sbomDetails?.packages || []" :key="index" 
                  class="package-item">
                <div class="package-header" @click="togglePackageDetails(index)">
                  <span><strong>{{ pkg.name }}</strong> - 版本: {{ pkg.version }}</span>
                  <span class="toggle-icon">{{ expandedPackages[index] ? '▼' : '▶' }}</span>
                </div>
                <div v-if="expandedPackages[index]" class="package-expanded-details">
                  <div><strong>名称:</strong> {{ pkg.name }}</div>
                  <div><strong>版本:</strong> {{ pkg.version }}</div>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import apiService from '../api';
  
  const loading = ref(false);
  const currentSbomFile = ref('');
  const sbomDetails = ref(null);
  const sbomGenerated = ref(false);
  const showDetailList = ref(false);
  const expandedPackages = ref({});
  
  // 切换包详情的展开/折叠状态
  const togglePackageDetails = (index) => {
    expandedPackages.value = {
      ...expandedPackages.value,
      [index]: !expandedPackages.value[index]
    };
  };
  
  // 监听LocalStorage变化
  const handleStorageChange = (event) => {
    if (event.key === 'currentSBOMFile') {
      if (event.newValue && event.newValue.trim() !== '') {
        sbomGenerated.value = true;
        localStorage.setItem('sbomGenerated', 'true');
        currentSbomFile.value = event.newValue;
        loadSbomDetails(); // 加载SBOM详情
      } else {
        sbomGenerated.value = false;
        localStorage.setItem('sbomGenerated', 'false');
        currentSbomFile.value = '';
      }
    } else if (event.key === 'sbomGenerated') {
      sbomGenerated.value = event.newValue === 'true';
    }
  };
  
  // 从LocalStorage获取当前SBOM文件
  const loadCurrentSbomFile = () => {
    const storedFile = localStorage.getItem('currentSBOMFile');
    if (storedFile && storedFile.trim() !== '') {
      sbomGenerated.value = true;
      localStorage.setItem('sbomGenerated', 'true');
      currentSbomFile.value = storedFile;
    } else {
      localStorage.removeItem('currentSBOMFile');
      localStorage.setItem('sbomGenerated', 'false');
      sbomGenerated.value = false;
      currentSbomFile.value = '';
    }
  };
  
  // 加载SBOM文件详情
  const loadSbomDetails = async () => {
    if (!currentSbomFile.value) return;
    
    loading.value = true;
    try {
      // 使用API服务获取SBOM详情
      console.log('正在请求SBOM详情，文件名:', currentSbomFile.value);
      const response = await apiService.getSBOMDetails(currentSbomFile.value);
      console.log('SBOM详情响应数据:', response.data);
      sbomDetails.value = response.data;
      
      // 检查包是否为空
      if (!response.data.packages || response.data.packages.length === 0) {
        console.warn('SBOM详情中没有包信息');
      }
    } catch (error) {
      console.error('加载SBOM详情失败:', error);
      console.error('错误详情:', error.response ? error.response.data : '无响应数据');
      // 错误处理，例如显示错误消息
      sbomDetails.value = {
        name: '加载失败',
        packages: []
      };
    } finally {
      loading.value = false;
    }
  };
  
  onMounted(() => {
    const generated = localStorage.getItem('sbomGenerated') === 'true';
    sbomGenerated.value = generated;
    
    if (generated) {
      loadCurrentSbomFile();
      // 自动加载SBOM详情
      loadSbomDetails();
    }
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
    display: flex;
    flex-direction: column;
  }
  
  .empty-state, .loading {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    color: #888;
    font-style: italic;
    background-color: #f9f9f9;
    border-radius: 8px;
    flex-direction: column;
  }
  
  .empty-state p {
    margin: 10px 0;
    font-size: 14px;
  }
  
  .empty-state .instruction {
    font-style: normal;
    font-size: 12px;
    color: #666;
    margin-top: 10px;
    text-align: center;
    max-width: 80%;
  }
  
  .sbom-details {
    padding: 10px;
    display: flex;
    flex-direction: column;
    flex: 1;
    min-height: 0;
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
    flex: 1;
    min-height: 200px;
    max-height: calc(100vh - 300px);
    overflow-y: auto;
  }
  
  .packages-list {
    list-style-type: none;
    padding: 0;
    margin: 0;
    max-width: 100%;
  }
  
  .package-item {
    padding: 8px;
    font-size: 14px;
    color: #555;
    border-bottom: 1px solid #eee;
    border-radius: 4px;
    margin-bottom: 5px;
  }
  
  .package-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    padding: 3px 0;
  }
  
  .toggle-icon {
    font-size: 12px;
    color: #666;
  }
  
  .package-expanded-details {
    margin-top: 8px;
    padding: 8px;
    background-color: rgba(249, 249, 249, 0.8);
    border-radius: 4px;
    font-size: 13px;
    line-height: 1.4;
  }
  
  .package-expanded-details div {
    margin-bottom: 5px;
  }
  </style>