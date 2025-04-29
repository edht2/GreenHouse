import paho.mqtt.client as mqtt
from app.utils import utils
from app.app_extensions.log import log
import json

class Subscribe():
    def __init__(self, broker, port, topics, message_handler):
        self.message_handler = message_handler
        self.topics = topics
        self.broker = broker
        self.port = port
        self.keepalive = 60
        self.mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.mqttc.on_message = self.on_message
        self.mqttc.on_subscribe = self.on_subscribe
        self.mqttc.on_connect_fail = self.on_connect_failure
        self.mqttc.on_disconnect = self.on_disconnect


    def __str__(self):
        return f"{self.topics}, {self.broker}, {self.port}"

    def on_connect_failure(self, **kwargs):
        return log(False, 'mqtt', 'subscription', 'Failed to connect to', str(self.port))

    def on_message(self, mqttc, obj, msg):
        print(f"Received message on topic '{msg.topic}': {msg.payload.decode()}")
        mqtt_message_dict = {"topic": msg.topic, "payload": json.loads(msg.payload.decode())} # Construct the expected dictionary
        self.message_handler(mqtt_message_dict)

    def on_subscribe(self, mqttc, obj, mid, reason_code_list, properties):
        return log(True, 'mqtt', 'subscription', 'Successfully connected to', self.port)
    
    def on_disconnect(self, client, userdata, rc):
        if rc != 0:
            print(f"Disconnected unexpectedly from MQTT broker (reason code: {rc})")
        else:
            print("Disconnected cleanly from MQTT broker")
    
    def run(self):
        self.mqttc.connect(self.broker, self.port, self.keepalive)
        self.mqttc.subscribe(self.topics)
        self.mqttc.loop_forever()