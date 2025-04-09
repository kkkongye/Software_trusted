import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import VulnerabilityPage from '../views/VulnerabilityPage.vue'
import IdentifierPage from '../views/IdentifierPage.vue'
import VulnerabilitySettingsPage from '../views/VulnerabilitySettingsPage.vue'
import MainPage from '../components/MainPage.vue'
import Login from '../components/Login.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: MainPage,
    meta: { requiresAuth: true }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { requiresAuth: false }
  },
  {
    path: '/sbom',
    name: 'SBOM',
    component: MainPage,
    meta: { requiresAuth: true }
  },
  {
    path: '/identifier',
    name: 'Identifier',
    component: IdentifierPage,
    meta: { requiresAuth: true }
  },
  {
    path: '/vulnerability-settings',
    name: 'VulnerabilitySettings',
    component: VulnerabilitySettingsPage,
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 全局前置守卫，验证用户是否已登录
router.beforeEach((to, from, next) => {
  const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true'
  
  if (to.meta.requiresAuth && !isLoggedIn) {
    // 需要登录但未登录，重定向到登录页
    next({ name: 'Login' })
  } else if (to.name === 'Login' && isLoggedIn) {
    // 已登录用户访问登录页，重定向到首页
    next({ name: 'Home' })
  } else {
    // 其他情况正常放行
    next()
  }
})

export default router 