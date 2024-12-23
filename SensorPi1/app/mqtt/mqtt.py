from app.mqtt.pub import Publisher
from app.mqtt.sub import Subscriber
from app.config import mqtt_broker_address

sub = Subscriber(broker=mqtt_broker_address, port=1883)
pub = Publisher (broker=mqtt_broker_address, port=1883)

# you can use it like this:
#sub.subscribe([('SYS/<topic1>', 1), ('SYS/<topic2>', 1)], sd)
#pub.publish('SYS/<topic1>', "<data to send>")
