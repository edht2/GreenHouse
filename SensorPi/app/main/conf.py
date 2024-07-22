def read_cfg():
    cfg_file = open("app/config.txt", "r")
    cfg_raw =  cfg_file.readlines()
    cfg = []
    
    for line in cfg_raw:
        line = line.split(":")
        line_data = line[1].split()
        line_title = line[0]
        cfg.append(line_data)
    return cfg

def mqttBrokerAddr():
    return read_cfg()[0][0]

def climateZone():
    return read_cfg()[1][0]

def sendFrequency():
    return read_cfg()[2][0]

from app.extensions.log import log

def configure(
    mqttBrokerAddr:str,
    climateZone:int,
    sendFrequency:int):

    cfg_file = open("app/config.txt", "w")
    cfg_file.write(
    f"""mqttBrokerAddr: {mqttBrokerAddr}
climateZone: {climateZone}
sendFrequency: {sendFrequency}""")
    cfg_file.close()
    log(f'sensorPi{climateZone}', True, 'config', 'setup', 'Successfully updated the config file')
    