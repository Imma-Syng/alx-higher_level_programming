#!/usr/bin/python3
"""Module that finds the max integer in a list"""

def max_integer(list=[]):
    """ A function that finds the max integer
        in a list of integers

        Args:
            list=[]: list of numbers

        Return:
            None if list is empty
            max integer
        """
        if len(list) == 0:
            return None
        result = list[0]
        m = 1
        while m < len(list):
            if list[m] > result:
                result = list[m]
            m += 1
        return result
