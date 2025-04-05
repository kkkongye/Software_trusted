<template>
  <div>
    <nav class="nav-bar">
      <router-link to="/" class="nav-item active">主页</router-link>
      <router-link to="/vulnerabilities" class="nav-item">漏洞清单信息</router-link>
    </nav>
    <MainPage />
  </div>
</template>

<script setup>
import MainPage from '../components/MainPage.vue';
</script>

<style scoped>
.nav-bar {
  display: flex;
  background-color: #333;
  padding: 10px 20px;
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-item {
  color: white;
  text-decoration: none;
  padding: 10px 15px;
  margin-right: 10px;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.nav-item:hover, .nav-item.active {
  background-color: #555;
}

.nav-item.active {
  font-weight: bold;
}
</style>
