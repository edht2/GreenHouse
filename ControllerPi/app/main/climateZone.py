from app.extensions.mqtt import sub
from app.extensions.utils import utils
from app.extensions.log import log
from json import dump

class ClimateZone:
    def __init__(self, beds, topWindows, sideWindows, heatingSolenoid, mistingSolenoid, climateZoneNumber, targetTemperatureRange, relativeHumidityRange, minimumTargetCO2percent, SCD30sensorMqttTopic):
        self.no:int = climateZoneNumber
        self.mqttTopic:str = f"SYS/climateZone{climateZoneNumber}"
        self.beds:list = beds

        # relay controlled
        self.twin:list = topWindows
        self.swin:list = sideWindows
        self.heatingSolenoid = heatingSolenoid
        self.mistingSolenoid = mistingSolenoid
                
        # sensor readings
        self.relativeHumidity:int = None
        self.CO2ppm:int = None
        self.temperature:int = None # temp. in celceis
                
        self.SCD30sensorMqttTopic = SCD30sensorMqttTopic
        # SCD30 mqtt topic, what did you think?
        
        # targets
        self.targetTemperatureRange = targetTemperatureRange
        self.relativeHumidityRange = relativeHumidityRange
        self.minimumTargetCO2percent = minimumTargetCO2percent
        
        sub.subscribe(self.SCD30sensorMqttTopic, self.onSCD30packetArival)
        # this listener waits for the sensor pi to update information about the scd30 sensor
        
    def onSCD30packetArival(self, data):
        data = dump(data)
        # make the string a python dictionary!
        
        self.relativeHumidity = data["humidityReading"]
        self.CO2ppm = data["CO2ppmReading"]
        self.temperature = data["temperatureReading"]
        
    def tick(self):
        for bed in self.beds:
            bed.tick()
            
        if self.temperature != None:
            # this if is necessary for when the greenhouse starts.
            # This is because the greenhouse.temperature has a starting value of None type!
            
            """ If the greenhouse goes out of the desired ranges it isn't really a problem. Sure it is best to have a perfectly regulated
            temperature, however it is not always posible to heat the greenhouse to the needed temeratures. For example: it is -2°C out
            side despite all of the windows closed and the heating pipe on, it may be the greenhouse is ~5°C. And while not desired, this
            is OK as any plant out side survives the -2°C. Again it is not ideal but sometimes the best you can do is all you will get. """
            
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
                            # close any open top_windows            
