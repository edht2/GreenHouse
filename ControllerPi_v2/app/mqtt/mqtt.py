from app.mqtt.pub import Publisher
from app.mqtt.sub import Subscriber
from app.config.config import mqtt_broker_address

sub = Subscriber(broker=mqtt_broker_address, port=1883)
pub = Publisher (broker=mqtt_broker_address, port=1883)

# you can use it like this:
#sub.subscribe(topic, on_message_function)
#pub.publish(topic(s), message)
