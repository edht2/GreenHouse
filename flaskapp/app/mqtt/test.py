from app.mqtt import Subscribe, Publisher
from app.utils import utils

def message_handler(p):
    print(str(p))

@utils.fire_and_forget
def subs():
    sub = Subscribe("mqtt.eclipseprojects.io", 1883, [("SYS/climateZone1",1),("SYS/climateZone2",1)], message_handler)
    
def pubs():
    pub = Publisher('mqtt.eclipseprojects.io', 1883)
    pub.publish('SYS/climateZone1',"{'temp': 16.5, 'rh': 75, 'CO2':710,'soilMoisture':[{'bed1': 44}, {'bed2':42}]}")