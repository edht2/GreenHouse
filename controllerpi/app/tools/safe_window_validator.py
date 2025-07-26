from lib.weather.client import Client as Weather_Client

def safe_window_validator(self, window: str) -> bool:

    from app.config.config import state
    # import as the function is ran to ensure we are using the most recent 'state.json'

    """ Makes sure that by opening the windows no damage will be caused to the green-house. For example if
    there is rain or high winds they could cause significant damage """
    
    if Weather_Client().get_current().wind_sp > state[f'{window}OpenMaxWindSpeed'] * 1.852:
        # if wind speed it too high for the windows, damage can be caused therefore it is not worth opening the windows
        # 'Weather_Client.get_current.wind_sp' is in km/h so by multiplying max speed in knots by 1.852 we turn it to km/h
        return False
    
    if not Weather_Client().get_current().precip * 4 > state[f'{window}PrecipitationLimit']:
        # if it is raining less hard than the window limit it is ok
        # 'Weather_Client().get_current().precip' is in mm/0.25hr so multiply it by 4 to get mm/hr
        return False
    
    return True
    # Weather is good - open the windows