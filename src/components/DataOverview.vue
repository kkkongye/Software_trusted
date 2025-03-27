<template>
  <div class="wrapper">
    <h2 class="Heading">Data Overview</h2>
    <div class="main_container">

      <!-- Upload Button with Functionality -->
      <div class="upload-container">
        <div class="upload-button" @click="triggerFileUpload">
          <span>Upload</span>
          <div class="upload-icon-container">
            <img src="@/assets/upload.svg" alt="Upload Icon" class="upload-icon" />
          </div>
          <input type="file" ref="fileInput" style="display: none" @change="handleFileChange" />
        </div>

        <!-- Display uploaded file name -->
        <span v-if="uploadedFileName" class="uploaded-file-name">{{ uploadedFileName }}</span>
      </div>

      <!-- Centered text under each divider -->
      <div class="centered-content">
        <el-divider content-position="left">Interval</el-divider>
        <span class="centered-content-text">{{Interval}}</span>
      </div>

      <div class="centered-content">
        <el-divider content-position="left">Items</el-divider>
        <span class="centered-content-text">{{Items}}</span>
      </div>

      <div class="centered-content">
        <el-divider content-position="left">Features</el-divider>
        <span class="centered-content-text">{{Features}}</span>
      </div>

    </div>
  </div>
</template>

<script>
import { Card, message } from 'ant-design-vue';
import { ref } from 'vue';
import { ElDivider } from 'element-plus';
import { useIntervalStore } from '../stores/Interval';

export default {
  components: {
    'a-card': Card,
    ElDivider,
  },
  setup() {
    const Interval = ref(null);
    const Items = ref(null);
    const Features = ref(null);
    const fileInput = ref(null);
    const uploadedFileName = ref(null);

    Interval.value = '2021/1/1-2023/5/23';
    Items.value = '874';
    Features.value = '14';

    const startDate = Interval.value.split('-')[0];  // 获取起始日期

    const endDate = Interval.value.split('-')[1];  // 获取结束日期

    // 获取 useIntervalStore 并更新其值
    const intervalStore = useIntervalStore();
    intervalStore.setInterval({
      startDate: startDate,
      endDate: endDate,
    });

    const triggerFileUpload = () => {
      fileInput.value.click();
    };

    const handleFileChange = (event) => {
      const file = event.target.files[0];
      if (file) {
        uploadedFileName.value = file.name;
        message.success(`File ${file.name} uploaded successfully!`);
      }
    };

    return {
      Interval,
      Items,
      Features,
      triggerFileUpload,
      handleFileChange,
      fileInput,
      uploadedFileName
    };
  }
};
</script>

<style scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  height: 100vh;
  /* 适应视窗高度 */
  padding: 0px;
  border: 1px solid #e0e0e0;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

.Heading {
  height: 30px;
  width: 100%;
  background: linear-gradient(to bottom, rgb(244, 244, 244), rgb(233, 233, 233));
  color: black;
  font-size: 18px;
  text-align: left;
  font-family: "JetBrains Mono";
  font-weight: bold;
  padding: 5px 10px;
  border-radius: 8px 8px 0 0;
}

.main_container {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  /* 扩展高度 */
  gap: 10px;
  padding: 10px 2px;
  justify-content: space-around;
  /* 使元素均匀分布 */
}

.centered-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.centered-content-text {
  font-size: 14px;
  font-weight: bold;
}

.upload-container {
  display: flex;
  align-items: center;
  /* 去掉 justify-content: center; */
  margin-left: 10px;
  /* 让容器整体距左侧 10px */
}

.upload-button {
  background-color: #e0e0e0;
  padding: 5px 8px;
  border-radius: 5px;
  display: flex;
  align-items: center;
  cursor: pointer;
  gap: 8px;
  font-weight: bold;
  font-size: 14px;
  color: #000000;
  transition: color 0.2s;
  margin-left: 0;
  /* 去掉多余的 margin */
}


.upload-button:hover {
  color: #0056b3;
}

.upload-icon-container {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #e1e1e1;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  transition: background-color 0.3s;
}

.upload-button:hover .upload-icon-container {
  background-color: #aadffb;
}

.upload-icon {
  width: 12px;
  height: 12px;
  transition: transform 0.3s;
}

.upload-button:active .upload-icon {
  transform: scale(0.9);
}

.uploaded-file-name {
  margin-left: 10px;
  font-size: 14px;
  color: #555;
}

/* 使用 ::v-deep 修改 el-divider 样式 */
::v-deep .el-divider {
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: -60px;
  font-style: italic;
}
</style>
