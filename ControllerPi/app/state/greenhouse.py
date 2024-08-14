from app.main.bed import Bed
from app.main.climateZone import ClimateZone
from app.controll.solenoid import Solenoid
from app.controll.acctuator import Acctuator
from app.wateringMethods.soilmoisture import SM
from app.extensions.log import log
from json import loads, dump

setupJSONstring = open("app/state/state.json").read()
setupDict = loads(setupJSONstring)

GREENHOUSE = []
# greenhouse[0].beds[0].wateringMethod.soilMoistureFloat = new data

for climateZone in setupDict['climateZones']:
    # for each climate zone

    beds = []
    sideWindowAcctuators = []
    topWindowAcctuators = []

    for bed in climateZone['beds']:
        # for each bed
        beds.append(Bed(
            wateringMethod=SM(targetMoistureRange=bed['bedMoistureRange'],chirpSensorI2CAddress=bed["chirpSensorI2CAddress"], chirpSensorCalibration=bed["chirpSensorCalibration"]),
            wateringSolenoid=Solenoid(bed['wateringSolenoidRelayIndex']),
            climateZoneNumber=climateZone['climateZoneNumber'],
            bedNumber=bed['bedNumber'],
            MQTTtopic=bed['MQTTtopic'])
            ) # make a bed object
        
    for swin in climateZone['sideWindows']:
        # for every side window!
        sideWindowAcctuators.append(Acctuator(
            relayIndexes=[swin['acctuatorRelayIndexExtend'], swin['acctuatorRelayIndexRetract']],
            extensionTime=60))
        
    for twin in climateZone['topWindows']:
        # for every top window!
        topWindowAcctuators.append(Acctuator(
            relayIndexes=[twin['acctuatorRelayIndexExtend'], twin['acctuatorRelayIndexRetract']],
            extensionTime=60))
    
    GREENHOUSE.append(ClimateZone(
        beds=beds,
        topWindows=topWindowAcctuators,
        sideWindows=sideWindowAcctuators,
        heatingSolenoid=climateZone['heatingSolenoidRelayIndex'],
        mistingSolenoid=climateZone['mistingSolenoidRelayIndex'],
        climateZoneNumber=climateZone['climateZoneNumber'],
        extremeTemperatureRange=climateZone['extremeTemperatureRange'],
        relativeHumidityRange=climateZone['targetHumidity%'],
        co2ppmMin=climateZone['minimumTargetCO2%']))
    
def onConfigRequest(data:str):
    # the request will look something like "climateZone : 1"
    try:
        climateZoneNumber = int(data.split(':')[1].strip())
        # the climate zone number has been extracted!
        GREENHOUSE[climateZoneNumber-1]
        # now I must turn all of the bed objects into a string parsable json!
        bedList = []
        for bed in GREENHOUSE[climateZoneNumber-1]['beds']:
            bedDict = {
                "chirpSensorI2CAddress" : bed.wateringMethod.chirpSensorI2CAddress if bed.wateringMethod.__class__ == SM else None,
                "chirpSensorCalibration" : bed.wateringMethod.chirpSensorCalibration if bed.wateringMethod.__class__ == SM else None,
                "bedNumber" : bed.no,
                "MQTTtopic" : bed.MQTTtopic
            }
            bedList.append(bedDict)
        
        responceDict = dump({"beds" : bedList})
        # the dump function translates a python dictionary to a JSON string very cool!
        return responceDict

    except Exception as e:
        log('ControllerPi', False, 'configuration', 'mqtt', 'Incompatible format request message: ', arg=data, error=e)
        return "Incompatible message"