from app.extensions.mqtt import sub
from app.extensions.utils import utils
from app.extensions.log import log

class ClimateZone:
    def __init__(self, beds, top_windows, side_windows, climateZoneNumber, mqttTopic='SYS/climateZone'):
        self.no:int = climateZoneNumber
        self.mqttTopic:str = mqttTopic + climateZoneNumber
        self.beds:list = [3]
        self.top_windows = []
        self.side_windows = []
        # data
        self.relativeHumidity:int = None
        self.CO2ppm:int = None
        
        # targets
        self.rh_range = [0, 1]
        self.co2ppm_min = 100
        
        #finnish contructing the class
        self.setupListener()
    
    @utils.fire_and_forget
    def setupListener(self):
        def on_data_received(data):
            for bed in self.beds:
                bed.soilMoistureSensorFloat = data['chirpSensors'][f'sen{self.beds.index(bed)}']['float'] 
            self.relativeHumidity = data['RH']
            self.CO2ppm = data['CO2']
            log('ControllerPi', True, 'climatezone', 'sensordata', 'Recived sensor data for ', arg=f'climateZone{self.no}')
    
        sub.subscribe(self.mqttTopic, on_data_received)
        
    def tick(self):
        for bed in self.beds:
            bed.tick()
            
        if self.CO2ppm
            