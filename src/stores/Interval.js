import { defineStore } from 'pinia';

export const useIntervalStore = defineStore('interval', {
  state: () => ({
    startDate: '',
    endDate: '',
  }),
  actions: {
    setInterval({ startDate, endDate }) {
      this.startDate = startDate;
      this.endDate = endDate;
    },
  },
});
