from app.extensions.log import log

def configure(
    mqttBrokerAddr:str,
    tickFrequency:int,
    sensorSendFrequency:int
    ):

    cfg_file = open("app/config.txt", "w")
    cfg_file.write(
    f"""mqttBrokerAddr: {mqttBrokerAddr}
tickFrequency: {tickFrequency}
sensorSendFrequency: {sensorSendFrequency}
    """)
    cfg_file.close()
    log(f'ControllerPi', True, 'config', 'setup', 'Successfully written to the config file')
    
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

def tickFrequency():
    return read_cfg()[1][0]

def sensorSendFrequency():
    return read_cfg()[2][0]