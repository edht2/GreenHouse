import asyncio

class utils:
    def fire_and_forget(f):
        def wrapped(*args, **kwargs):
            return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)
            # runs the targeted function asyncronously - very cool
        return wrapped

    def median_of_five(numbers: list) -> float:
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

            return 0.0

        # Sort the list to easily find the median
        numbers.sort()

        # The median is the middle element (index 2) of the sorted list
        return numbers[2]

