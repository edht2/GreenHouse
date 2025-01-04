import paho.mqtt.client as mqtt
# We're using paho mqtt driver
import asyncio

def fire_and_forget(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)
        # runs the targeted function on a seperate thread
    return wrapped

class Subscriber():
    def __init__(self, broker, port):
        self.broker = broker
        self.port = port
        self.keepalive = 60
        
    @ fire_and_forget
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
