<template>
  <div class="main-page">
    <!-- 左列 -->
    <div class="left-column">
      <FileUpload />
      <TypeSelection />
    </div>

    <!-- 中间列 -->
    <div class="middle-column">
      <SBOMList />
    </div>

    <!-- 右列 -->
    <div class="right-column">
      <SoftwareIdentifier />
    </div>
  </div>
</template>

<script setup>
import FileUpload from './FileUpload.vue';
import TypeSelection from './TypeSelection.vue';
import VulnerabilityList from './VulnerabilityList.vue';
import SBOMList from './SBOMList.vue';
import SoftwareIdentifier from './SoftwareIdentifier.vue';
</script>

<style scoped>
.main-page {
  display: grid;
  grid-template-columns: 1.2fr 1.4fr 1fr; /* 三列布局，中间列宽度是左列和右列的两倍 */
  grid-template-rows: 1fr; /* 单行，高度占满页面 */
  gap: 0px; /* 列间距 */
  height: calc(100vh - 60px); /* 占满整个页面高度，减去导航栏的高度 */
  width: 100vw;
  padding: 1px; /* 页面内边距 */
  background-color: #f0f0f0; /* 页面背景颜色 */
  overflow: auto; /* 页面内容超出时显示滚动条 */
}

.left-column {
  display: flex;
  flex-direction: column;
  gap: 5px; /* 左列内部模块间距 */
  min-height: 0; /* 允许内容超出时滚动 */
}

.middle-column {
  flex: 2; /* SBOM清单模块占中间列 */
  margin-bottom: 20px;
  min-height: 0; /* 允许内容超出时滚动 */
}

.right-column {
  flex: 1; /* 软件标识管理模块占右列 */
  margin-bottom: 20px;
  min-height: 0; /* 允许内容超出时滚动 */
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
}
</style>