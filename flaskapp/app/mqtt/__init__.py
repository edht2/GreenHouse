from app.mqtt.pub import Publisher
from app.mqtt.sub import Subscribe
# these are the only two mqtt products I will need

from config import mqtt_broker_address


pub = Publisher (broker=mqtt_broker_address, port=1883)
#sub = Subscribe(broker=mqtt_broker_address, port=1883 , topics='SYS/<topic2>', message_handler=1)

# you can use it like this:
#sub.subscribe([('SYS/<topic1>', 1), ('SYS/<topic2>', 1)], sd)
#pub.publish('SYS/<topic1>', "<data to send>")
