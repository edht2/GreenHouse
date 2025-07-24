from app.config.config import state
from app.tools.log import log
from app.control.actuator import Actuator
from app.mqtt.mqtt import sub
from app.bed import Bed
from json import load

class ClimateZone:
    
    def __init__(self, climate_zone_number: int) -> None:
        
        self.climate_zone_number = climate_zone_number
        
        # *** Sensor Values ***
        self.temperature = None
        self.relative_humidity = None
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
        # set the runtime variables
        
        if not self.values_set:
            self.values_set = True
        # used for quick verification
        
        
    def update(self) -> None:
        
        for bed in self.beds:
            
            bed.update()
            # do an update!!
        
        state = load(open("app/config/state.json"))["climateZones"]
        # reload state incase there were any changes to the ranges and tergets
        
        """ Add climatezone temperature, VPD and CO₂ regulation here!! """
        
        """ This will use an 'extreme priority' based solution. Where if a value is out-side
        of a range it is prioritised to be fixed even if that means it will cause another
        problem soon. Otherwise temperature and VPD are prioritised.
        """
        
        if not self.values_set:
            # sensor data hasn't been recived yet! So no climate optimisation can occur
            return None
        
        if 
            
         
        
        