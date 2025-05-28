<template>
    <div>
      <base-card>
        <h4><base-button><gr-hs-icon iconwidth="15" class="icon"></gr-hs-icon>Greenhouse Zone 1 climate</base-button></h4>
        <div class="dials-container">
          <router-link :to="{name: 'drilldownDetail', params: {dataLabel:dataLabel[2]}}">
            <the-circular-dial
              :greenLowerLimit="zone1Limits['vpdLowerLimit']"
              :greenUpperLimit="zone1Limits['vpdUpperLimit']"
              :zoneDegrees="zoneDegrees"
              :currentCondition="zone1CurrentConditions['currentVPD']"
              :title="titles['VPD']"
            >
            </the-circular-dial>
          </router-link>
          <router-link :to="{name: 'drilldownDetail', params: {dataLabel:dataLabel[0]}}">
            <the-circular-dial
              :greenLowerLimit="zone1Limits['tempLowerLimit']"
              :greenUpperLimit="zone1Limits['tempUpperLimit']"
              :zoneDegrees="zoneDegrees"
              :currentCondition="zone1CurrentConditions['currentTemp']"
              :title="titles['temp']"
            >
            </the-circular-dial>
          </router-link>
          <router-link :to="{name: 'drilldownDetail', params: {dataLabel:dataLabel[1]}}">
            <the-circular-dial
              :greenLowerLimit="zone1Limits['co2LowerLimit']"
              :greenUpperLimit="zone1Limits['co2UpperLimit']"
              :zoneDegrees="zoneDegrees"
              :currentCondition="zone1CurrentConditions['currentCO2']"
              :title="titles['CO2']"
            >
            </the-circular-dial>
          </router-link>
        </div>
      </base-card>
      
      <base-card>
      <h4><base-button><gr-hs-icon iconwidth="15" class="icon"></gr-hs-icon>Soil Moisture Readings for Zone 1</base-button></h4>
      <div class="the-test-tube">
        <router-link :to="{name: 'drilldownDetail', params: {dataLabel:dataLabel[3]}}">
          <the-test-tube 
            :currentSoilMoisture="zone1CurrentConditions['currentSoilMoisture1']" 
            :title="titles['bed1']"
          >
          </the-test-tube>
        </router-link>
        <router-link :to="{name: 'drilldownDetail', params: {dataLabel:dataLabel[4]}}">
          <the-test-tube 
            :currentSoilMoisture="zone1CurrentConditions['currentSoilMoisture2']" 
            :title="titles['bed2']"
          >
          </the-test-tube>
        </router-link>
        <router-link :to="{name: 'drilldownDetail', params: {dataLabel:dataLabel[5]}}">
          <the-test-tube 
            :currentSoilMoisture="zone1CurrentConditions['currentSoilMoisture3']" 
            :title="titles['bed3']"
          >
          </the-test-tube>
        </router-link>
    </div>
      </base-card>
      <base-card>
        <h4><base-button><gr-hs-icon iconwidth="15" class="icon"></gr-hs-icon>Greenhouse Zone 2 climate</base-button></h4>
        <div class="dials-container">
          <router-link :to="{name: 'drilldownDetail', params: {dataLabel:dataLabel[8]}}">
            <the-circular-dial
              :greenLowerLimit="zone2Limits['vpdLowerLimit']"
              :greenUpperLimit="zone2Limits['vpdUpperLimit']"
              :zoneDegrees="zoneDegrees"
              :currentCondition="zone2CurrentConditions['currentVPD']"
              :title="titles['VPD']"
            >
            </the-circular-dial>
        </router-link>
        <router-link :to="{name: 'drilldownDetail', params: {dataLabel:dataLabel[6]}}">
            <the-circular-dial
              :greenLowerLimit="zone2Limits['tempLowerLimit']"
              :greenUpperLimit="zone2Limits['tempUpperLimit']"
              :zoneDegrees="zoneDegrees"
              :currentCondition="zone2CurrentConditions['currentTemp']"
              :title="titles['temp']"
            >
            </the-circular-dial>
        </router-link>
        <router-link :to="{name: 'drilldownDetail', params: {dataLabel:dataLabel[7]}}">
            <the-circular-dial
              :greenLowerLimit="zone2Limits['co2LowerLimit']"
              :greenUpperLimit="zone2Limits['co2UpperLimit']"
              :zoneDegrees="zoneDegrees"
              :currentCondition="zone2CurrentConditions['currentCO2']"
              :title="titles['CO2']"
            >
            </the-circular-dial>
        </router-link>
        </div>
      </base-card>
      
      <base-card>
      <h4><base-button><gr-hs-icon iconwidth="15" class="icon"></gr-hs-icon>Soil Moisture Readings for Zone 2</base-button></h4>
      <div class="the-test-tube">
      <router-link :to="{name: 'drilldownDetail', params: {dataLabel:dataLabel[9]}}"> 
        <the-test-tube 
          :currentSoilMoisture="zone2CurrentConditions['currentSoilMoisture1']" 
          :title="titles['bed4']"
        >
        </the-test-tube>
      </router-link>
      <router-link :to="{name: 'drilldownDetail', params: {dataLabel:dataLabel[10]}}"> 
        <the-test-tube 
          :currentSoilMoisture="zone2CurrentConditions['currentSoilMoisture2']" 
          :title="titles['bed5']"
        >
        </the-test-tube>
    </router-link>
    <router-link :to="{name: 'drilldownDetail', params: {dataLabel:dataLabel[11]}}"> 
        <the-test-tube 
          :currentSoilMoisture="zone2CurrentConditions['currentSoilMoisture3']" 
          :title="titles['bed6']"
        >
      </the-test-tube>
    </router-link>
    <router-link :to="{name: 'drilldownDetail', params: {dataLabel:dataLabel[12]}}">
        <the-test-tube 
          :currentSoilMoisture="zone2CurrentConditions['currentSoilMoisture4']" 
          :title="titles['bed7']"
        >
        </the-test-tube>
    </router-link>
    <router-link :to="{name: 'drilldownDetail', params: {dataLabel:dataLabel[13]}}">
        <the-test-tube 
          :currentSoilMoisture="zone2CurrentConditions['currentSoilMoisture5']" 
          :title="titles['bed8']"
        >
        </the-test-tube>
    </router-link>
    </div>
      </base-card>
    </div>
