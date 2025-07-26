def percent_range(_range: list, value: float) -> float:
    """ Finds how far though the range a value is.
    eg. range = 10-20 value = 15 output = 50%
    This works through ((x-min(r)) / (max(r)-min(r))) * 100% """    
    return (value - min(_range) / (max(_range) - min(_range))) * 100
