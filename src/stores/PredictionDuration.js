// src/stores/PredictionDuration.js
import { defineStore } from 'pinia';

export const usePredictionDurationStore = defineStore('predictionDuration', {
  state: () => ({
    duration: 30, // 默认值
  }),
  actions: {
    setDuration(newDuration) {
      this.duration = newDuration;
    },
  },
});
