<template>
    <span class="test-tube">
        <svg width="75px" height="112.5px" viewBox="370 160 390 800" class="icon"  version="1.1" xmlns="http://www.w3.org/2000/svg">
        
        <path d="M373.2 600.3h278.7v8H373.2z" fill="#999999" />
        <path d="M512.6 950.3h-9.8c-58.7 0 -106.7-48 -106.7-106v-55h255v50c0 78.4 -64.2 106.7 -142.5 106.7z" fill="blue" />
        <path d="M511.7 958.8c-40.7 0-79-15.9-108-44.9s-44.9-67.3-44.9-108V209.2h-32.2c-11.4 0-20.7-9.3-20.7-20.7v-17.6c0-11.4 9.3-20.7 20.7-20.7h370.1c11.4 0 20.7 9.3 20.7 20.7v17.6c0 11.4-9.3 20.7-20.7 20.7h-32.2v596.7c0 40.7-15.9 79-44.9 108-28.9 28.9-67.2 44.9-107.9 44.9zM326.6 165.1c-3.2 0-5.7 2.6-5.7 5.7v17.6c0 3.2 2.6 5.7 5.7 5.7h47.2v611.7c0 36.7 14.4 71.3 40.5 97.4 26.1 26.1 60.7 40.5 97.4 40.5s71.3-14.4 97.4-40.5c26.1-26.1 40.5-60.7 40.5-97.4V194.2h47.2c3.2 0 5.7-2.6 5.7-5.7v-17.6c0-3.2-2.6-5.7-5.7-5.7l-370.2-0.1z" fill="#999999" />
        <path d="M373.2 193.8h50.7v8h-50.7zM466.8 193.8h185.1v8H466.8z" fill="#999999" />
        <rect x="375" :y="500" :width="275" :height="300" fill="white" /> 
        <rect :x="blueRectX" :y="blueRectY" :width="blueRectWidth" :height="blueRectHeight" fill="blue" />
        <line x1="550" y1="256.75" x2="660" y2="256.75" stroke="#999999" stroke-width="14" />
        <line x1="590" y1="391" x2="660" y2="391" stroke="#999999" stroke-width="14" />
        <line x1="550" y1="536.75" x2="660" y2="536.75" stroke="#999999" stroke-width="14" />  
        <line x1="590" y1="681" x2="660" y2="681" stroke="#999999" stroke-width="14" /> 
        <line x1="550" y1="825" x2="660" y2="825" stroke="#999999" stroke-width="14" /> 
           
        </svg>
        <p class="a">{{ title }}</p>
    </span>
</template>


<script>
export default {
    props: {
        currentSoilMoisture: {
            type: Number,
            required: true,
            default: 75
        },
        title: {
            type: String,
            required: true,
        }
    },
    computed: {
        blueRectX() {
            return 396; // Approximate left x of the straight section (should be 396)
        },
        blueRectWidth() {
            return 254; // Approximate width of the straight section
        },
        blueRectBaseY() {
            return 825; // Approximate y at the bottom of the straight section
        },
        blueRectMaxY() {
            return 250; // Approximate y at the top of the straight section
        },
        blueRectHeight() {
            const moistureRatio = this.currentSoilMoisture / 100;
            const maxHeight = this.blueRectBaseY - this.blueRectMaxY;
            return moistureRatio * maxHeight;
        },
        blueRectY() {
            return this.blueRectBaseY - this.blueRectHeight;
        },
        liquidTopLineY() {
            return this.blueRectY - 5; // Position the line 5 units above the rectangle
        }
    }
}
</script>

<style scoped>
.test-tube {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.a {
  text-decoration: none;
  padding: 0.3rem 0.5rem;
  font: inherit;
  font-size: 0.6rem; /* Adjust this value to make text smaller/larger */
  font-weight: bold;  /* Makes the text bold */
  color: #74ad7d;
  cursor: pointer;
  border-radius: 30px;
  margin-right: 0.5rem;
  display: flex; /* Change to flex */
  align-items: center; /* Vertically center the content */
  justify-content: center; /* Optionally, horizontally center as well */
  margin-top: 0.5rem;    /* Added space ABOVE the element */
  margin-bottom: 0.5rem; /* Added space BELOW the element */
}
</style>