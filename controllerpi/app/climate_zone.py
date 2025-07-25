from app.config.config import state, temperature_range_play
from app.tools.log import log
from app.control.actuator import Actuator
from app.tools.calculate_vpd import calculate_vpd
from lib.weather.client import Client as Weather_Client
from app.mqtt.mqtt import sub
from app.bed import Bed
from json import load

class ClimateZone:
    
    def __init__(self, climate_zone_number: int) -> None:
        
        self.climate_zone_number = climate_zone_number
        
        # *** Sensor Values ***
        self.temperature = None
        self.relative_humidity = None
        self.vapour_pressure_defecit = None
        self.co2_ppm = None
        
        self.values_set = False
        # *********************
        
        # ******** Beds *******
        self.beds = [
            Bed(self.climate_zone_number, bed["bedNumber"]) 
            for bed in state[self.climate_zone_number-1]["Beds"]]
        # get all of the beds and create a bed object for each one
        log('OK', f'climatezone{self.climate_zone_number}', 'init', 'All beds initialised successfuly')
        # *********************


        # ****** Windows ******
        self.side_windows = [
            Actuator([
                actuator_sw["actuatorRelayIndexExtend"], 
                actuator_sw["actuatorRelayIndexRetract"]],
                extension_time=40
        ) for actuator_sw in state[self.climate_zone_number-1]["sideWindows"]]
        # creates all of the side_windows in the actuator class so you can type 'side_window[index].extend()'
        
        self.top_windows = [
            Actuator([
                actuator_tw["actuatorRelayIndexExtend"], 
                actuator_tw["actuatorRelayIndexRetract"]],
                extension_time=60
        ) for actuator_tw in state[self.climate_zone_number-1]["topWindows"]]
        # locate the addresses of the top and side windows then initialise them to the Actuator object
        log('OK', f'climatezone{self.climate_zone_number}', 'init', 'Window acctuators initialised')
        # *********************
        
        sub().subscribe(f'climate_zone_{self.climate_zone_number}', self.on_sensor_update)
        # subscribe to climate zone data
        
        log('OK', f"climatezone{self.climate_zone_number}", "init", f"Successfuly initialised climate-zone")
        # log the climate-zone has been created!
        
        
    def on_sensor_update(self, data: str) -> None:
        # When a data packet gets recived from the sensor pi
        
        data = load(data)
        # turn json string into python dictionary
        
        self.temperature = data['median_temp']
        self.relative_humidity = data['median_rh']
        self.co2_ppm = data['median_co2_ppm']
        
        self.vapour_pressure_defecit = calculate_vpd(self.relative_humidity)
        # set the runtime variables  
        
        if not self.values_set:
            self.values_set = True
        # used for quick verification
        
        
    def update(self) -> None:
    
        for bed in self.beds:
            # for every bed do an update
            bed.update()
        
        state = load(open("app/config/state.json"))["climateZones"]
        # reload state incase there were any changes to the ranges and tergets
        
        """ Add climatezone temperature, VPD and CO₂ regulation here!! """
        
        """ This will use an 'extreme priority' based solution. Where if a value is out-side
        of a range it is prioritised to be fixed even if that means it will cause another
        problem soon. Otherwise temperature and VPD are prioritised.
        """
        
        if not self.values_set:
            # sensor data hasn't been recived yet! So no climate optimisation can occur
            log("WARN", f"climatezone{self.climate_zone_number}", "update", "No sensor data")
            """ if no sensor values are sent for a while; say 20 minutes, go into safe mode where the internal
            green-house data is assumed to be the same as the outside temperature. Of-coarse this is not good
            as the point of a green-house is to seperate the outside temperature and internal!"""
            return None
        
        temp_state = False
        vpd_state = False
        
        if (state['climateZones'][self.climate_zone_number-1]['targetTemperatureRange'][0] > self.temperature or
        state['climateZones'][self.climate_zone_number-1]['targetTemperatureRange'][1] < self.temperature):
            temp_state = True
            
        if (state['climateZones'][self.climate_zone_number-1]['targetVPDRange'][0] > self.vapour_pressure_defecit or
        state['climateZones'][self.climate_zone_number-1]['targetVPDRange'][1] < self.vapour_pressure_defecit):
            vpd_state = True
            
        if temp_state or vpd_state:
            # correct vpd and temp
            return None
    
        if not self.co2_ppm < state['climateZones'][self.climate_zone_number-1]['minimumTargetCO2ppm']:
            # if the CO₂ ppm is not less than the minimum level of CO₂
            return None
        
        """ if both temperature and vpd are sound but not CO₂ fix it. This can most easily be done by opening
        the windows and allow a breeze or diffusion to enrich the air with CO₂. In the future a CO₂ canister
        can be installed which could work regardless of the weather """
        
        if not Weather_Client().get_current().temp - temperature_range_play < state['climateZones'][self.climate_zone_number-1]['targetTemperatureRange'][0]:
            # if outside temperature is too cold ( with some play ) don't open the windows instead it is better to have a lower CO₂ concentrate
            return None
        
        if Weather_Client().get_current().wind_sp > state['windSpeedMax_knts'] * 1.852:
            # if wind speed it too high for the windows, damage can be caused therefore it is not worth opening the windows
            # 'Weather_Client.get_current.wind_sp' is in km/h so by multiplying max speed in knots by 1.852 we turn it to km/h
            return None
        
        if not Weather_Client().get_current().precip * 4 > state['topWindowPrecipitationLimit']:
            # if it is raining less hard than the top window limit open the windows
            # 'Weather_Client().get_current().precip' is in mm/0.25hr so multiply it by 4 to get mm/hr
            for top_window in self.top_windows: top_window.extend(True)
        
        if not Weather_Client().get_current().precip * 4 > state['topWindowPrecipitationLimit']:
            # if it is raining harder than the side windows limit don't allow the windows to open
            for side_window in self.side_windows: side_window.extend(True)