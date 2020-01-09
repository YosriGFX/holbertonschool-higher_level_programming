#!/usr/bin/python3
class Square:
    __doc__ = "Square Validation"

    def __init__(self, size=0):
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                def area(self):
                    return (size * size)
        else:
            raise TypeError("size must be an integer")
        self.__class__.area = area
