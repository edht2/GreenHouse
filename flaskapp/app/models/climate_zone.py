from app.extensions import db
from datetime import datetime as dt
from app.app_extensions.log import log
import math  # Import the math module

class ClimateZone(db.Model):
    __tablename__ = 'ClimateZone'
    id = db.Column(db.Integer, primary_key=True)
    climate_zone_name = db.Column(db.String, nullable=False)
    temp = db.Column(db.Float, nullable=False)  # Temperature in °C
    rh = db.Column(db.Float, nullable=False)  # Relative Humidity
    VPD = db.Column(db.Float, nullable=False)  # Vapor Pressure Deficit
    co2_ppm = db.Column(db.Float, nullable=False)  # CO2 ppm (Parts per million)
    ap_hPa = db.Column(db.Float, nullable=True)  # Atmospheric pressure in hPa (hectopascal)
    time_stamp = db.Column(db.DateTime, nullable=True)  # When were these readings taken?
    log(True, 'database', f'tbl_{__tablename__}', f"Table '{__tablename__}' successfully created")

    def __init__(self, climate_zone_name, temp, rh, co2_ppm, ap_hPa=None, time_stamp=None):
        """
        Custom constructor to calculate VPD before saving to the database.
        """
        self.climate_zone_name = climate_zone_name
        self.temp = temp
        self.rh = float(rh)  # Ensure rh is a float
        self.VPD = self.calculate_vpd(temp, self.rh)  # Calculate VPD here
        self.co2_ppm = co2_ppm
        self.ap_hPa = ap_hPa
        self.time_stamp = time_stamp

    @staticmethod
    def calculate_saturation_vapor_pressure(temp_c):
        """
        Calculates saturation vapor pressure (es) in kPa using the August-Roche-Magnus equation.
        :param temp_c: Temperature in Celsius (°C)
        :return: Saturation vapor pressure (es) in kPa
        """
        temp_c = float(temp_c)  # Ensure temp_c is a float
        es = 0.6108 * math.exp((17.27 * temp_c) / (temp_c + 237.3))
        return es

    @staticmethod
    def calculate_vpd(temp_c, rh_percent):
        """
        Calculates Vapor Pressure Deficit (VPD) in kPa.
        :param temp_c: Temperature in Celsius (°C)
        :param rh_percent: Relative humidity in percentage (%)
        :return: VPD in kPa
        """
        es = ClimateZone.calculate_saturation_vapor_pressure(temp_c)
        ea = es * (float(rh_percent) / 100.0)  # Ensure rh_percent is a float
        vpd = es - ea
        return vpd

    def co2_percent(self):
        """Calculates CO2 percentage from CO2 ppm."""
        co2_percentage = self.co2_ppm / 1000000.0  # Ensure float division
        co2_percentage *= 100
        return co2_percentage

