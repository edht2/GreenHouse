import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes
from app.app_extensions.log import log
from app.utils import utils
import time

class Publisher:
    def __init__(self, broker, port):
        self.broker_address = broker
        self.broker_port = port
        self.client = mqtt.Client(client_id="client", callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
        self.client.connect(self.broker_address, port=self.broker_port)
        self.publish_properties = Properties(PacketTypes.PUBLISH)
        self.publish_properties.ResponseTopic = 'response'
        self.publish_properties.CorrelationData = b"334"

    @utils.fire_and_forget
    def publish(self, topic, message):
        self.client.publish(topic=topic, payload=message, qos=1, properties=self.publish_properties)
        log(True, 'mqtt', 'publishment', 'Published message:', message)
        self.client.loop_start()    # start the loop
        time.sleep(5)               # wait
        self.client.loop_stop()     # stop the loop

    def __str__(self):
        return f"Sent {self.payload} at {self.topic} to {self.broker_address}"