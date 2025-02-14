import asyncio

class utils:
    def fire_and_forget(f):
        def wrapped(*args, **kwargs):
            return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)
            # runs the targeted function on a seperate thread
        return wrapped
    
    def mean(lst):
        # returns the mean average of the inputed list
        print(lst)
        if not lst:
            return 0
        #return sum(lst) / len(lst)
        return lst[0]
    
    def median_of_five(numbers):
        """
        Returns the median of five numbers in a list.

        Args:
            numbers: A list of five numbers.

        Returns:
            The median of the five numbers.
            Raises ValueError if the input list does not contain exactly five numbers.
        """

        if len(numbers) != 5:
            #raise ValueError("Input list must contain exactly five numbers.")

            return 0

        # Sort the list to easily find the median
        numbers.sort()

        # The median is the middle element (index 2) of the sorted list
        return numbers[2]

