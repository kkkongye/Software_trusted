// main.js
import { createApp } from 'vue';
import { createPinia } from 'pinia';
import Antd from 'ant-design-vue';
import App from './App.vue';
import router from './router'; // 导入路由
import 'ant-design-vue/dist/reset.css';
import * as echarts from 'echarts';
import axios from 'axios';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import '@fortawesome/fontawesome-free/css/all.css';


const app = createApp(App);

// 创建 Pinia 实例
const pinia = createPinia();

// 配置全局属性
app.config.globalProperties.$echarts = echarts;

// 配置全局的 axios 实例
// app.config.globalProperties.$axios = axios.create({
//   baseURL: 'https://www.hdvis.net:8001',
//   timeout: 5000,
// });

// 挂载 Pinia、Antd 和 Element Plus 插件以及路由
app.use(pinia).use(Antd).use(ElementPlus).use(router).mount('#app');
