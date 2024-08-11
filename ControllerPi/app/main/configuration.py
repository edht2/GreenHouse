from json import loads

configFile = open("app/cfg.json", "r")
configFileDict = loads(configFile.read())
cfg = configFileDict
configFile.close()