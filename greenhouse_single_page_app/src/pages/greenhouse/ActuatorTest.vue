<template>
  <div>
    <base-card>
      <h3>
        <base-button><act-icon iconwidth="20" class="icon"></act-icon> Actuator Test Kit</base-button>
      </h3>
    </base-card>

    <base-card>
    <base-button><act-icon iconwidth="20" class="icon"></act-icon> Roof Sash Test</base-button><br>
    <div class="eight-grid-container">
      <div class="eight-grid-item-window-description">Roof Sash 1</div>
      <div class="eight-grid-item-window-toggle"><window-actuator-toggle v-model="roof1Position"></window-actuator-toggle></div>
      <div class="eight-grid-item-window-description">Roof Sash 2</div>
      <div class="eight-grid-item-window-toggle"><window-actuator-toggle v-model="roof2Position"></window-actuator-toggle></div>
      <div class="eight-grid-item-window-description">Roof Sash 3</div>
      <div class="eight-grid-item-window-toggle"><window-actuator-toggle v-model="roof3Position"></window-actuator-toggle></div>
      <div class="eight-grid-item-window-description">Roof Sash 4</div>
      <div class="eight-grid-item-window-toggle"><window-actuator-toggle v-model="roof4Position"></window-actuator-toggle></div>
      <div class="eight-grid-item-window-description">Roof Sash 5</div>
      <div class="eight-grid-item-window-toggle"><window-actuator-toggle v-model="roof5Position"></window-actuator-toggle></div>
      <div class="eight-grid-item-window-description">Roof Sash 6</div>
      <div class="eight-grid-item-window-toggle"><window-actuator-toggle v-model="roof6Position"></window-actuator-toggle></div>
      <div class="eight-grid-item-window-description">Roof Sash 7</div>
      <div class="eight-grid-item-window-toggle"><window-actuator-toggle v-model="roof7Position"></window-actuator-toggle></div>
      <div class="eight-grid-item-window-description">Roof Sash 8</div>
      <div class="eight-grid-item-window-toggle"><window-actuator-toggle v-model="roof8Position"></window-actuator-toggle></div>
    </div>  
    </base-card>

    <base-card>
    <base-button><act-icon iconwidth="20" class="icon"></act-icon> Louvre Test</base-button><br>
    <div class="eight-grid-container">
      <div class="eight-grid-item-window-description">Louvre 1</div>
      <div class="eight-grid-item-window-toggle"><window-actuator-toggle v-model="louvre1Position"></window-actuator-toggle></div>
      <div class="eight-grid-item-window-description">Louvre 2</div>
      <div class="eight-grid-item-window-toggle"><window-actuator-toggle v-model="louvre2Position"></window-actuator-toggle></div>
      <div class="eight-grid-item-window-description">Louvre 3</div>
      <div class="eight-grid-item-window-toggle"><window-actuator-toggle v-model="louvre3Position"></window-actuator-toggle></div>
      <div class="eight-grid-item-window-description">Louvre 4</div>
      <div class="eight-grid-item-window-toggle"><window-actuator-toggle v-model="louvre4Position"></window-actuator-toggle></div>
      <div class="eight-grid-item-window-description">Louvre 5</div>
      <div class="eight-grid-item-window-toggle"><window-actuator-toggle v-model="louvre5Position"></window-actuator-toggle></div>
      <div class="eight-grid-item-window-description">Louvre 6</div>
      <div class="eight-grid-item-window-toggle"><window-actuator-toggle v-model="louvre6Position"></window-actuator-toggle></div>
      <div class="eight-grid-item-window-description">Louvre 7</div>
      <div class="eight-grid-item-window-toggle"><window-actuator-toggle v-model="louvre7Position"></window-actuator-toggle></div>
      <div class="eight-grid-item-window-description">Louvre 8</div>
      <div class="eight-grid-item-window-toggle"><window-actuator-toggle v-model="louvre8Position"></window-actuator-toggle></div>
    </div>  
    </base-card>

    <base-card>
    <base-button><act-icon iconwidth="20" class="icon"></act-icon> Watering Beds</base-button><br>
    <div class="eight-grid-container">
      <div class="eight-grid-item">Watering Bed 1</div>
      <div class="eight-grid-item"><actuator-toggle></actuator-toggle></div>
      <div class="eight-grid-item">Watering Bed 2</div>
      <div class="eight-grid-item"><actuator-toggle></actuator-toggle></div>
      <div class="eight-grid-item">Watering Bed 3</div>
      <div class="eight-grid-item"><actuator-toggle></actuator-toggle></div>
      <div class="eight-grid-item">Watering Bed 4</div>
      <div class="eight-grid-item"><actuator-toggle></actuator-toggle></div>
      <div class="eight-grid-item">Watering Bed 5</div>
      <div class="eight-grid-item"><actuator-toggle></actuator-toggle></div>
      <div class="eight-grid-item">Watering Bed 6</div>
      <div class="eight-grid-item"><actuator-toggle></actuator-toggle></div>
      <div class="eight-grid-item">Watering Bed 7</div>
      <div class="eight-grid-item"><actuator-toggle></actuator-toggle></div>
      <div class="eight-grid-item">Watering Bed 8</div>
      <div class="eight-grid-item"><actuator-toggle></actuator-toggle></div>
    </div>  
    </base-card>

    <base-card>
    <base-button><act-icon iconwidth="20" class="icon"></act-icon> Heating Circuits</base-button><br>
    <div class="two-grid-container">
      <div class="two-grid-item">Heating Circuit CZ1</div>
      <div class="two-grid-item"><actuator-toggle></actuator-toggle></div>
      <div class="two-grid-item">Heating Circuit CZ2</div>
      <div class="two-grid-item"><actuator-toggle></actuator-toggle></div>
    </div>  
    </base-card>

    <base-card>
    <base-button><act-icon iconwidth="20" class="icon"></act-icon> Water Misters</base-button><br>
    <div class="two-grid-container">
      <div class="two-grid-item">Water Mister CZ1</div>
      <div class="two-grid-item"><actuator-toggle></actuator-toggle></div>
      <div class="two-grid-item">Water Mister CZ2</div>
      <div class="two-grid-item"><actuator-toggle></actuator-toggle></div>
    </div>  
    </base-card>
  </div>
