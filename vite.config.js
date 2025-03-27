import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import { resolve } from 'path';

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src')
    }
  },
  server: {
    proxy: {
      '/api': {
        target: 'https://www.hdvis.net:8001',
        changeOrigin: true,
        secure: false, // 如果后端使用自签名证书，可以设置为false
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  }
});
