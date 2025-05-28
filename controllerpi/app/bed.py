from app.config.config import state, device_name
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
        
        self.watering_solenoid = Solenoid(
            state[self.climate_zone_number-1]["Beds"][self.bed_number-1]["wateringSolenoidRelayIndex"]
        )
        # create a solenoid object with the relay index assigned to the bed
        
        sub().subscribe(f"{state[self.climate_zone_number-1]['climateZoneMQTTtopic']}/{state[climate_zone_number-1]['Beds'][bed_number-1]['MQTTtopic']}", self.on_sensor_update)
        # subscribe to the sensor data stream!
        print(f"{state[self.climate_zone_number-1]['climateZoneMQTTtopic']}/{state[climate_zone_number-1]['Beds'][bed_number-1]['MQTTtopic']}")
        
        

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
        if self.soil_moisture_percent and self.bed_temperature:
            # if there is sensor data, ie. the app has been sent a data packet
            
            if self.soil_moisture_percent <= state[self.climate_zone_number-1]["Beds"][self.bed_number-1]["bedMoistureRange"][0]:
                # if the soil moisture percent drops to (or below) the minimum bed moisture range
                if self.watering_solenoid.state == 0:
                    # if the solenoid is closed
                    self.watering_solenoid.open()
                    print(f"Watering bed{self.bed_number}")
                    # open it!
                    
            elif self.soil_moisture_percent >= state[self.climate_zone_number-1]["Beds"][self.bed_number-1]["bedMoistureRange"][1]:
                # if the bed has too much water
                if self.watering_solenoid.state == 1:
                    # if the solenoid is open
                    self.watering_solenoid.close()
                    print(f"Stopped watering bed{self.bed_number}")
                    # close it!
                    
            # this are for perhaps the most important part of the app - watering the beds
        else:
            log(device_name, "WARN", "bed", "update", "No sensor data for bed", arg=self.bed_number)
            # if this warn occurs too many times consecutivly then this bed should go into safe mode