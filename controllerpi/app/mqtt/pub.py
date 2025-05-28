import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes
from app.tools.fire_and_forget import fire_and_forget
from app.config.config import mqtt_broker_address
import time

class Publisher:
    def __init__(self, broker=mqtt_broker_address, port=1883):
        self.broker_address = broker
        self.broker_port = port 

    @ fire_and_forget
    def publish(self, topic, message):
        self.client = mqtt.Client(client_id="client", callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
        self.client.connect(self.broker_address, port=self.broker_port)
        self.publish_properties = Properties(PacketTypes.PUBLISH)
        self.publish_properties.ResponseTopic = 'response'
        self.publish_properties.CorrelationData = b"334"
        self.client.publish(topic=topic, payload=message, qos=2, properties=self.publish_properties)
        self.client.loop_start()    # start the loop
        time.sleep(5)               # wait
        self.client.loop_stop()     # stop the loop
