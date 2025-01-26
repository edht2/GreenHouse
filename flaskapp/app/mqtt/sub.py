import paho.mqtt.client as mqtt
from app.utils import utils
from app.app_extensions.log import log

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
        self.mqttc.on_connect_fail = self.on_connect_failiar
        self.mqttc.connect(self.broker, self.port, self.keepalive)
        self.mqttc.subscribe(topics)
        self.mqttc.loop_forever()

    def __str__(self):
        return f"{self.topics}, {self.broker}, {self.port}"

    def on_connect_failiar(self, **kwargs):
        return log(False, 'mqtt', 'subscription', 'Failed to connect to', str(self.port))

    def on_message(self, mqttc, obj, msg):
        self.message_handler(msg.payload)

    def on_subscribe(self, mqttc, obj, mid, reason_code_list, properties):
        return log(True, 'mqtt', 'subscription', 'Successfully connected to', self.port)