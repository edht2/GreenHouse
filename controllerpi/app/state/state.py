from app.bed import Bed
from app.climate_zone import ClimateZone
from app.controll.solenoid import Solenoid
from app.controll.acctuator import Acctuator
from json import loads

setup_dict = loads(open("app/state/state.json").read())

GREEN_HOUSE = []

for cz in setup_dict['climateZones']:
    # for each climate zone
    
    beds = [
        Bed(
            watering_solenoid=Solenoid(bed['wateringSolenoidRelayIndex']),
            climate_zone_number=cz['climateZoneNumber'],
            bed_number=bed['bedNumber'],
            mqtt_topic=bed['MQTTtopic'],
            soil_moisture_percentage_range=bed['bedMoistureRange']
        ) for bed in cz['Beds']]
    # all of the beds
    
    side_window_acctuators = [Acctuator(relayIndexes=[swin['acctuatorRelayIndexExtend'], swin['acctuatorRelayIndexRetract']], extensionTime=60) for swin in cz['sideWindows']]
    # all of the side windows
    
    top_window_acctuators = [Acctuator(relayIndexes=[twin['acctuatorRelayIndexExtend'], twin['acctuatorRelayIndexRetract']], extensionTime=60) for twin in cz['topWindows']]       
    # all of the top windows

    GREEN_HOUSE.append(ClimateZone(
        beds=beds,
        top_windows=side_window_acctuators,
        side_windows=top_window_acctuators,
        heating_solenoid=cz['heatingSolenoidRelayIndex'],
        misting_solenoid=cz['mistingSolenoidRelayIndex'],
        climate_zone_number=cz['climateZoneNumber'],
        target_temperature_range=cz['targetTemperatureRange'],
        relative_humidity_range=cz['targetHumidity%'],
        minimum_target_CO2_percent=cz['minimumTargetCO2%'],
        SCD30_sensor_mqtt_topic=cz['SCD30sensorMqttTopic']
        )
    )
