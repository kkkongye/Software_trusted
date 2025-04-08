<template>
  <div class="main-page">
    <!-- 左列 - 文件上传和漏洞图表 -->
    <div class="column left-column">
      <div class="column-content">
        <div class="file-upload-container">
          <FileUpload />
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
import { ref } from 'vue';
import FileUpload from './FileUpload.vue';
import VulnerabilityChart from './VulnerabilityChart.vue';
import VulnerabilityList from './VulnerabilityList.vue';
import SBOMList from './SBOMList.vue';

const vulnerabilityData = ref({
  critical: 0,
  high: 0,
  medium: 0,
  low: 0,
  unknown: 0
});
</script>

<style scoped>
.main-page {
  display: grid;
  grid-template-columns: 1.2fr 1.4fr 1fr; /* 三列布局，中间列宽度是左列和右列的两倍 */
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
}
</style>