from app.mqtt.mqtt import sub
from app.tools.utils import utils
from app.tools.log import log
from json import dump

class ClimateZone:
    def __init__(self, beds, top_windows, side_windows, heating_solenoid, misting_solenoid, climate_zone_number, target_temperature_range, relative_humidity_range, minimum_target_CO2_percent, SCD30_sensor_mqtt_topic):
        
        if " ": # variable definitions
            self.climate_zone_number = climate_zone_number
            self.mqtt_topic:str = f"climate_zone_{climate_zone_number}"
            self.beds = beds

            self.top_windows = top_windows
            self.side_window = side_windows
            # top and side windows (Acctuator class)
            # so self.swin[0].extend() will extend an acctuator
            
            self.heating_solenoid = heating_solenoid
            self.misting_solenoid = misting_solenoid
            # the windows, both lists of Acctuator
            
            self.relative_humidity = None
            self.CO2ppm = None
            self.temperature = None # temp. in celceis
            # sensor readings which will be updated
        
            self.SCD30_sensor_mqtt_topic = SCD30_sensor_mqtt_topic
            # SCD30 mqtt topic
            
            self.target_temperature_range = target_temperature_range
            self.relative_humidity_range = relative_humidity_range
            self.minimum_target_CO2_percent = minimum_target_CO2_percent
            # the ideal ranges / minimums
        
        sub.subscribe(self.SCD30_sensor_mqtt_topic, self.on_SCD30_packet_arival)
        # this listener waits for the sensor pi to update information about the scd30 sensor
        
        
    def on_SCD30_packet_arival(self, data):
        data = dump(data)
        # make the string a python dictionary!
        
        self.relativeHumidity = data["RH%"]
        self.CO2ppm = data["temperature"]
        self.temperature = data["CO2ppm"]
        # set the runtime variables to the new incoming data
        
        
    def tick(self):
        for bed in self.beds:
            bed.tick()
        
        
        """ 
        ##################################################################    
        if self.temperature != None:
            # this if is necessary for when the greenhouse starts.
            # This is because the greenhouse.temperature has a starting value of None type!
            
             If the greenhouse goes out of the desired ranges it isn't really a problem. Sure it is best to have a perfectly regulated
            temperature, however it is not always posible to heat the greenhouse to the needed temeratures. For example: it is -2°C out
            side despite all of the windows closed and the heating pipe on, it may be the greenhouse is ~5°C. And while not desired, this
            is OK as any plant out side survives the -2°C. Again it is not ideal but sometimes the best you can do is all you will get. 
            
            if self.temperature < utils.mean(self.targetTemperatureRange): # if it is colder than half way                
                
                if self.targetTemperatureRange[0] > self.temperature:
                    print(f"CZ{self.no}: Very cold! Cannot sufficiently heat the greenhouse")
                    # OK this is not brilliant but it is OK.
                
                elif utils.percentRange(self.targetTemperatureRange, 0.05) >= self.temperature:
                    # if it is below / on 5% allowed temp let's turn on the radiator
                    # self.heating_solenoid.open() # We allow flow through the radiator
                    print(f"CZ{self.no}: Below 5% allowed temp -> Heating Solenoid is activating")
                
                elif utils.percentRange(self.targetTemperatureRange, 0.2) >= self.temperature:
                    # if it is below 20% allowed temp
                    for window_acctuator in self.swin:
                        if window_acctuator.state == 1:
                            #window_acctuator.retract()
                            print(f"CZ{self.no}: Below 20% allowed temp -> Side windows closing")
                            # close any open side_windows
                            
                elif utils.percentRange(self.targetTemperatureRange, 0.4) >= self.temperature:
                    # if it is below 40% allowed temp
                    self.heating_solenoid.close()
                    for window_acctuator in self.twin:
                        if window_acctuator.state == 1:
                            # window_acctuator.retract()
                            print(f"CZ{self.no}: Below 40% allowed temp -> Top windows closing")
                            # close any open top_windows                 
                            
            if self.temperature > utils.mean(self.targetTemperatureRange): # if it is hotter than half way

                if self.targetTemperatureRange[1] < self.temperature:
                    # green house is hotter than liked
                    print(f"CZ{self.no}: Above allowed temp range -> Alert")
                    # alert!!!
                    pass
                
                elif utils.percentRange(self.targetTemperatureRange, 0.95) <= self.temperature:
                    # if it is above 95% allowed
                    self.misting_solenoid.open()
                    # the misting solenoid should do the trick as when water evaporates it cools down
                
                elif utils.percentRange(self.targetTemperatureRange, 0.8) <= self.temperature:
                    # if it is above 20% allowed temp
                    self.misting_solenoid.close()
                    for window_acctuator in self.twin:
                        if window_acctuator.state == 0:
                            window_acctuator.extend()
                            # close any open top_windows
                            
                elif utils.percentRange(self.targetTemperatureRange, 0.6) <= self.temperature:
                    # if it is above 60% allowed temp. warm!
                    for window_acctuator in self.swin:
                        if window_acctuator.state == 0:
                            window_acctuator.extend()
                            # close any open top_windows     """        
