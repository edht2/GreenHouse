<template>
    <button
      class="actuator-button"
      :class="colorClass"
      @mouseover="isHovered = true"
      @mouseleave="isHovered = false"
    >
      <slot></slot>
    </button>
  </template>
  
  <script>
  export default {
    props: {
      color: {
        type: String,
        validator: (value) => ['blue', 'red'].includes(value),
        default: 'blue',
      },
    },
    data() {
      return {
        isHovered: false,
      };
    },
    computed: {
      colorClass() {
        if (this.color === 'blue') {
          return this.isHovered ? 'blue-dark' : 'blue-light';
        } else if (this.color === 'red') {
          return this.isHovered ? 'red-dark' : 'red-light';
        }
        return 'blue-light'; // Default if prop is invalid
      },
    },
  };
  </script>
  
  <style scoped>
  .actuator-button {
    padding: 0.75rem 1.5rem;
    font: inherit;
    color: white;
    cursor: pointer;
    border: none;
    margin-right: 0.5rem;
    display: inline-block;
    padding: 8px 16px; /* Example padding */
    border-radius: 4px; /* Example border-radius */
    cursor: pointer;
    font-size: 1em;

  /* Add vertical and horizontal margins here */
  margin: 10px 5px; /* 10px vertical, 5px horizontal */
  }
  
  .blue-light {
    background-color: #2196f3; /* Light blue */
  }
  
  .blue-dark {
    background-color: #1976d2; /* Dark blue */
  }
  
  .red-light {
    background-color: #f44336; /* Light red */
  }
  
  .red-dark {
    background-color: #d32f2f; /* Dark red */
  }
  
  .actuator-button:focus {
    outline: none; /* Optional: remove default focus outline */
    box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.5); /* Optional: custom focus style */
  }
  </style>