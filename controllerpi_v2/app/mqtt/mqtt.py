from app.mqtt.pub import Publisher
from app.mqtt.sub import Subscriber
from app.config.config import mqtt_broker_address

sub = Subscriber
pub = Publisher

# you can use it like this:
#sub().subscribe(topic(s), on_message_function)
#pub().publish(topic, message)
