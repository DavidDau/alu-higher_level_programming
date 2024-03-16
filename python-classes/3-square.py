#!/usr/bin/python3
"""Define a  Square"""


class Square:
    """ Represents a Square"""
    def __init__(self, size=0):
        """Initialize a new square.
        Args:
          size(int): The size of new square.
        """

        if not isinstance(size, int):
            raise TypeError("size must ba an integer")
        elif size < 0:
            raise ValueError("size must ba >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
