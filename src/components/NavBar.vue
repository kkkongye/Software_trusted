<template>
  <div class="navbar">
    <div class="logo">
      <h1>软件可信认证系统</h1>
    </div>
    <div class="nav-links">
      <router-link to="/" class="nav-link">首页</router-link>
      <router-link to="/vulnerabilities" class="nav-link">漏洞清单</router-link>
    </div>
    <div class="user-section" v-if="isLoggedIn">
      <div class="dropdown">
        <button class="dropdown-btn">
          <span class="username">{{ username }}</span>
          <i class="dropdown-icon">▼</i>
        </button>
        <div class="dropdown-content">
          <button class="dropdown-item" @click="handleLogout">退出登录</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const isLoggedIn = ref(false);
const username = ref('');

// 在组件挂载时检查登录状态
onMounted(() => {
  checkLoginStatus();
});

// 检查用户是否已登录
const checkLoginStatus = () => {
  const loginStatus = localStorage.getItem('isLoggedIn');
  if (loginStatus === 'true') {
    isLoggedIn.value = true;
    username.value = localStorage.getItem('username') || '用户';
  } else {
    isLoggedIn.value = false;
    // 如果未登录且不在登录页面，则重定向到登录页
    if (router.currentRoute.value.path !== '/login') {
      router.push('/login');
    }
  }
};

// 处理退出登录
const handleLogout = () => {
  // 清除登录状态
  localStorage.removeItem('isLoggedIn');
  localStorage.removeItem('username');
  localStorage.removeItem('rememberMe');
  
  // 更新组件状态
  isLoggedIn.value = false;
  username.value = '';
  
  // 重定向到登录页
  router.push('/login');
};
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 60px;
  padding: 0 20px;
  background-color: #2c3e50;
  color: white;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.logo h1 {
  margin: 0;
  font-size: 20px;
  font-weight: 500;
}

.nav-links {
  display: flex;
  gap: 20px;
}

.nav-link {
  color: white;
  text-decoration: none;
  font-size: 16px;
  padding: 5px 10px;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.nav-link:hover,
.router-link-active {
  background-color: rgba(255, 255, 255, 0.1);
}

.user-section {
  position: relative;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  background: none;
  border: none;
  color: white;
  font-size: 16px;
  cursor: pointer;
  padding: 8px 12px;
  border-radius: 4px;
}

.dropdown-btn:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.dropdown-icon {
  font-size: 12px;
}

.dropdown-content {
  display: none;
  position: absolute;
  right: 0;
  background-color: white;
  min-width: 160px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  z-index: 1;
  border-radius: 4px;
  overflow: hidden;
}

.dropdown:hover .dropdown-content {
  display: block;
}

.dropdown-item {
  color: #333;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  border: none;
  width: 100%;
  text-align: left;
  background: none;
  cursor: pointer;
  transition: background-color 0.3s;
}

.dropdown-item:hover {
  background-color: #f5f5f5;
}
</style> 