</template>

<script>
import ActuatorToggle from '@/components/UI/ActuatorToggle.vue';
import WindowActuatorToggle from '@/components/UI/WindowActuatorToggle.vue';

export default {
  components: {
    ActuatorToggle,
    WindowActuatorToggle
  },
  data() {
    return {
      louvre1Position: 'closed',
      louvre2Position: 'closed',
      louvre3Position: 'closed',
      louvre4Position: 'closed',
      louvre5Position: 'closed',
      louvre6Position: 'closed',
      louvre7Position: 'closed',
      louvre8Position: 'closed',
      roof1Position: 'closed',
      roof2Position: 'closed',
      roof3Position: 'closed',
      roof4Position: 'closed',
      roof5Position: 'closed',
      roof6Position: 'closed',
      roof7Position: 'closed',
      roof8Position: 'closed',
    };
  },
  watch: {
    louvre1Position(newValue, oldValue) {
      console.log('louvre1Position changed:', oldValue, '=>', newValue);
    },
    louvre2Position(newValue, oldValue) {
      console.log('louvre2Position changed:', oldValue, '=>', newValue);
    },
    louvre3Position(newValue, oldValue) {
      console.log('louvre3Position changed:', oldValue, '=>', newValue);
    },
    louvre4Position(newValue, oldValue) {
      console.log('louvre4Position changed:', oldValue, '=>', newValue);
    },
    louvre5Position(newValue, oldValue) {
      console.log('louvre5Position changed:', oldValue, '=>', newValue);
    },
    louvre6Position(newValue, oldValue) {
      console.log('louvre6Position changed:', oldValue, '=>', newValue);
    },
    louvre7Position(newValue, oldValue) {
      console.log('louvre7Position changed:', oldValue, '=>', newValue);
    },
    louvre8Position(newValue, oldValue) {
      console.log('louvre8Position changed:', oldValue, '=>', newValue);
    },
  },
};
</script>

<style scoped>
.icon {
  margin-right: 10px;
}

.container {
  display: flex; /* Enable Flexbox */
  align-items: center; /* Vertically center items */
  justify-content: center; /* Horizontally center items */
  margin-top: 15px;
  margin-bottom: 15px; /* Add some spacing between the circuit sections */
  gap: 10px; /* Add spacing between the title and buttons, and between the buttons */
}

.two-grid-container {
  display: flex;
  flex-wrap: wrap;
  width: 100%; /* Adjust as needed */
  height: 100px; /* Adjust as needed */
  border: 1px solid black; /* For visualization */
  border-radius: 15px;
  border-color: rgb(221, 219, 219);
}

.two-grid-item {
  width: 50%;
  height: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.eight-grid-container {
  display: flex;
  flex-wrap: wrap;
  width: 100%; /* Adjust as needed */
  height: 400px; /* Adjust as needed */
  border: 1px solid black; /* For visualization */
  border-radius: 15px;
  border-color: rgb(221, 219, 219)
}

.eight-grid-item {
  width: 50%;
  height: 12.5%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.eight-grid-item-window-description {
  width: 40%;
  height: 12.5%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.eight-grid-item-window-toggle {
  width: 60%;
  height: 12.5%;
  display: flex;
  justify-content: center;
  align-items: center;
}

</style>