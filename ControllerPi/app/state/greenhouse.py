from app.main.bed import Bed
from app.main.climateZone import ClimateZone
from app.main.greenhouse import GreenHouse
from app.controll.solenoid import Solenoid
from app.controll.acctuator import Acctuator
from app.bedModes.soilmoisture import SM
from app.extensions.log import log
from json import loads, dump

setupJSON = open("app/state/state.json")
setupJSONstring = setupJSON.read()
setupJSON.close()
setupDict = loads(setupJSONstring)

def getGreenhouseObject():
    gh = []
    
    for cz in setupDict['climateZones']:
        # for each climate zone

        beds = []
        sideWindowAcctuators = []
        topWindowAcctuators = []

        for bed in cz['Beds']:
            # for each bed
            beds.append(Bed(
                wateringMethod=SM(targetMoistureRange=bed['bedMoistureRange'],chirpSensorI2CAddress=bed["chirpSensorI2CAddress"], chirpSensorCalibration=bed["chirpSensorCalibration"]),
                wateringSolenoid=Solenoid(bed['wateringSolenoidRelayIndex']),
                climateZoneNumber=cz['climateZoneNumber'],
                bedNumber=bed['bedNumber'],
                MQTTtopic=bed['MQTTtopic'])
                ) # make a bed object
            
        for swin in cz['sideWindows']:
            # for every side window!
            sideWindowAcctuators.append(Acctuator(
                relayIndexes=[swin['acctuatorRelayIndexExtend'], swin['acctuatorRelayIndexRetract']],
                extensionTime=60))
            
        for twin in cz['topWindows']:
            # for every top window!
            topWindowAcctuators.append(Acctuator(
                relayIndexes=[twin['acctuatorRelayIndexExtend'], twin['acctuatorRelayIndexRetract']],
                extensionTime=60))
        
        gh.append(ClimateZone(
            beds=beds,
            topWindows=topWindowAcctuators,
            sideWindows=sideWindowAcctuators,
            heatingSolenoid=cz['heatingSolenoidRelayIndex'],
            mistingSolenoid=cz['mistingSolenoidRelayIndex'],
            climateZoneNumber=cz['climateZoneNumber'],
            extremeTemperatureRange=cz['extremeTemperatureRange'],
            relativeHumidityRange=cz['targetHumidity%'],
            minimumTargetCO2percent=cz['minimumTargetCO2%'],
            SCD30sensorMqttTopic=cz['SCD30sensorMqttTopic']))
        
    return gh

GREENHOUSE = getGreenhouseObject()
      
def onConfigRequest(data:str):
    # the request will look something like "climateZone : 1"
    try:
        climateZoneNumber = int(data.split(':')[1].strip())
        # the climate zone number has been extracted!
        GREENHOUSE[climateZoneNumber-1]
        # now I must turn all of the bed objects into a string parsable json!
        bedList = []
        for bed in GREENHOUSE.greenhouse[climateZoneNumber-1]['Beds']:
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
