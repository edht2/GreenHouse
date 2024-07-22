from app.extensions.utils import utils
from app.extensions.mqtt import pub, sub
from app.main.main import Main

@utils.fire_and_forget
def setupResponce():
    pub.publish('SYS/setup', "mqttBrokerAddr: mqtt.eclipseprojects.io|climateZone: 1|sendFrequency: 10")
    # the climate zone should change based on the current climatezones

sub.subscribe('SYS/setup', setupResponce())
# this is the listener for a sensor pi to connect

app = Main()