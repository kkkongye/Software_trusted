<template>
    <div class="sbom-list">
      <h3>SBOM清单信息</h3>
      <pre>{{ sbomData }}</pre>
    </div>
</template>
  
  <script setup>
  import { ref } from 'vue';
  
  const sbomData = ref(`{
    "components": [
      { "name": "libraryA", "version": "1.0.0" },
      { "name": "libraryB", "version": "2.0.0" }
    ]
  }`);
  </script>
  
  <style scoped>
  .sbom-list {
    border: 1px solid #ccc;
    padding: 10px;
    margin: 10px;
    height: 100%; /* 占满父容器 */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 阴影效果 */
  }
  h3 {
  margin-top: 0;
  margin-bottom: 15px;
  text-align: center;
  font-size: 16px;
  color: #333;
  font-weight: bold;
}
  </style>