import paho.mqtt.client as mqtt
from app.tools.fire_and_forget import fire_and_forget
from app.config.config import mqtt_broker_address
from json import dumps

class Subscriber():
    def __init__(self, broker=mqtt_broker_address, port=1883):
        self.broker = broker
        self.port = port
    
    @ fire_and_forget
    def subscribe(self, topic, message_handler, del_after_use=False):
        
        if type(topic) == list:
            topics = [(tpc, 2) for tpc in topic]
        else:
            topics = [(topic, 2)]
            
        self.message_handler = message_handler
        self.del_after_use = del_after_use
        self.mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.mqttc.on_message = self.on_message
        
        self.mqttc.connect(self.broker, self.port, 60)
        self.mqttc.subscribe(topics)
        self.mqttc.loop_forever()

    def on_message(self, mqttc, obj, msg):
        self.message_handler(msg.payload.decode("utf-8"))
        if self.del_after_use:
            self.mqttc.disconnect()
