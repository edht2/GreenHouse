from bed import Bed
from Chirp.soilMoistureSensors import SoilMoistureSensors

class Beds:
	def __init__(self):
		sms = SoilMoistureSensors().sensors
		ws = ["watering solenoid!"] # the watering solenoids!!

		self.bed1 = Bed(
			soil_moisture_sensors=(sms[0])
			watering_solenoid=(ws[0])
			minimum_water_sat=20 # 20 for 20% staturated water
			max_water_sat=50 # 50 for 50%
			)
		self.beds = [self.bed1] # i don't know how many beds there will be so I'm only entering 1
