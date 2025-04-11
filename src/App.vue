<template>
  <div class="background">
    <!-- 只在非登录页面显示导航栏 -->
    <NavBar v-if="!isLoginPage" />
    <div class="view-container" :class="{ 'with-navbar': !isLoginPage }">
      <router-view />
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { defineComponent } from 'vue';
import NavBar from './components/NavBar.vue';

const route = useRoute();
const isLoginPage = computed(() => route.name === 'Login');

// 在应用初始化时检查状态
onMounted(() => {
  // 检查是否是首次加载或刷新页面
  const isPageRefresh = !sessionStorage.getItem('app_initialized');
  sessionStorage.setItem('app_initialized', 'true');
  
  // 如果是刷新页面，强制重置所有漏洞相关状态
  if (isPageRefresh) {
    localStorage.setItem('vulnReportGenerated', 'false');
    localStorage.removeItem('vulnerabilitySettings');
    console.log('页面刷新：重置所有漏洞相关状态');
  } else {
    // 常规检查：如果没有实际数据但标志为true，重置标志
    const savedSettings = localStorage.getItem('vulnerabilitySettings');
    const vulnReportGenerated = localStorage.getItem('vulnReportGenerated') === 'true';
    
    if (vulnReportGenerated) {
      const hasRealData = savedSettings && Object.values(JSON.parse(savedSettings || '{}')).some(val => val > 0);
      
      if (!hasRealData) {
        localStorage.setItem('vulnReportGenerated', 'false');
        console.log('重置漏洞报告生成状态：没有实际数据');
      }
    }
  }
});

// import DataOverview from '@/components/DataOverview.vue';
// import LeftButton from '@/components/LeftButton.vue';
// import MainPage from '@/components/MainPage.vue';

// 使用 defineComponent 在组合式 API 中定义组件
defineComponent({});

// 检查文件是否存在，如果不存在则先尝试创建App.vue
</script>

<style scoped>
.background {
  display: flex;
  flex-direction: column;
  width: 100vw;
  height: 100vh;
  background-color: #efefef;
  overflow: auto;
  /* 允许滚动以防止内容溢出 */
}

.view-container {
  background-color: #fff;
  width: 100vw;
  height: 100vh;
  border: 2px solid #efefef;
  border-radius: 8px;
  box-sizing: border-box;
  overflow: hidden;
  /* 防止内容溢出 */
}

/* 添加导航栏后的视图容器调整 */
.view-container.with-navbar {
  height: calc(100vh - 60px);
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
