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
        
        # targets
        self.targetTemperatureRange = targetTemperatureRange
        self.relativeHumidityRange = relativeHumidityRange
        self.minimumTargetCO2percent = minimumTargetCO2percent
        
        sub.subscribe(f'SYS/ClimateZone{climateZoneNumber}/SCD30', self.onSCD30packetArival)
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
            
            if self.temperature < utils.mean(self.targetTemperatureRange): # if it is colder than half way 
                if self.targetTemperatureRange[0] > self.temperature:
                    print(f"CZ{self.no}: Very cold! Cannot sufficiently heat the greenhouse")
                    # alert!!! The climate zone is too cold and is in a dire moment.
                    # to heat it up, all windows are closed and a heating pipe is activeated
                
                elif utils.percentRange(self.targetTemperatureRange, 0.05) >= self.temperature:
                    # if it is below / on 5% allowed temp this is cold we must heat it up!
                    """ self.heating_solenoid.open() """ # We allow flow through the radiator
                    # if this doesn't work there will be problems!!
                    print(f"CZ{self.no}: Below 5% allowed temp -> Heating Solenoid is activating")
                
                elif utils.percentRange(self.targetTemperatureRange, 0.2) >= self.temperature:
                    # if it is below 20% allowed temp starting to get cold
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
