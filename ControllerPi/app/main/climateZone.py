from app.extensions.mqtt import sub
from app.extensions.utils import utils
from app.extensions.log import log
from json import dump

class ClimateZone:
    def __init__(self, beds, topWindows, sideWindows, heatingSolenoid, mistingSolenoid, climateZoneNumber, extremeTemperatureRange, relativeHumidityRange, minimumTargetCO2percent, SCD30sensorMqttTopic):
        self.no:int = climateZoneNumber
        self.mqttTopic:str = f"SYS/climateZone{climateZoneNumber}"
        self.beds:list = beds

        # relay controlled
        self.twin:list = topWindows
        self.swin:list = sideWindows
        self.hsol = heatingSolenoid
        self.msol = mistingSolenoid
                
        # data
        self.relativeHumidity:int = None
        self.CO2ppm:int = None
        self.tempC:int = None
        self.SCD30sensorMqttTopic = SCD30sensorMqttTopic
        
        # targets
        self.temperatureRange = extremeTemperatureRange
        self.relativeHumidityRange = relativeHumidityRange
        self.minimumTargetCO2percent = minimumTargetCO2percent
        
        self.isCold = False
        self.isHot = False

        #finnish contructing the class
        
    def onSCD30packetArival(self, data):
        data = dump(data)
        # make the string a python dictionary!
        if data["status"] == "ER":
            # error!! safe mode.
            pass
        else:
            self.relativeHumidity = data["humidityReading"]
            self.CO2ppm = data["CO2ppmReading"]
            self.tempC = data["temperatureReading"]
                   
        
    def tick(self):
        for bed in self.beds:
            bed.tick()
        if self.tempC != None:
            """ For temperature this is the chart I created for working
                            | Alert! too hot
                Max temp | Misting
                        0.9 |
                        0.8 | Open top windows
                        0.7 |
                        0.6 | Open side windows
                        0.5 |
                        0.4 | Close top windows
                        0.3 |
                        0.2 | Close side windows
                        0.1 |
                Min temp | Heating pipes
                            | Alert! too cold
                            """
            # temp managment
            if self.tempC < utils.mean(self.temperatureRange): # if it is colder than half way 
                if self.temperatureRange[0] > self.tempC:
                    print(f"CZ{self.no}: Very cold! Cannot sufficiently heat the greenhouse")
                    # alert!!! The climate zone is too cold and is in a dire moment.
                    # to heat it up, all windows are closed and a heating pipe is activeated
                
                elif utils.percentRange(self.temperatureRange, 0.05) >= self.tempC:
                    # if it is below / on 5% allowed temp this is cold we must heat it up!
                    """ self.heating_solenoid.open() """ # We allow flow through the radiator
                    # if this doesn't work there will be problems!!
                    print(f"CZ{self.no}: Below 5% allowed temp -> Heating Solenoid is activating")
                
                elif utils.percentRange(self.temperatureRange, 0.2) >= self.tempC:
                    # if it is below 20% allowed temp starting to get cold
                    for window_acctuator in self.swin:
                        if window_acctuator.state == 1:
                            #window_acctuator.retract()
                            print
                            # close any open top_windows
                            
                elif utils.percentRange(self.temperatureRange, 0.4) >= self.tempC:
                    # if it is below 40% allowed temp
                    self.heating_solenoid.close()
                    self.isCold = True
                    for window_acctuator in self.twin:
                        if window_acctuator.state == 1:
                            window_acctuator.retract()
                            # close any open top_windows                
            if self.tempC > utils.mean(self.temperatureRange): # if it is hotter than half way 
                if self.temperatureRange[1] < self.tempC:
                    # MAGOR PROBLEM TOO HOT
                    # alert!!!
                    pass
                
                elif utils.percentRange(self.temperatureRange, 0.95) <= self.tempC:
                    # if it is above 95% allowed temp this is hot!
                    self.misting_solenoid.open()
                    # the misting solenoid should do the trick as when water evaporates it cools down
                    
                
                elif utils.percentRange(self.temperatureRange, 0.8) <= self.tempC:
                    # if it is below 20% allowed temp starting to sweat
                    self.misting_solenoid.close()
                    for window_acctuator in self.twin:
                        if window_acctuator.state == 0:
                            window_acctuator.extend()
                            # close any open top_windows
                            
                elif utils.percentRange(self.temperatureRange, 0.6) <= self.tempC:
                    # if it is above 60% allowed temp. warm!
                    self.isHot = True
                    for window_acctuator in self.swin:
                        if window_acctuator.state == 0:
                            window_acctuator.extend()
                            # close any open top_windows                        
                
            # humidity reg.
            if self.relativeHumidity < utils.mean(self.relativeHumidityRange): # if it is less humid 
                if utils.percentRange(self.relativeHumidity, 0.2) < self.relativeHumidity:
                    # humidity is low
                    if not (self.isHot or self.isCold):
                        """if the temperature is perfect, we can spray some water.
                        we would do this as a portion of the sprayed water would evapourate
                        and thus increase the humidity. """
                        self.misting_solenoid.open()      
            if self.relativeHumidity > utils.mean(self.relativeHumidityRange):
                if utils.percentRange(self.relativeHumidity, 0.8) > self.relativeHumidity:
                    # humidity is high
                    if not (self.isHot or self.isCold):
                        """ when the humidity is high we can open the windows assuming the RH outside is lower.
                        if not, just the wind blowing through would cause the tempature to decrease with 
                        evapouritive cooling and the dew point would raise likley resulting in some condensation"""
                        for side_window_acctuator in self.swin:
                            if side_window_acctuator.state == 1:
                                side_window_acctuator.retract()

            # co2 mgnt.
            if self.CO2ppm < self.co2ppm_min and not self.isCold:
                # co2 level is too low open some windows!
                for window_acctuator in self.side_windows:
                    window_acctuator.extend()
                
