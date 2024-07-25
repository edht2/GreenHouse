from app.main.conf import configure

configure(
    mqttBrokerAddr='mqtt.eclipseprojects.io',
    tickFrequency=30,
    sensorSendFrequency=10
)

from app.extensions.mqtt import pub, sub
from app.extensions.utils import utils
from app.main.main import Main

@utils.fire_and_forget
def setupResponce():
    pub.publish('SYS/setup', "mqttBrokerAddr: mqtt.eclipseprojects.io|climateZone: 1|sendFrequency: 10")
    # the climate zone should change based on the current climatezones

sub.subscribe('SYS/setupReqest', setupResponce())
# this is the listener for a sensor pi to connect

app = Main()