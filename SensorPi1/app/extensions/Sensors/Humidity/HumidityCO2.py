import time
from scd30_i2c import SCD30

class HumidityCO2:
	def __init__(self):
		self.scd30 = SCD30()
		self.scd30.set_measurement_interval(2)
		self.scd30.start_periodic_measurement()

	def read(self):
		time.sleep(2) # we must wait for a measurement
		if self.scd30.get_data_ready():
			m = self.scd30.read_measurement()
			if m is not None:
				return m
			else:
				time.sleep(0.2)
				return read()
	def stop(self):
		self.sd30.stop_periodic_measurements()
		# if we want to stop the sensor you can!
