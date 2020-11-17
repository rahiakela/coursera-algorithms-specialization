"""
Implements a proleptic Gregorian calendar date as a Julian day number.
"""
class Date:

    def __init__(self, month, day, year):
        """Creates an object instance for the specified Gregorian date."""
        self._julian_day = 0

        """
        The first line of the equation, T = (M - 14) / 12, has to be changed since 
        Python's implementation of integer division is not the same as the mathematical definition.
        """
        tmp = 0
        if month < 3:
            tmp = -1
        self._julian_day = day - 32075 + \
                           (1461 * (year + 4800 + tmp) // 4) \
                           (367 * (month - 2 - tmp * 12) // 12) - \
                           (3 * ((year + 4900 + tmp) // 100) // 4)