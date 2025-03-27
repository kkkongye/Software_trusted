<template>
  <div class="background">
    <div class="view-container">
      <!-- <DataOverview class="DataOverview-card" /> -->
      <!-- <LeftButton class="LeftButton-card" /> -->
      <MainPage class="LeftButton-card" />
     </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { defineComponent } from 'vue';

// import DataOverview from '@/components/DataOverview.vue';
// import LeftButton from '@/components/LeftButton.vue';
import MainPage from '@/components/MainPage.vue';





// 使用 defineComponent 在组合式 API 中定义组件

defineComponent({
  components: {

    // DataOverview,
    // LeftButton,
    MainPage
    // 'a-card': Card,

  },
});
</script>

<style scoped>
.background {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100vw;
  height: 100vh;
  background-color: #efefef;
  overflow: auto;
  /* 允许滚动以防止内容溢出 */
}





.view-container {
  background-color: #fff;
  display: grid;
  grid-template-rows: repeat(7, 1fr);
  grid-template-columns: repeat(12, 1fr);
  gap: 2px;
  border: 2px solid #efefef;
  border-radius: 8px;
  box-sizing: border-box;
  justify-items: center;
  /* 水平居中网格单元内容 */
  align-items: center;
  /* 垂直居中网格单元内容 */
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  /* 防止内容溢出 */
}

/* 默认组件样式 */
.DataOverview-card {
  grid-row: 1 / 3;
  grid-column: 1 / 4;
  border: 2px solid #efefef;
  border-radius: 8px;
  transition: box-shadow 0.3s ease;
}

.DataOverview-card:hover {
  box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.4);
}


/* 确保子组件填满网格单元但不被拉伸 */
.DataOverview-card{
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  /* 可根据需要调整内边距 */
  overflow: hidden;
  /* 允许内部滚动以避免内容溢出 */
}


</style>
