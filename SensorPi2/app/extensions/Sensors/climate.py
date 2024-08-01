from beds import Beds
from Humidity.HumidityCO2 import HumidityCO2

class Climate:
	def __init__(self, beds, target_temp_range:tuple, target_rh_range:tuple)
		self.beds = beds # the beds object!!

		self.target_temp_range = target_temp_range
		
		self.target_rh_range = target_rh_range		
		self.humidity_sensor = HumidityCO2
