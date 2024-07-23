import asyncio
from numpy import mean as mn

class utils:
    def fire_and_forget(f):
        def wrapped(*args, **kwargs):
            return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)
            # runs the targeted function on a seperate thread
        return wrapped
    
    def meanSensorData(list_to_edit, to_add):
        """ I store the last 3 epochs of data from sensors. I do this to soften the effects of data anomalies """
        lte = list_to_edit
        try:
            lte[2] = lte[1]
            lte[1] = lte[0]
            lte[0] = to_add
        except:
            lte = [to_add, to_add, to_add]
        # it turns this:
        # [20, 30, 40]
        # to this:
        # ['newitem', 20, 30]
        #  →  →  →  →  →  →  →
        return lte
    
    def mean(list):
        return mn(list)
    
    def percentRange(range, float):
        return ((max(range) - min(range)) * float) + min(range)
       
       