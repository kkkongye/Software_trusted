<template>
  <div>
    <div class="identifier-page">
      <SoftwareIdentifier class="full-page-identifier" />
    </div>
  </div>
</template>

<script setup>
import SoftwareIdentifier from '../components/SoftwareIdentifier.vue';
</script>

<style scoped>
.identifier-page {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  height: calc(100vh - 60px);
  background-color: #f0f0f0;
  width: 100%;
  box-sizing: border-box;
}

.full-page-identifier {
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
}
</style> 