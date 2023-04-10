#!/usr/bin/python3

"""Defines the sum of two integers"""


def add_integer(a, b=98):
    
    """
    A function that adds two numbers.

    Args:
        a(int) = first number.
        b(int) = second number.

    Raises:
        TypeError : if a and b are not integers or floats.

    Returns:
        sum of int(a) and int (b).
    """
    
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError('a must be an integer')
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
