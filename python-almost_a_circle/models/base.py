#!/usr/bin/python3

class Base:
    """Base class for managing id attribute in future classes."""

    __nb_objects = 0  # Private class attribute

    def __init__(self, id=None):
        """
        Class constructor.

        Args:
            id (int): If provided, assigns the public instance
                      attribute 'id' with the given value. Otherwise,
                      increments '__nb_objects' and assigns the new
                      value to 'id'.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
