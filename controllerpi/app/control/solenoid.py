from app.control.relay import relay
from app.tools.log import log
from time import sleep
import asyncio

class Solenoid:
    def __init__(self, relay_index) -> None:
        self.relay_index = relay_index
        self.state = 0

    # I have a seperate fire and forget decorator for the relays allowing togglable asyncronousity
    def fire_and_forget(f):
        """ Fire and forget is just asyncronously doing two things at the same time! 
        eg. extend and actuator AND not have to wait for it to fully extend """
        def wrapped(*args, **kwargs):
            try:
                if args[2]:
                    return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)
                return f(args[0], args[1], args[2])
            except:
                return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)
        return wrapped

    @fire_and_forget
    def open(self, seconds=None, asynchronous=True) -> None:
        print("Opening solenoid on relay", self.relay_index)
        #relay.turn_on_relay_by_index(self.relay_index)
        self.state = 1
        log('ControllerPi', True, 'controll', 'solenoid', 'Opened watering solenoid for {time} seconds on relay', arg=self.relay_index)
        if type(seconds) == int:
            sleep(seconds)
            print("Closing solenoid on relay", self.relay_index, "after", seconds, "seconds open")
            #relay.turn_off_relay_by_index(self.relay_index)
            self.state = 0
            # finnish by closing the solenoid after waiting the requested time

    @fire_and_forget
    def close(self, seconds=None, asynchronous=True) -> None:
        #relay.turn_off_relay_by_index(self.relay_index)
        print(f"Closed solenoid on relay {self.relay_index}")
        self.state = 0
        log('ControllerPi', True, 'controll', 'solenoid', 'Closed watering solenoid for {time} seconds on relay', arg=self.relay_index)
