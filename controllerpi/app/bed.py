from app.config.config import state, max_ticks_without_data
from app.mqtt.mqtt import sub
from app.control.solenoid import Solenoid
from json import load
from app.tools.log import log

class Bed:
    
    def __init__(self, climate_zone_number: int, bed_number: int) -> None:
        
        # *** Important Indexes ***
        self.bed_number = bed_number
        self.climate_zone_number = climate_zone_number
        # *************************
        
        # **** Sensor Readings ****
        self.soil_moisture_percent = None
        self.bed_temperature = None
        # *************************
        
        # *** Watering Solenoid ***
        self.watering_solenoid = Solenoid(
            state[self.climate_zone_number-1]["Beds"][self.bed_number-1]["wateringSolenoidRelayIndex"]
        )
        # *************************
        
        # ******* Safe mode *******
        self.ticks_without_sensor_data = 0
        self.is_safe_mode = False
        self.safe_mode_timer = 0
        # *************************
        
        sub().subscribe(f"{state[self.climate_zone_number-1]['climateZoneMQTTtopic']}/{state[climate_zone_number-1]['Beds'][bed_number-1]['MQTTtopic']}", self.on_sensor_update)
        # subscribe to the sensor data stream!
        # log mqtt topic print(f"{state[self.climate_zone_number-1]['climateZoneMQTTtopic']}/{state[climate_zone_number-1]['Beds'][bed_number-1]['MQTTtopic']}")
        

    def on_sensor_update(self, bed_data: str) -> None:
        """ This method is called when a new sensor data packet is recived by the MQTT broker. It updates the values of the bed for optimizing later"""     
           
        bed_data = eval(bed_data)
        # turn the string dictionary into a python dict object

        self.soil_moisture_percent = bed_data["median_soil_moist"]
        self.bed_temperature = bed_data["median_temp"]
        # update the sensor readings        
        print(f"Bed{self.bed_number} | soil_moisture: {self.soil_moisture_percent} bed_temp: {self.bed_temperature} status: {bed_data['status']}")


    def update(self) -> None:
        
        state = load(open("app/config/state.json"))["climateZones"]
        
        if (not self.is_safe_mode) and self.soil_moisture_percent and self.bed_temperature:
            # if there is sensor data, ie. the app has been sent a data packet
            
            self.ticks_without_sensor_data = 0
            # reset the 'ticks_without_sensor_data' variable
            
            if self.soil_moisture_percent <= state[self.climate_zone_number-1]["Beds"][self.bed_number-1]["bedMoistureRange"][0]:
                # if the soil moisture percent drops to (or below) the minimum bed moisture range
                if self.watering_solenoid.state == 0:
                    # if the solenoid is closed
                    self.watering_solenoid.open()
                    # open it!
                    
            elif self.soil_moisture_percent >= state[self.climate_zone_number-1]["Beds"][self.bed_number-1]["bedMoistureRange"][1]:
                # if the bed has too much water
                if self.watering_solenoid.state == 1:
                    # if the solenoid is open
                    self.watering_solenoid.close()
                    # close it!
                    
            # these are for perhaps the most important parts of the app - watering the beds
            
        elif not self.is_safe_mode:
            
            self.ticks_without_sensor_data += 1
            
            if self.ticks_without_sensor_data == max_ticks_without_data:
                # too many consecutive ticks without data! going into safe mode
                log("WARN", "bed", "safemode", "Going into safemode after missing too many ticks with data", arg=f"climate zone {self.climate_zone_number} / bed {self.bed_number}")
                
                self.is_safe_mode = True
            
            log("WARN", "bed", "update", "No sensor data (climatezone, bed)", arg=f"{self.climate_zone_number} : {self.bed_number}")
            # if this warn occurs too many times consecutivly then this bed should go into safe mode
        
        else:
            # in safe mode
            self.safe_mode_timer += 1
            # increment timer by 1
            
            if self.safe_mode_timer >= state[self.climate_zone_number-1]["Beds"][self.bed_number-1]["safeModeTimerFrequency"]:
                # if the timer runs out water the bed ↓
                
                self.safe_mode_timer = 0
                # reset the timer
                
                self.watering_solenoid.open(seconds=state[self.climate_zone_number-1]["Beds"][self.bed_number-1]["safeModeTimerPeriod"])
                # water the bed for the set period