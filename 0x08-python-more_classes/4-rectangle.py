#!/usr/bin/python3
class Rectangle:
    """Rectangle

    Attributes:
        width
        height
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """rectangle width
        """
        return self.__width

    @property
    def height(self):
        """rectangle height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """rectangle width
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        """calculates the rectangle's perimeter
        Returns:
            The perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """printable string
        Returns:
            string
        """
        reps = ""
        if self.__width != 0 and self.__height != 0:
            reps += "\n".join("#" * self.__width
                                 for i in range(self.__height))

        return reps

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
