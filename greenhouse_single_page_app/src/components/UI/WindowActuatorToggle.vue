<template>
    <div class="three-position-toggle" @click="cyclePosition">
      <div
        class="switch-container"
        :class="currentPositionClass"
        :style="{
          height: containerHeight + 'px',
          borderRadius: containerHeight / 2 + 'px'
        }"
      >
        <span class="label closed-label">Closed</span>
        <div class="slider" :style="simplifiedSliderStyle"></div>
        <span class="label half-label">Half</span>
        <span class="label open-label">Open</span>
      </div>
    </div>
  </template>

<script>
export default {
  props: {
    modelValue: {
      type: String,
      default: 'closed',
      validator: (value) => ['closed', 'half', 'open'].includes(value),
    },
  },
  emits: ['update:modelValue'],
  data() {
    return {
      positions: ['closed', 'half', 'open'],
      containerHeight: 30,
      sliderHeight: 26,
      labelFontSize: '0.8em',
    };
  },
  watch: {
    windowPosition(newValue, oldValue) {
      console.log('windowPosition changed:', oldValue, '=>', newValue);
    },
  },
  computed: {
    currentIndex() {
      const initialIndex = this.positions.indexOf(this.modelValue);
      return initialIndex !== -1 ? initialIndex : 0;
    },
    currentPositionClass() {
      return `position-${this.positions[this.currentIndex]}`;
    },
    simplifiedSliderStyle() {
      const containerWidth = 180;
      const sliderWidth = this.sliderHeight;
      const baseOffset = 2;
      const step = (containerWidth - sliderWidth - 2 * baseOffset) / (this.positions.length - 1);
      const translateX = baseOffset + this.currentIndex * step;
      return {
        transform: `translateX(${translateX}px)`,
        width: `${sliderWidth}px`,
        height: `${this.sliderHeight}px`,
        borderRadius: `${this.sliderHeight / 2}px`,
      };
    },
  },
  methods: {
  cyclePosition() {
    console.log('cyclePosition called!'); // Add this line
    const nextIndex = (this.positions.indexOf(this.modelValue) + 1) % this.positions.length;
    this.$emit('update:modelValue', this.positions[nextIndex]);
  },
},
};
</script>

<style scoped>
.three-position-toggle {
  display: inline-block;
  cursor: pointer;
}

.switch-container {
  position: relative;
  width: 180px; /* Increased width */
  height: 30px; /* Set fixed height to match ActuatorToggle */
  background-color: #ccc;
  border-radius: 15px; /* Match ActuatorToggle's border-radius (half of height) */
  overflow: hidden;
  transition: background-color 0.3s ease;
}

.position-closed {
  background-color: #f44336; /* Red for "Closed" */
}

.position-half {
  background-color: #800080; /* Purple for "Half" */
}

.position-open {
  background-color: #2196f3; /* Blue for "Open" */
}

.label {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  color: #fff;
  font-size: v-bind(labelFontSize); /* Use data for font size */
  font-weight: bold;
  user-select: none;
  white-space: nowrap;
}

.closed-label {
  left: 10px;
}

.half-label {
  left: 50%;
  transform: translate(-50%, -50%);
}

.open-label {
  right: 10px;
}

.slider {
  position: absolute;
  top: 2px; /* Adjust top to maintain visual consistency */
  left: 2px; /* Adjust left to maintain visual consistency */
  width: 26px; /* Match ActuatorToggle's slider width */
  height: 26px; /* Match ActuatorToggle's slider height */
  background-color: rgba(255, 165, 0, 0.6); /* Semi-opaque orange: R, G, B, Alpha */
  border-radius: 50%; /* Make it a circle */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s ease;
}
</style>