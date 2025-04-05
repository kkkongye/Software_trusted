import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import VulnerabilityPage from '../views/VulnerabilityPage.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/vulnerabilities',
    name: 'Vulnerabilities',
    component: VulnerabilityPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router 