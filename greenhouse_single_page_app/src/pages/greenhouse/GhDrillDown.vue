<template>
  <div>
    <base-card>
      <h3>
        <base-button>
          <to-do-icon iconwidth="25" class="icon"></to-do-icon>
          Drill Down on {{ dataLabel }}
        </base-button>
      </h3>
    </base-card>

    <base-card>
      <h4>Last 24 Hours</h4>
      <div class="chart-container hourly-chart-container">
        <canvas ref="hourlyChartCanvas"></canvas>
      </div>
    </base-card>

    <base-card>
      <h4>Past 7 Days (Hourly Data)</h4>
       <div class="chart-container weekly-chart-container">
            <canvas ref="weeklyChartCanvas"></canvas>
       </div>
    </base-card>

  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js';
// *** Make sure you have run: npm install chartjs-adapter-date-fns date-fns ***
import 'chartjs-adapter-date-fns';
// ***************************************************************************
Chart.register(...registerables);

// Import base components if they are not globally registered
import BaseCard from '@/components/UI/BaseCard.vue';
import BaseButton from '@/components/UI/BaseButton.vue';
import ToDoIcon from '@/components/UI/icons/ToDoIcon.vue'; // Adjust path if necessary


export default {
  components: {
      BaseCard,
      BaseButton,
      ToDoIcon
      // Register other components used in the template if needed
  },
  props: {
    dataLabel: { // Keep prop even if not used for data fetching *yet*
      type: String,
      required: true,
    }
  },
  data() {
    return {
      // Chart instances
      hourlyChartInstance: null,
      weeklyChartInstance: null,
      // Sample data storage
      hourlySampleData: [],
      weeklyHourlySampleData: [],
    };
  },
  computed: {
    // Formatter for the hourly chart data (uses explicit labels)
    formattedHourlyChartData() {
      if (!this.hourlySampleData || this.hourlySampleData.length === 0) {
        return { labels: [], datasets: [{ label: 'Temperature (°C)', data: [] }] };
      }
      const labels = this.hourlySampleData.map(item => item.timeLabel);
      const dataPoints = this.hourlySampleData.map(item => item.value);
      return {
        labels: labels, // X-axis labels (e.g., "14:00")
        datasets: [
          {
            label: 'Temperature (°C)',
            data: dataPoints, // Y-axis values
            borderColor: '#74ad7d',
            backgroundColor: 'rgba(116, 173, 125, 0.2)',
            tension: 0.1,
            fill: true,
            // --- Styling for 'x' markers (defined per dataset) ---
            pointStyle: 'crossRot',
            pointRadius: 6,
            pointBorderWidth: 2,
            pointBackgroundColor: 'rgba(0,0,0,0.5)',
            // ----------------------------------------------------
          }
        ]
      };
    },

    // Formatter for the weekly chart using HOURLY data points ({x, y})
    formattedWeeklyChartData() {
       if (!this.weeklyHourlySampleData || this.weeklyHourlySampleData.length === 0) {
         return { datasets: [{ label: 'Temperature (°C)', data: [] }] };
       }
       return {
         // No separate labels array needed when using {x,y} format for time scale
         datasets: [
          {
            label: 'Temperature (°C)', // Dataset label
            data: this.weeklyHourlySampleData.map(item => ({
                x: new Date(item.timestamp), // Use Date object or timestamp for x
                y: item.value                // The temperature value for y
            })),
            borderColor: '#36A2EB',
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            tension: 0.1, // Smoothes the line slightly
            fill: true,
            // Point radius 0 to hide points is set in the chart options below
          }
        ]
      };
    }
  },
  methods: {
    // Generates 24h of hourly data
    generateHourlySampleData() {
      const data = [];
      const now = new Date(); // Current time
      const baseTemp = 15;
      const variation = 5;
      for (let i = 23; i >= 0; i--) {
        const timestamp = new Date(now.getTime() - i * 60 * 60 * 1000);
        const temp = baseTemp + (Math.random() - 0.5) * 2 * variation;
        data.push({
          timestamp: timestamp.toISOString(),
          value: parseFloat(temp.toFixed(1)),
          timeLabel: timestamp.toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit', hour12: false })
        });
      }
      this.hourlySampleData = data;
    },

    // Generates 7 days of HOURLY data
    generateWeeklyHourlySampleData() {
       const data = [];
       const now = new Date(); // Current time
       const hoursToGoBack = 7 * 24; // 168 hours
       const baseTemp = 14;
       const variation = 4;
       // Removed unused firstTimestamp and lastTimestamp declarations

       for (let i = hoursToGoBack - 1; i >= 0; i--) { // Loop through hours
         const timestamp = new Date(now.getTime() - i * 60 * 60 * 1000);
         // Removed assignments to unused firstTimestamp/lastTimestamp
         const temp = baseTemp + (Math.random() - 0.5) * 2 * variation;
         data.push({
           timestamp: timestamp.toISOString(), // Store full timestamp
           value: parseFloat(temp.toFixed(1)),
         });
       }
       this.weeklyHourlySampleData = data;
    },

    // Render hourly chart
    renderHourlyChart() {
      if (!this.$refs.hourlyChartCanvas) return;
      const ctx = this.$refs.hourlyChartCanvas.getContext('2d');
      if (this.hourlyChartInstance) this.hourlyChartInstance.destroy();
      if (!this.hourlySampleData || this.hourlySampleData.length === 0) return;

      const formattedData = this.formattedHourlyChartData;
      if (!formattedData || !formattedData.datasets || !formattedData.datasets[0] || !formattedData.datasets[0].data || formattedData.datasets[0].data.length === 0) {
           console.error("Formatted hourly data is invalid or empty!");
           return;
      }

      try {
          this.hourlyChartInstance = new Chart(ctx, {
            type: 'line',
            data: formattedData, // Use the local variable fixed the ReferenceError
            options: {
              responsive: true,
              maintainAspectRatio: false,
              scales: {
                x: { title: { display: true, text: 'Time (Last 24h)' } },
                y: { beginAtZero: false, title: { display: true, text: 'Temperature (°C)' } },
              },
              plugins: {
                legend: { display: false },
                title: { display: true, text: 'Hourly Temperature (°C)' },
                tooltip: { enabled: true }
              }
            }
          });
      } catch (error) {
           console.error("Error creating hourly chart:", error);
      }
    },

    // Render weekly chart with HOURLY data points and time scale
    renderWeeklyChart() {
        if (!this.$refs.weeklyChartCanvas) return;
        // Corrected: getContext from the specific ref
        const ctx = this.$refs.weeklyChartCanvas.getContext('2d');
        if (this.weeklyChartInstance) this.weeklyChartInstance.destroy();
        if (!this.weeklyHourlySampleData || this.weeklyHourlySampleData.length === 0) return;

        // *** Determine min/max timestamps from the actual data ***
        // Convert ISO strings back to time values for comparison
        const timestamps = this.weeklyHourlySampleData.map(d => new Date(d.timestamp).getTime());
        // Add checks in case timestamps array is empty
        const minTimestamp = timestamps.length ? Math.min(...timestamps) : null;
        const maxTimestamp = timestamps.length ? Math.max(...timestamps) : null;
        // *********************************************************

        const formattedData = this.formattedWeeklyChartData;
        if (!formattedData || !formattedData.datasets || !formattedData.datasets[0] || !formattedData.datasets[0].data || formattedData.datasets[0].data.length === 0) {
           console.error("Formatted weekly data is invalid or empty!");
           return;
        }

        // Only proceed if min/max calculation was successful
        if (minTimestamp === null || maxTimestamp === null) {
            console.error("Could not determine min/max timestamps for weekly chart.");
            return;
        }

        try {
            this.weeklyChartInstance = new Chart(ctx, {
                type: 'line',
                data: formattedData, // Uses the {x, y} data structure
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                     scales: {
                         y: {
                             beginAtZero: false,
                             title: { display: true, text: 'Temperature (°C)'}
                         },
                         x: {
                             type: 'time', // *** Enable time scale ***
                             title: { display: true, text: 'Date / Time'},
                             time: {
                                 unit: 'day', // Display labels primarily by day
                                 tooltipFormat: 'PPp', // Format for tooltips (e.g., Apr 13, 2025, 3:00 PM)
                             },
                             ticks: {
                                 source: 'auto',
                                 maxRotation: 45,
                                 minRotation: 45
                             },
                             // *** Explicitly set min/max for the axis ***
                             min: minTimestamp,
                             max: maxTimestamp
                             // ******************************************
                         }
                    },
                     plugins: {
                        legend: { display: false },
                        title: { display: true, text: 'Weekly Temperature Trend (°C)'},
                        tooltip: { enabled: true }
                     },
                     elements: {
                         point:{
                             radius: 0 // *** Hide points on this chart ***
                         }
                     },
                     parsing: false, // Optimization
                     normalized: true, // Optimization
                }
            });
        } catch(error) {
             console.error("Error creating weekly chart:", error);
        }
    }
  },
  created() {
    // Generate both datasets immediately
    this.generateHourlySampleData();
    this.generateWeeklyHourlySampleData();
  },
  mounted() {
    // Render charts after component is mounted
    // Using nextTick ensures DOM elements (canvas) are definitely ready
    this.$nextTick(() => {
        this.renderHourlyChart();
        this.renderWeeklyChart();
    });
  },
  beforeUnmount() {
    // Clean up both chart instances
    if (this.hourlyChartInstance) this.hourlyChartInstance.destroy();
    if (this.weeklyChartInstance) this.weeklyChartInstance.destroy();
  },
}
</script>

<style scoped>
.icon {
  margin-right: 10px;
}

/* Style the container div to control chart size */
.chart-container {
  position: relative; /* Needed for responsive chart sizing */
  width: 350px;
  height: 200px;
  margin: 20px auto; /* Add vertical margin between elements/cards */
}

/* Canvas itself should fill the container */
canvas {
  display: block; /* Prevents extra space below canvas */
  width: 100%;
  height: 100%;
}
</style>