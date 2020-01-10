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
                while (e < self.position[0]):
                    if self.position[1] > 0:
                        print(end="_")
                    else:
                        print(end=" ")
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
                return self.__size
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):
        self.__position = value
        if self.__position != ((int > 0), (int > 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            __a, __b = self.__position[0], self.__position[1]
            return (a, b)
