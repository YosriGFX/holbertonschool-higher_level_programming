#!/usr/bin/python3
class Square:
    __doc__ = "Square Validation"

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size != 0:
            for f in range(self.__position[1]):
                print()
            i = 0
            while (i < self.__size):
                for e in range(self.__position[0]):
                    print(end=" ")
                for j in range(self.__size):
                    print(end="#")
                print()
                i += 1
        else:
            print()

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

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 \
        or type(value[0]) is not int or value[0] < 0 \
        or type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
