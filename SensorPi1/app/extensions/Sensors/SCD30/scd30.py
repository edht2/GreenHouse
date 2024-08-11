import time
from scd30_i2c import SCD30 as SCD30driver

class SCD30:
	def __init__(self):
		self.scd30 = SCD30driver()
		self.scd30.set_measurement_interval(2)
		self.scd30.start_periodic_measurement()

	def takeReading(self):
		if self.scd30.get_data_ready():
			m = self.scd30.read_measurement()
			if m is not None:
				return m
			else:
				time.sleep(0.2)
				return self.takeReading()
			
	def stop(self):
		self.scd30.stop_periodic_measurements()
		# if we want to stop the sensor you can!
