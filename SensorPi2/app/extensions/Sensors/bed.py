class Bed:
	def __init__(self, soil_moisture_sensors:list, watering_solenoid:object, minimum_water_sat, max_water_sat):
		self.soil_moisture_sensors = soil_moisture_sensors
		self.watering_solenoid = watering_solenoid
		self.min = minimum_water_sat
		self.max = max_water_sat

	def read(self):
		sum = 0
		for soil_moisture_sensor in self.soil_moisture_sensors:
			soil_moistrure_sensor.trigger()
			sum += soil_moisture_sensor.moist_percent
		return sum / len(self.soil_moisture_sensors)

	def tick(self): # tick checks the water level and waters accordingly! (ran every,,5 seconds)
		""" A tick is an update. This reads the moisture of the soil and waters accordingly """
		sum = 0

		for sensor in self.soil_moisture_sensors:
			sum += sensor.moist_percent
		sum /= len(self.soil_moisture_sensors)
		if sum < self.min: # if it is less than the being the target moisture mimimum
			pass
			# enable the watering solenoid for 5 seconds

