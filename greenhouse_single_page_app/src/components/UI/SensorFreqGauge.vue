<template>
  <div class="ping-indicator">
    <div class="segment segment-red"></div>
    <div class="segment segment-orange"></div>
    <div class="segment segment-green"></div>
    <div
      class="ping-marker"
      :style="{
        left: visualPingPercentage === 100
          ? `calc(100% - ${markerThickness}px)`
          : visualPingPercentage + '%'
      }"
    ></div>
  </div>
</template>

<script>
export default {
  name: 'SensorFreqGauge',
  props: {
    successfulPings: {
      type: Number,
      required: true,
    },
    totalExpectedPings: {
      type: Number,
      required: true,
    },
  },
  computed: {
    visualPingPercentage() {
      const pulled = Number(this.successfulPings);
      const expected = Number(this.totalExpectedPings);

      if (expected === 0) {
        return 0;
      }

      const rawPercentage = (pulled / expected) * 100;
      let visualPercentage;

      if (rawPercentage <= 75) {
        visualPercentage = 0;
      } else {
        visualPercentage = ((rawPercentage - 75) / 25) * 100;
      }

      return visualPercentage;
    },
    markerThickness() {
      return 5; // Or 3, depending on your CSS
    },
  },
};
</script>

<style scoped>
.ping-indicator {
  position: relative;
  display: flex;
  width: 300px; /* Adjust as needed */
  height: 30px;  /* Adjust as needed */
  border: 0px solid #ccc;
  overflow: hidden;
}

.segment {
  height: 100%;
  flex-shrink: 0;
  position: absolute;
}

.segment-red {
  background-color: red;
  left: 0;
  width: calc((85 - 75) / 25 * 100%); /* Represents the 75-85% actual range */
}

.segment-orange {
  background-color: orange;
  left: calc((85 - 75) / 25 * 100%); /* Starts after red */
  width: calc((95 - 85) / 25 * 100%); /* Represents the 85-95% actual range */
}

.segment-green {
  background-color: green;
  left: calc((85 - 75) / 25 * 100% + (95 - 85) / 25 * 100%); /* Starts after red + orange */
  width: calc((100 - 95) / 25 * 100%); /* Represents the 95-100% actual range */
}

.ping-marker {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 5px; /* Or 3px */
  background-color: black;
  z-index: 10;
}
</style>