#!/usr/bin/python3

""" Function that prits a square with character # """

def print_square(size):
    """
    Prints a square with character #

    Args:
        size(int): length of the square

    Raises:
    TypeError: if size is not an integer
    TypeError: if size is a float and is less than zero(0)
    ValueError: if size is less than zero(0)

    Return:
        square with character #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for s in range(size):
        [print("#", end="") for q in range(size)]
        print("")
