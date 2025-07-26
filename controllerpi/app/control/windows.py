from app.tools.safe_window_validator import safe_window_validator
from app.control.actuator import Actuator
from app.config.config import state

class Windows:
    
    def __init__(self, window: str) -> None:
        
        self.window_type = window
        
        self.window_classes = [
            Actuator([
                actuator["actuatorRelayIndexExtend"], 
                actuator["actuatorRelayIndexRetract"]],
                extension_time=40
        ) for actuator in state[self.climate_zone_number-1][window]]
        # creates all of the windows in the actuator class so you can type 'side_window[index].extend()'
        
    def open(self) -> None:
        # opens all windows
        
        if safe_window_validator(self.window_type):
            # if it is safe to open the top windows
            
            for window in self.window_classes: window.extend()
            # open all of the windows
            
    def close(self) -> None:
        # closes all windows
        
        if safe_window_validator(self.window_type):
            # if it is safe to open the top windows
            
            for window in self.window_classes: window.retract()