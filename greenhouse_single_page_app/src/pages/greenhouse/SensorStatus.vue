<template>
    <div>
      <base-card>
        <h3>
          <base-button><sensor-icon iconwidth="20" class="icon"></sensor-icon>Sensor Health Check</base-button>
        </h3>
        <base-card>
          <p>
            We have 10 sensors attached to two Raspberry pi's in the greenhouse detecting 14 variables. Climate zone 1 has 3 soil moisture sensors, CO², relative humidity and air temperature sensors.
          </p>
          <br />
          <p>Climate zone 2 has 5 soil moisture sensors, CO², relative humidity and air temperature.</p>
          <br />
          <p>One additional sensor is attached directly to the controller pi in the boiler room which senses barometric pressure.</p>
        </base-card>
      </base-card>
      <base-card>
        <h3>Sensor Data Pull Frequency</h3>
        <div v-for="sensor in sensors" :key="sensor.id" class="sensor-item">
          <p>{{ sensor.title }}</p>
          <sensor-freq-gauge
            :successful-pings="sensor.dataPulled"
            :total-expected-pings="sensor.dataExpected"
          >
        </sensor-freq-gauge>
          <p>{{ calculateDataPullPercentage(sensor.dataPulled, sensor.dataExpected) }}% data received</p>
        </div>
      </base-card>
    </div>
  </template>
  
  <script>
  import SensorFreqGauge from '@/components/UI/SensorFreqGauge.vue';

  
  export default {
    components: { SensorFreqGauge }, // Register the PingIndicator
    data() {
      return {
        sensors: [
          {
            id: 'soil-moisture-1',
            title: 'Soil Moisture - Bed 1',
            dataPulled: 2160, // Example values
            dataExpected: 2880,
            currentValue: null,
            expectedRange: { min: 10, max: 90 },
            inRange: true,
          },
          {
            id: 'soil-moisture-2',
            title: 'Soil Moisture - Bed 2',
            dataPulled: 2736, // Example values
            dataExpected: 2880,
            currentValue: null,
            expectedRange: { min: 10, max: 90 },
            inRange: true,
          },
          {
            id: 'soil-moisture-3',
            title: 'Soil Moisture - Bed 3',
            dataPulled: 2800, // Example values
            dataExpected: 2880,
            currentValue: null,
            expectedRange: { min: 10, max: 90 },
            inRange: true,
          },
          {
            id: 'soil-moisture-4',
            title: 'Soil Moisture - Bed 4',
            dataPulled: 2592, // Example values
            dataExpected: 2880,
            currentValue: null,
            expectedRange: { min: 10, max: 90 },
            inRange: true,
          },
          {
            id: 'soil-moisture-5',
            title: 'Soil Moisture - Bed 5',
            dataPulled: 2016, // Example values
            dataExpected: 2880,
            currentValue: null,
            expectedRange: { min: 10, max: 90 },
            inRange: true,
          },
          {
            id: 'soil-moisture-6',
            title: 'Soil Moisture - Bed 6',
            dataPulled: 2784, // Example values
            dataExpected: 2880,
            currentValue: null,
            expectedRange: { min: 10, max: 90 },
            inRange: true,
          },
          {
            id: 'soil-moisture-7',
            title: 'Soil Moisture - Bed 7',
            dataPulled: 2880, // Example values
            dataExpected: 2880,
            currentValue: null,
            expectedRange: { min: 10, max: 90 },
            inRange: true,
          },
          {
            id: 'soil-moisture-8',
            title: 'Soil Moisture - Bed 8',
            dataPulled: 2669, // Example values
            dataExpected: 2880,
            currentValue: null,
            expectedRange: { min: 10, max: 90 },
            inRange: true,
          },
          {
            id: 'relative-humidity-1',
            title: 'Relative Humidity Sensor 1',
            dataPulled: 2851, // Example values
            dataExpected: 2880,
            currentValue: null,
            expectedRange: { min: 30, max: 90 },
            inRange: true,
          },
          {
            id: 'relative-humidity-2',
            title: 'Relative Humidity Sensor 2',
            dataPulled: 2707, // Example values
            dataExpected: 2880,
            currentValue: null,
            expectedRange: { min: 35, max: 85 },
            inRange: true,
          },
          {
            id: 'co2-sensor-1',
            title: 'CO₂ Sensor 1',
            dataPulled: 2534, // Example values
            dataExpected: 2880,
            currentValue: null,
            expectedRange: { min: 400, max: 1000 },
            inRange: true,
          },
          {
            id: 'co2-sensor-2',
            title: 'CO₂ Sensor 2',
            dataPulled: 2880, // Example values
            dataExpected: 2880,
            currentValue: null,
            expectedRange: { min: 400, max: 950 },
            inRange: true,
          },
          {
            id: 'temperature-sensor-1',
            title: 'Temperature Sensor 1',
            dataPulled: 2693, // Example values
            dataExpected: 2880,
            currentValue: null,
            expectedRange: { min: 1, max: 40 },
            inRange: true,
          },
          {
            id: 'temperature-sensor-2',
            title: 'Temperature Sensor 2',
            dataPulled: 2880, // Example values
            dataExpected: 2880,
            currentValue: null,
            expectedRange: { min: 1, max: 40 },
            inRange: true,
          },
        ],
        dataPullThresholdPercentage: 90,
      };
    },
    methods: {
      calculateDataPullPercentage(pulled, expected) {
        if (expected === 0) {
          return 0;
        }
        return Math.round((pulled / expected) * 100);
      },
    },
  };
  </script>
  
  <style scoped>
  .icon {
    margin-right: 10px;
  }
  
  .sensor-item {
    margin-bottom: 20px;
  }
  
  .sensor-item p {
    margin-bottom: 5px;
  }
  </style>