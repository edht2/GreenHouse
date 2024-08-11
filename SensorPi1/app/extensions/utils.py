import asyncio

class utils:
    def fire_and_forget(f):
        def wrapped(*args, **kwargs):
            return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)
            # runs the targeted function on a seperate thread
        return wrapped
    
    def mean(lst):
        # returns the mean average of the inputted list
        return sum(lst) / len(lst)