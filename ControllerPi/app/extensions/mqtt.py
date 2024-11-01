from app.extensions.MQTT.pub import Publisher
from app.extensions.MQTT.sub import Subscriber
from app.main.configuration import cfg

sub = Subscriber(broker=cfg["mqttBrokerAddr"], port=1883)
pub = Publisher (broker=cfg["mqttBrokerAddr"], port=1883)

# you can use it like this:
#sub.subscribe([('SYS/<topic1>', 1), ('SYS/<topic2>', 1)], onReceivedFunction)
#pub.publish('SYS/<topic1>', "<data to send>")