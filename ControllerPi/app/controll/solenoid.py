from app.controll.relay import relay
from app.extensions.log import log
from time import sleep
import asyncio

class Solenoid:
    def __init__(self, relayIndex):
        self.relayIndex = relayIndex
        self.state = 0

    # I have a seperate fire and forget decorator for the relays allowing togglable asyncronousity
    def fire_and_forget(f):
        """ Fire and forget is just asyncronously doing two things at the same time! 
        eg. extend and acctuator AND not have to wait for it to fully extend """
        def wrapped(*args, **kwargs):
            try:
                if args[2]:
                    return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)
                return f(args[0], args[1], args[2])
            except:
                return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)
        return wrapped

    @fire_and_forget
    def open(self, seconds=None, asynchronous=True):
        relay.turn_on_relay_by_index(self.relayIndex)
        log('ControllerPi', True, 'controll', 'solenoid', 'Opened watering solenoid for {time} seconds on relay', arg=self.relayIndex)
        if type(seconds) == int:
            sleep(seconds)
            relay.turn_off_relay_by_index(self.relayIndex)
            # finnish by closing the solenoid after waiting the requested time

    @fire_and_forget
    def close(self, seconds=None, asynchronous=True):
        relay.turn_off_relay_by_index(self.relayIndex)
        log('ControllerPi', True, 'controll', 'solenoid', 'Closed watering solenoid for {time} seconds on relay', arg=self.relayIndex)
