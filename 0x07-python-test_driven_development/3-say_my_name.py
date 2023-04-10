#!/usr/bin/python3
""" Defines a function that a name """

def say_my_name(first_name, last_name=""):
    """ 
    Print my name

    Args:
        first_name(str) = First name to be printed
        last_name(str) = second name to be printed

    Raises:
        TypeError: first_name be a string
        TypeError: last_name must be a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
