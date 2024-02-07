#!/usr/bin/python3
"""Contains an class : 'Square'"""


class Square:
    def __init__(self, size=0):
        """Initialize a Square instance with a given size."""
        try:
            if not isinstance(size, int):
                raise Exception('size must be an integer')
            elif size < 0:
                raise Exception('size must be >= 0')
            else:
                self.__size = size
        except Exception as e:
            print(e)

    def area(self):
        """Return the area of the square."""
        try:
            return self.__size ** 2
        except Exception as e:
            print(e)
