#!/usr/bin/python3
"""Defines a rectangle class based on 0-rectangle.py"""


class Rectangle:
    """a class that represents a rectangle"""

    def __init__(self, width=0, height=0):
        """initialises the attributes of the object

        Args:
            width(integer): width of rectangle.
            height(integer): height of rectangle.

        Raises:
            TypeError: if width is not an integer.
            TypeError: if height is not an integer.
            ValueError: if width is less than zero (0).
            ValueError: if height is less than zero (0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Sets the rectangle's width"""
        return self.__width

    @width.setter
    def sidth(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >+ 0")
        self.__width = value

    @property
    def height(self):
        """Sets the rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise Value Error("height must be >= 0")
        self.__height = value