</template>

<script>
import BaseCard from '@/components/UI/BaseCard.vue';
import TheCircularDial from '../../components/greenhouse/TheCircularDial.vue';
import TheTestTube from '../../components/greenhouse/TheTestTube.vue';
import GrHsIcon from '../../components/UI/icons/GrHsIcon.vue';

export default {
  components: {
    TheCircularDial,
    TheTestTube,
    BaseCard,
    GrHsIcon
  },
  data() {
    return {
      zone1Limits: {
        tempLowerLimit: 10,
        tempUpperLimit: 20,
        vpdLowerLimit: 0.5,
        vpdUpperLimit: 1.5,
        co2LowerLimit: 200,
        co2UpperLimit: 450
      },
      zone2Limits: {
        tempLowerLimit: 20,
        tempUpperLimit: 28,
        vpdLowerLimit: 0.5,
        vpdUpperLimit: 1.5,
        co2LowerLimit: 200,
        co2UpperLimit: 450
      },

      zoneDegrees: [120, 40, 40], // Moved zoneDegrees to data

      zone1CurrentConditions: {
        currentTemp: 8,
        currentVPD: 0.8,
        currentCO2: 380,
        currentSoilMoisture1: 30,
        currentSoilMoisture2: 40,
        currentSoilMoisture3: 50,
      },
      zone2CurrentConditions: {
        currentTemp: 28,
        currentVPD: 1.4,
        currentCO2: 450,
        currentSoilMoisture1: 30,
        currentSoilMoisture2: 40,
        currentSoilMoisture3: 50,
        currentSoilMoisture4: 60,
        currentSoilMoisture5: 70
      },
      titles: {
        temp: '°C', 
        VPD: 'VPD',
        CO2: 'CO²',
        bed1: 'Bed 1',
        bed2: 'Bed 2',
        bed3: 'Bed 3',
        bed4: 'Bed 4',
        bed5: 'Bed 5',
        bed6: 'Bed 6',
        bed7: 'Bed 7',
        bed8: 'Bed 8',

      },
      dataLabel: [
        'cz1_temp',
        'cz1_CO2',
        'cz1_VPD',
        'cz1_bed1',
        'cz1_bed2',
        'cz1_bed3',
        'cz2_temp',
        'cz2_CO2',
        'cz2_VPD',
        'cz2_bed4',
        'cz2_bed5',
        'cz2_bed6',
        'cz2_bed7',
        'cz2_bed8',
        ]

    };
  },
};

</script>

<style scoped>
.icon {
  margin-right: 10px;
}
.dials-container {
  display: flex;
  flex-direction: row;
  justify-content: space-around; /* You can also use 'space-between', 'flex-start', 'center', etc. */
  align-items: center; /* This will vertically align the items in the center if needed */

}

.the-test-tube {
  display: flex;
  flex-direction: row;
  justify-content: space-around; /* You can also use 'space-between', 'flex-start', 'center', etc. */
  align-items: center; /* This will vertically align the items in the center if needed */
  margin-top: 30px;
}
</style>