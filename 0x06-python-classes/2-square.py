#!/usr/bin/python3
class Square:
    __doc__ = "Square Validation"
    _Square__size = {}

    def __init__(self, size=0):
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            self._Square__size = size
        else:
            raise TypeError("size must be an integer")
