<template>
  <div class="login-container">
    <div class="login-content">
      <div class="login-logo">
        <div class="logo-circle">
          <h1>STS</h1>
        </div>
        <h2>杞欢鍙俊璁よ瘉绯荤粺</h2>
        <p class="tagline">瀹夊叏銆佸彲闈犵殑杞欢淇′换绠＄悊骞冲彴</p>
      </div>
      <div class="login-form">
        <h3>鐢ㄦ埛鐧诲綍</h3>
        <div class="form-group">
          <label for="username">
            <i class="user-icon">馃懁</i>
            <span>鐢ㄦ埛鍚?/span>
          </label>
          <input 
            type="text" 
            id="username" 
            v-model="username" 
            placeholder="璇疯緭鍏ョ敤鎴峰悕"
            @keyup.enter="handleLogin"
            autocomplete="username"
          />
        </div>
        <div class="form-group">
          <label for="password">
            <i class="password-icon">馃敀</i>
            <span>瀵嗙爜</span>
          </label>
          <input 
            type="password" 
            id="password" 
            v-model="password" 
            placeholder="璇疯緭鍏ュ瘑鐮?
            @keyup.enter="handleLogin"
            autocomplete="current-password"
          />
        </div>
        <div class="login-options">
          <div class="remember-me">
            <input type="checkbox" id="remember" v-model="rememberMe" />
            <label for="remember">璁颁綇鎴?/label>
          </div>
          <a href="#" class="forgot-password">蹇樿瀵嗙爜?</a>
        </div>
        <button 
          class="login-btn" 
          @click="handleLogin" 
          :disabled="isLoading"
          :class="{ 'loading': isLoading }"
        >
          <span class="btn-text">{{ isLoading ? '鐧诲綍涓? : '鐧?褰? }}</span>
          <span v-if="isLoading" class="spinner"></span>
        </button>
        <div v-if="errorMsg" class="error-message">
          <i class="error-icon">鉂?/i> {{ errorMsg }}
        </div>
      </div>
    </div>
    <div class="login-footer">
      <p>漏 2023 杞欢鍙俊璁よ瘉绯荤粺 鐗堟潈鎵€鏈?/p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

// 鐘舵€佸彉閲?
const username = ref('');
const password = ref('');
const rememberMe = ref(false);
const isLoading = ref(false);
const errorMsg = ref('');
const router = useRouter();

// 妯℃嫙鐧诲綍閫昏緫
const handleLogin = async () => {
  // 琛ㄥ崟楠岃瘉
  if (!username.value || !password.value) {
    errorMsg.value = '璇疯緭鍏ョ敤鎴峰悕鍜屽瘑鐮?;
    return;
  }
  
  try {
    isLoading.value = true;
    errorMsg.value = '';
    
    // 妯℃嫙API璇锋眰
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    // 鍋囪鐢ㄦ埛鍚嶆槸admin锛屽瘑鐮佹槸123456锛屽疄闄呴」鐩腑搴旂敱鍚庣楠岃瘉
    if (username.value === 'admin' && password.value === '123456') {
      // 瀛樺偍鐧诲綍鐘舵€佸埌鏈湴瀛樺偍
      localStorage.setItem('isLoggedIn', 'true');
      localStorage.setItem('username', username.value);
      if (rememberMe.value) {
        localStorage.setItem('rememberMe', 'true');
      }
      
      // 鐧诲綍鎴愬姛锛岃烦杞埌涓婚〉
      router.push('/');
    } else {
      errorMsg.value = '鐢ㄦ埛鍚嶆垨瀵嗙爜閿欒';
    }
  } catch (error) {
    errorMsg.value = '鐧诲綍澶辫触锛岃绋嶅悗鍐嶈瘯';
    console.error('鐧诲綍閿欒:', error);
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
