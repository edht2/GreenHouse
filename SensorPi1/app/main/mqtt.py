from app.extensions.mqtt import pub
from app.main.configuration import cfg

class MQTT:
    def send_sensor_data(data):
        pub.publish(f'SYS/ClimateZone{cfg["climateZone"]}', data)
        # sends sensor data to the broker