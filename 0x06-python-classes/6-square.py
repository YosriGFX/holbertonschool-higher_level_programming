#!/usr/bin/python3
class Square:
    __doc__ = "Square Validation"

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size != 0:
            i = 0
            while (i < self.__size):
                j, e = 0, 0
                if len(self.__position) == 2:
                    while (e < self.__position[0]):
                        if self.__position[1] > 0:
                            print(end=" ")
                        else:
                            pass
                        e += 1
                while (j < self.__size):
                    print(end="#")
                    j += 1
                print()
                i += 1
        else:
            print()

    @property
    def position(self):
        return (self.__position)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        self.__size = value
        if type(self.__size) == int:
            if self.__size < 0:
                raise ValueError("size must be >= 0")
            else:
                print("here")
                return self.__size
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):
        self.__position = value
        if type(self.__position) == tuple:
            if (self.__position[0] >= 0) and (self.__position[1] >= 0):
                if not (self.__position[3]):
                    return self._position
        raise TypeError("position must be a tuple of 2 positive integers")
