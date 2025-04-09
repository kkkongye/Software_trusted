<template>
  <div class="identifier-page">
    <SoftwareIdentifier />
  </div>
</template>

<script setup>
import SoftwareIdentifier from '../components/SoftwareIdentifier.vue';
</script>

<style scoped>
.identifier-page {
  position: relative;
  width: 100%;
  height: calc(100vh - 60px); /* 减去分页栏的高度 */
  padding: 0;
  margin: 0;
  overflow: hidden;
}
</style> 