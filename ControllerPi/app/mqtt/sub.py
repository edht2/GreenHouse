import paho.mqtt.client as mqtt
# We're using paho mqtt driver
from app.tools.utils import utils
# utils is used for fire and forget

class Subscriber():
    def __init__(self, broker, port):
        self.broker = broker
        self.port = port
        self.keepalive = 60
        
    @utils.fire_and_forget
    def subscribe(self, topic, message_handler, del_after_use=False):
        self.message_handler = message_handler
        self.del_after_use = del_after_use
        self.mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.mqttc.on_message = self.on_message
        topics = [(topic, 1)]
        self.mqttc.connect(self.broker, self.port, self.keepalive)
        self.mqttc.subscribe(topics)
        self.mqttc.loop_forever()

    def on_message(self, mqttc, obj, msg):
        self.message_handler(msg.payload.decode("utf-8"))
        if self.del_after_use:
            self.mqttc.disconnect()
