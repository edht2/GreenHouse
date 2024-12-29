from app.tools.log import log
from app.mqtt.mqtt import sub
from app.config import tick_frequency
from json import loads

class Bed:
    def __init__(self, watering_solenoid, climate_zone_number, bed_number, mqtt_topic, soil_moisture_percentage_range):
        """ A bed comprises of a watering solenoid and a soil moisture sensor. """
        self.watering_solenoid = watering_solenoid
        
        self.ticks_since_last_watering = 0
        # this will be used to know if perhaps a chirp sensor brakes, how long does it usually take
        self.watering_ticks = 0
        # and how long was it watered
        
        self.bed_temperature = None
        self.soil_moisture_sensor_percent = None
        # sensor readings
        
        self.soil_moisture_percentage_range = soil_moisture_percentage_range
        # soil moisture percentage range this will be like 20% to 60% saturation
        # really there probably is no need for gardeners to ever have to water any of the plants
                
        self.climate_zone_number = climate_zone_number
        # climate zone number used for logs
        
        self.bed_number = bed_number
        # bed number used for dubug / logs
        
        self.mqtt_topic = mqtt_topic
        # mqtt topic, all data from this bed has this parent directory

        sub.subscribe("gerbil", self.on_sensor_update)
        
    def on_sensor_update(self, data): # When we recive a bed package, we need to update the values
        print("HELLO", data)
        # when the sensor pi sends an update on the sensor values ↓
        data = loads(data)
        # JSON → Python dict

        self.soil_moisture_sensor_percent = data["soil_moisture_reading"]
        self.bed_temperature = data["temperature_reading"]
        # update the values
        
        status = data["status"]
        # status is not used YET

    def should_water(self): # determite if we should water! 
        if not self.soil_moisture_sensor_percent:
            print("WARNING: No data for bed", self.bed_number)
            return False
        if self.soil_moisture_sensor_percent < self.soil_moisture_percentage_range[0]:
            # if the bed's soil-moisture saturation is below desired levels ↓
            print(f"Bed{self.no} is too dry: opening watering solenoid")
            return True
        
        if self.watering_solenoid.state == 1:
            # so if the watering solenoid is open: keep watering until the 'soil_moisture_sensor_percent' reaches the second value of 'soil_moisture_percentage_range' 
            return None
        
        if self.soil_moisture_sensor_percent > self.soil_moisture_percentage_range[1]:
            # bed has been sufficiently watered: disable watering solenoid
            print(f"Bed{self.no}: Bed has been sufficiently watered: closing watering solenoid")
            return False

    def tick(self):
        sw = self.should_water()
        if sw:
            # if 'should_water()' says to water the bed
            
            self.watering_solenoid.open(seconds=tick_frequency)
            # open the watering solenoid
            
            self.ticks_since_last_watering = 0
            # reset the ticks since last watering
            
            return log('ControllerPi', None, 'bed', 'wateringsolenoid', 'Opened the watering solenoids ', arg=f'climateZone:{self.climate_zone_number}@bed{self.bed_number}')
        
        elif sw == None:
            self.watering_ticks += 1
            # this variable can be used by the timer when that is implemented
            
        else:
            self.ticks_since_last_watering += 1
            # again used by the timer
