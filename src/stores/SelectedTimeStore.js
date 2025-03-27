// src/stores/SelectedTimeStore.js
import { defineStore } from 'pinia';

export const useSelectedTimeStore = defineStore('selectedTime', {
  state: () => ({
    selectedTime: null, // 默认没有选中的时间
  }),
  actions: {
    setSelectedTime(time) {
      this.selectedTime = time; // 更新 selectedTime
    },
  },
});
