from app.config import read_frequency
from scd30_i2c import SCD30 as SCD30driver
import time

class SCD30:
	def __init__(self):
		self.scd30 = SCD30driver()
		self.scd30.set_measurement_interval(read_frequency)
		# start reading from the scd30 sensor at the rate defined in config ('read_frequency')
		self.scd30.start_periodic_measurement()
		# start taking readings

	def read(self):
		if self.scd30.get_data_ready():
			m = self.scd30.read_measurement()
			if m is not None:
				return m
			else:
				time.sleep(0.2)
				return self.read()
				# returns: RH%, Temp and CO² in that order!
			
	def stop(self):
		self.scd30.stop_periodic_measurements()
		# if we want to stop the sensor we can
