from app.main.main import Main
from app.extensions.mqtt import sub, pub
from app.main.conf import configure, mqttBrokerAddr, climateZone, sendFrequency

def on_config_responce(data:str):
    # the app data will be sent in a string that looks like this
    # mqttBrokerAddtr: 5|climateZone: 2|et.c.
    data = data.split("|")
    config = []
    for point in data:
        config.append(point.split(":")[1].strip())
    configure(mqttBrokerAddr=config[0], climateZone=config[1], sendFrequency=config[2])

sub.subscribe('SYS/setup', on_config_responce)
pub.publish('SYS/setupRequest', "requesting config!")

app = Main(mqttBrokerAddr=mqttBrokerAddr(), climateZone=climateZone(), sendFrequency=sendFrequency())

