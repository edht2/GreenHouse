import math

def calculate_vpd(temp: float, rh: float) -> float:
    """ Calculates VPD with the maximum posible saturated in that temperature subtract the current vapour pressure
    A good range for plants 0.8 and 1.2 """
    
    saturation_vapor_pressure = 0.6108 * math.exp((17.27 * temp) / (temp + 237.3))
    # calculate saturation vapor pressure (kPa)
    
    actual_vapor_pressure = (rh / 100) * saturation_vapor_pressure
    # calculate actual vapor pressure (kPa)
    
    vpd = saturation_vapor_pressure - actual_vapor_pressure
    # Calculate VPD (kPa)
    
    return vpd