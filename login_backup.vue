<template>
  <div class="login-container">
    <div class="login-content">
      <div class="login-logo">
        <div class="logo-circle">
          <h1>STS</h1>
        </div>
        <h2>软件可信认证系统</h2>
        <p class="tagline">安全、可靠的软件信任管理平台</p>
      </div>
      <div class="login-form">
        <h3>用户登录</h3>
        <div class="form-group">
          <label for="username">
            <i class="user-icon">👤</i>
            <span>用户名</span>
          </label>
          <input 
            type="text" 
            id="username" 
            v-model="username" 
            placeholder="请输入用户名"
            @keyup.enter="handleLogin"
            autocomplete="username"
          />
        </div>
        <div class="form-group">
          <label for="password">
            <i class="password-icon">🔒</i>
            <span>密码</span>
          </label>
          <input 
            type="password" 
            id="password" 
            v-model="password" 
            placeholder="请输入密码"
            @keyup.enter="handleLogin"
            autocomplete="current-password"
          />
        </div>
        <div class="login-options">
          <div class="remember-me">
            <input type="checkbox" id="remember" v-model="rememberMe" />
            <label for="remember">记住我</label>
          </div>
          <a href="#" class="forgot-password">忘记密码?</a>
        </div>
        <button 
          class="login-btn" 
          @click="handleLogin" 
          :disabled="isLoading"
          :class="{ 'loading': isLoading }"
        >
          <span class="btn-text">{{ isLoading ? '登录中' : '登 录' }}</span>
          <span v-if="isLoading" class="spinner"></span>
        </button>
        <div v-if="errorMsg" class="error-message">
          <i class="error-icon">❗</i> {{ errorMsg }}
        </div>
      </div>
    </div>
    <div class="login-footer">
      <p>© 2023 软件可信认证系统 版权所有</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

// 状态变量
const username = ref('');
const password = ref('');
const rememberMe = ref(false);
const isLoading = ref(false);
const errorMsg = ref('');
const router = useRouter();

// 模拟登录逻辑
const handleLogin = async () => {
  // 表单验证
  if (!username.value || !password.value) {
    errorMsg.value = '请输入用户名和密码';
    return;
  }
  
  try {
    isLoading.value = true;
    errorMsg.value = '';
    
    // 模拟API请求
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    // 假设用户名是admin，密码是123456，实际项目中应由后端验证
    if (username.value === 'admin' && password.value === '123456') {
      // 存储登录状态到本地存储
      localStorage.setItem('isLoggedIn', 'true');
      localStorage.setItem('username', username.value);
      if (rememberMe.value) {
        localStorage.setItem('rememberMe', 'true');
      }
      
      // 登录成功，跳转到主页
      router.push('/');
    } else {
      errorMsg.value = '用户名或密码错误';
    }
  } catch (error) {
    errorMsg.value = '登录失败，请稍后再试';
    console.error('登录错误:', error);
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f0f0f0;
  background-color: #f8f8f8;
  background-image: none;
  padding: 20px;
}

.login-content {
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 500px;
  background-color: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  animation: fadeIn 0.8s ease;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-20px); }
  to { opacity: 1; transform: translateY(0); }
}

.login-logo {
  padding: 30px 20px;
  text-align: center;
  background-color: rgba(44, 62, 80, 0.05);
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
}

.logo-circle {
  width: 80px;
  height: 80px;
  margin: 0 auto 20px;
  background: linear-gradient(135deg, #444444, #222222);
  background: linear-gradient(135deg, #999999, #777777);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.logo-circle h1 {
  margin: 0;
  font-size: 24px;
  color: white;
  letter-spacing: 1px;
}

.login-logo h2 {
  margin: 0;
  font-size: 22px;
  font-weight: 600;
  color: #2c3e50;
}

.tagline {
  margin: 10px 0 0;
  font-size: 14px;
  color: #7f8c8d;
}

.login-form {
  padding: 30px 40px;
}

.login-form h3 {
  margin: 0 0 25px;
  font-size: 18px;
  color: #2c3e50;
  text-align: center;
  font-weight: 600;
}

.form-group {
  margin-bottom: 20px;
  position: relative;
}

.form-group label {
  display: flex;
  align-items: center;
  margin-bottom: 8px;
  font-weight: 500;
  color: #34495e;
  font-size: 14px;
}

.form-group i {
  margin-right: 8px;
  font-size: 16px;
  color: #4a90e2;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 12px 15px;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  font-size: 15px;
  color: #2c3e50;
  background-color: #f9f9f9;
  box-sizing: border-box;
  transition: all 0.3s ease;
}

input[type="text"]:focus,
input[type="password"]:focus {
  border-color: #4a90e2;
  box-shadow: 0 0 0 3px rgba(74, 144, 226, 0.15);
  background-color: white;
  outline: none;
}

input[type="text"]::placeholder,
input[type="password"]::placeholder {
  color: #bdc3c7;
}

.login-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
}

.remember-me {
  display: flex;
  align-items: center;
}

.remember-me input {
  margin-right: 8px;
  accent-color: #4a90e2;
}

.remember-me label {
  font-size: 14px;
  color: #7f8c8d;
  cursor: pointer;
}

.forgot-password {
  font-size: 14px;
  color: #4a90e2;
  text-decoration: none;
  transition: color 0.3s;
}

.forgot-password:hover {
  color: #3a7bca;
  text-decoration: underline;
}

.login-btn {
  position: relative;
  width: 100%;
  padding: 14px 20px;
  background: linear-gradient(to right, #555555, #333333);
  background: linear-gradient(to right, #999999, #777777);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-btn:hover {
  background: linear-gradient(to right, #444444, #222222);
  background: linear-gradient(to right, #888888, #666666);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.login-btn:disabled {
  background: linear-gradient(to right, #999999, #777777);
  background: linear-gradient(to right, #cccccc, #bbbbbb);
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

.login-btn .btn-text {
  margin-right: 8px;
}

.spinner {
  display: inline-block;
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  border-top-color: white;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error-message {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 20px;
  padding: 10px;
  color: #c0392b;
  background-color: rgba(231, 76, 60, 0.1);
  border-radius: 6px;
  font-size: 14px;
}

.error-icon {
  margin-right: 8px;
  font-size: 16px;
}

.login-footer {
  margin-top: 25px;
  font-size: 13px;
  color: rgba(255, 255, 255, 0.8);
  color: rgba(50, 50, 50, 0.8);
  text-align: center;
}
</style> 