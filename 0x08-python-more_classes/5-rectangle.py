#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        """Initializes a rectangle

        Args:
            width
            height
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        """height
        """
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """rectangle height
        Args:
            value : height
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """printable string
        Returns:
            string
        """
        rep_str = ""
        if self.__width != 0 and self.__height != 0:
            rep_str += "\n".join("#" * self.__width
                                 for i in range(self.__height))

        return rep_str

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
