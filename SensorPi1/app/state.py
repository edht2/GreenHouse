from app.extensions.Sensors.Chirp.chirpSensor import ChirpSensor
from app.extensions.Sensors.Humidity.HumidityCO2 import HumidityCO2
import time

calcfg = open("app/extensions/Sensors/Chirp/calibration.txt", "r")
lines = calcfg.readlines()

chirpSensor1 = ChirpSensor(address=0x34, no=1, min_moist=int(lines[0].strip().split()[0]), max_moist=int(lines[0].strip().split()[1]))
chirpSensor2 = ChirpSensor(address=0x33, no=2, min_moist=int(lines[2].strip().split()[0]), max_moist=int(lines[2].strip().split()[1]))
chirpSensor3 = ChirpSensor(address=0x32, no=3, min_moist=int(lines[2].strip().split()[0]), max_moist=int(lines[2].strip().split()[1]))
chirpSensor4 = ChirpSensor(address=0x31, no=4, min_moist=int(lines[3].strip().split()[0]), max_moist=int(lines[3].strip().split()[1]))
chirpSensor5 = ChirpSensor(address=0x30, no=5, min_moist=int(lines[4].strip().split()[0]), max_moist=int(lines[4].strip().split()[1]))
chirpSensors = [chirpSensor1, chirpSensor2, chirpSensor3, chirpSensor4, chirpSensor5]

SCD30_humco2 = HumidityCO2()

def calibrateSensors():
    for i in range(len(chirpSensors)):
        input("Place a sensor into water: ") 
        time.sleep(1) # wait for the sensor
        moisture_readings = []
        for no, chirp_sensor in enumerate(chirpSensors):
            moisture_readings.append(chirp_sensor.takeReading()[0])
        sensor = chirpSensors[moisture_readings.index(max(moisture_readings))]
        max_moisture = sensor.moist
        input("Remove sensor from water: ")
        sensor.takeReading(sensor)
        min_moisture = sensor.moist
        print(f"WET: {max_moisture}  DRY: {min_moisture}")
        sensor.max_moist, sensor.min_moist = max_moisture, min_moisture
        chirpSensors[chirpSensors.index(sensor)] = sensor
    
    calcfg = open("calibration.txt", "w")
    write = ''
    for sensor in chirpSensors:
        write = write + f"{sensor.min_moist} {sensor.max_moist}\n"
    calcfg.write(write)
    calcfg.close()