<template>
    <div class="toggle-switch" @click="toggle">
      <div class="switch-container" :class="{ 'on': isOn }">
        <span class="label on-label">On</span>
        <div class="slider"></div>
        <span class="label off-label">Off</span>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      modelValue: {
        type: Boolean,
        default: false,
      },
    },
    emits: ['update:modelValue'],
    data() {
      return {
        isOnInternal: this.modelValue,
      };
    },
    computed: {
      isOn: {
        get() {
          return this.isOnInternal;
        },
        set(newValue) {
          this.isOnInternal = newValue;
          this.$emit('update:modelValue', newValue);
        },
      },
    },
    methods: {
      toggle() {
        this.isOn = !this.isOn;
      },
    },
  };
  </script>
  
  <style scoped>
  .toggle-switch {
    display: inline-block;
    cursor: pointer;
  }
  
  .switch-container {
    position: relative;
    width: 60px; /* Adjust as needed */
    height: 30px; /* Adjust as needed */
    background-color: #ccc;
    border-radius: 15px;
    overflow: hidden;
    transition: background-color 0.3s ease;
  }
  
  .switch-container.on {
    background-color: #4CAF50; /* Green for "On" */
  }
  
  .label {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    color: #fff;
    font-size: 0.8em;
    font-weight: bold;
    user-select: none;
  }
  
  .on-label {
    left: 10px;
  }
  
  .off-label {
    right: 10px;
  }
  
  .slider {
    position: absolute;
    top: 2px;
    left: 2px;
    width: 26px; /* Adjust to be slightly smaller than height */
    height: 26px; /* Adjust as needed */
    background-color: #fff;
    border-radius: 50%;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    transition: transform 0.3s ease;
  }
  
  .switch-container.on .slider {
    transform: translateX(30px); /* Move to the right (width - slider width - 4px padding) */
  }
  </style>