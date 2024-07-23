from app.extensions.mqtt import sub
from app.extensions.utils import utils
from app.extensions.log import log

class ClimateZone:
    def __init__(self, beds, top_windows, side_windows, heating_solenoid, climateZoneNumber, mqttTopic='SYS/climateZone'):
        self.no:int = climateZoneNumber
        self.mqttTopic:str = mqttTopic + climateZoneNumber
        self.beds:list = beds
        self.twin:list = top_windows
        self.swin:list = side_windows
        self.heating_solenoid = heating_solenoid
                
        # data
        self.relativeHumidity:int = None
        self.CO2ppm:int = None
        self.tempC:int = None
        
        # targets
        self.tempC_range = [10, 30]
        self.rh_range = [0, 1]
        self.co2ppm_min = 100

        #finnish contructing the class
        self.setupAsncDataRecorder()
    
    @utils.fire_and_forget
    def setupAsncDataRecorder(self):
        def on_data_received(data):
            for bed in self.beds:
                bed.soilMoistureSensorFloat = data['chirpSensors'][f'sen{self.beds.index(bed)+1}']['float'] 
            self.relativeHumidity = data['RH']
            self.CO2ppm = data['CO2']
            log('ControllerPi', True, 'climatezone', 'sensordata', 'Recived sensor data for ', arg=f'climateZone{self.no}')
    
        sub.subscribe(self.mqttTopic, on_data_received)
        
    def ValidateOutSideTemp():
        pass
        
    def tick(self):
        for bed in self.beds:
            bed.tick()  
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
        if self.tempC < utils.mean(self.tempC_range): # if it is colder than half way 
            if self.tempC_range[0] > self.tempC:
                # MAGOR PROBLEM TOO COLD
                # alert!!!
                pass
            
            elif utils.percentRange(self.tempC_range, 0.05) >= self.tempC:
                # if it is below / on 5% allowed temp this is cold we must heat it up!
                self.heating_solenoid.open() # We allow flow through the radiator
                # if this doesn't work there will be problems!!
            
            elif utils.percentRange(self.tempC_range, 0.2) >= self.tempC:
                # if it is below 20% allowed temp starting to get cold
                for window_acctuator in self.swin:
                    if window_acctuator.state == 1:
                        window_acctuator.retract()
                        # close any open top_windows
                        
            elif utils.percentRange(self.tempC_range, 0.4) >= self.tempC:
                # if it is below 40% allowed temp
                for window_acctuator in self.twin:
                    if window_acctuator.state == 1:
                        window_acctuator.retract()
                        # close any open top_windows
                        
        if self.tempC > utils.mean(self.tempC_range): # if it is hotter than half way 
            if self.tempC_range[1] < self.tempC:
                # MAGOR PROBLEM TOO HOT
                # alert!!!
                pass
            
            elif utils.percentRange(self.tempC_range, 0.95) <= self.tempC:
                # if it is above 95% allowed temp this is hot!
                self.misting_solenoid.open()
                # the misting solenoid should do the trick as when water evaporates it cools down
                
            
            elif utils.percentRange(self.tempC_range, 0.8) <= self.tempC:
                # if it is below 20% allowed temp starting to sweat
                for window_acctuator in self.twin:
                    if window_acctuator.state == 0:
                        window_acctuator.extend()
                        # close any open top_windows
                        
            elif utils.percentRange(self.tempC_range, 0.6) <= self.tempC:
                # if it is above 60% allowed temp. warm!
                for window_acctuator in self.swin:
                    if window_acctuator.state == 0:
                        window_acctuator.extend()
                        # close any open top_windows                        
            
                        
            

        if self.CO2ppm < self.co2ppm_min and not self.isCold:
            # co2 level is too low open some windows!
            for window_acctuator in self.side_windows:
                window_acctuator.extend()
            