import paho.mqtt.client as mqtt
import json

def on_message(client, userdata, msg):
    print(f"Received message on topic '{msg.topic}': {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message

broker_address = "mqtt.eclipseprojects.io"
port = 1883
topic = 'climate_zone_1/SCD30'

client.connect(broker_address, port, 60)
client.subscribe(topic)
client.loop_forever()