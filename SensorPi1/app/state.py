from app.extensions.Sensors.SCD30.scd30 import SCD30 as SCD30sen
from app.main.bed import Bed

def instantiateSensorPi(data):
    beds = []
    for bed in data['beds']:
        # for each bed
        beds.append(Bed(chirpSensorI2CAddress=bed["chirpSensorI2CAddress"], chirpSensorCalibration=bed['chirpSensorCalibration'], bedNumber=bed['bedNumber']))
        
    SCD30 = SCD30sen()
    # this is the RH%, CO², Temperature sensor!
    return beds, SCD30