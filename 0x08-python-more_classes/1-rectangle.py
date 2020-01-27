#!/usr/bin/python3
"""
Class Rectangle

"""


class Rectangle:

    """

    Attributes:

        width (int):  width
        height (int):  height
    """

    def __init__(self, width=0, height=0):
        """
        args:
        width (int): width
        height (int): height
        Returns: None
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width
        Returns:
           attribute __width
        """
        return self.__width

    @property
    def height(self):
        """height
        Returns:
           attribute __height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """width
        Args:
            value (int): the width

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height
        Args:
            value (int): the height value
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
