<template>
  <div class="main-page">
    <!-- 左列 - 文件上传和漏洞图表 -->
    <div class="column left-column">
      <div class="column-content">
        <div class="file-upload-container">
          <FileUpload ref="fileUploadRef" @vulnerabilityDataUpdated="updateVulnerabilityData" />
        </div>
        <div class="vulnerability-chart-container">
          <VulnerabilityChart :data="vulnerabilityData" />
        </div>
      </div>
    </div>

    <!-- 中间列 - SBOM清单 -->
    <div class="column middle-column">
      <div class="column-content">
        <SBOMList />
      </div>
    </div>

    <!-- 右列 - 漏洞清单信息 -->
    <div class="column right-column">
      <div class="column-content">
        <VulnerabilityList />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import FileUpload from './FileUpload.vue';
import VulnerabilityChart from './VulnerabilityChart.vue';
import VulnerabilityList from './VulnerabilityList.vue';
import SBOMList from './SBOMList.vue';

const defaultVulnerabilityData = {
  critical: 0,
  high: 0,
  medium: 0,
  low: 0,
  unknown: 0
};

const vulnerabilityData = ref({...defaultVulnerabilityData});
const fileUploadRef = ref(null);

// 从本地存储加载漏洞设置
const loadVulnerabilitySettings = () => {
  const savedSettings = localStorage.getItem('vulnerabilitySettings');
  if (savedSettings) {
    try {
      const parsedSettings = JSON.parse(savedSettings);
      vulnerabilityData.value = parsedSettings;
    } catch (e) {
      console.error('Failed to parse saved vulnerability settings', e);
    }
  }
};

// 处理FileUpload组件发出的漏洞数据更新事件
const updateVulnerabilityData = (newData) => {
  // 直接更新漏洞数据，不再检查是否为0
  vulnerabilityData.value = { ...newData };
  
  // 保存到本地存储
  try {
    localStorage.setItem('vulnerabilitySettings', JSON.stringify(newData));
    
    // 确保所有组件都能感知到变化
    if (Object.values(newData).some(val => val > 0)) {
      localStorage.setItem('vulnReportGenerated', 'true');
      
      // 触发事件，确保其他组件更新
      window.dispatchEvent(new StorageEvent('storage', {
        key: 'vulnerabilitySettings',
        newValue: JSON.stringify(newData),
        url: window.location.href
      }));
      
      window.dispatchEvent(new StorageEvent('storage', {
        key: 'vulnReportGenerated',
        newValue: 'true',
        url: window.location.href
      }));
    }
  } catch (e) {
    console.error('Failed to save vulnerability settings', e);
  }
};

onMounted(() => {
  // 清除之前的状态，确保每次页面加载都是新的状态
  localStorage.removeItem('vulnReportGenerated');
  localStorage.removeItem('sbomGenerated');
  localStorage.removeItem('currentSBOMFile');
  localStorage.removeItem('vulnerabilitySettings');
  
  // 重置数据
  vulnerabilityData.value = {...defaultVulnerabilityData};
});
</script>

<style scoped>
.main-page {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr; /* 三列布局，三列等宽 */
  gap: 10px; /* 减小列间距 */
  height: calc(100vh - 60px); /* 占满整个页面高度，减去导航栏的高度 */
  width: 100vw;
  padding: 20px 20px 20px 10px; /* 上右下左内边距，左边只有10px */
  background-color: #f0f0f0; /* 页面背景颜色 */
  box-sizing: border-box;
}

.column {
  box-sizing: border-box;
}

.column-content {
  height: 100%;
  display: flex;
  flex-direction: column;
}

.left-column .column-content {
  gap: 20px; /* 文件上传和类型选择之间的间距 */
}

.file-upload-container {
  flex: 1; /* 文件上传占据左列的一半空间 */
}

.type-selection-container {
  flex: 1; /* 类型选择占据左列的一半空间 */
}

/* 左列特殊样式 */
.left-column {
  padding-left: 0; /* 移除左侧内边距 */
  padding-right: 0; /* 减少右侧内边距 */
}

/* 中间列特殊样式 */
.middle-column {
  padding-left: 0; /* 移除左侧内边距 */
}

/* 通用块样式 */
.file-upload,
.type-selection,
.vulnerability-list,
.sbom-list,
.software-identifier {
  background-color: #ffffff; /* 块背景颜色 */
  border: 1px solid #ccc; /* 块边框 */
  border-radius: 10px; /* 圆角边框 */
  padding: 15px; /* 内边距 */
  overflow: auto; /* 内容超出时显示滚动条 */
  height: 100%; /* 占满父容器高度 */
  width: 100%; /* 占满父容器宽度 */
  box-sizing: border-box;
}

.vulnerability-chart-container {
  flex: 1;
  background-color: #ffffff;
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 15px;
  overflow: auto;
  height: 100%;
  width: 100%;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  max-height: 50vh; /* 限制最大高度为视口高度的50% */
}
</style>