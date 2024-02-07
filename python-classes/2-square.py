#!/usr/bin/python3
"""Contains an class : 'Square'"""

class Square:
    def __init__(self, size=0):
        """Initialize a Square instance with a given size."""
        # Check if the size parameter is an integer
        if type(size) != int:
            # Raise a TypeError if size is not an integer
            raise TypeError('size must be an integer')
        # Check if the size parameter is less than zero
        elif size < 0:
            # Raise a ValueError if size is less than zero
            raise ValueError('size must be >= 0')
        else:
            # Set the size attribute to the given size
            self.__size = size
