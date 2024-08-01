from app.extensions.mqtt import pub
from app.main.conf import climateZone

class MQTT:
    def send_sensor_data(self, data):
        pub.publish(f'SYS/ClimateZone{climateZone()}', message=data)
        # sends sensor data to the broker