#!/usr/bin/python3
"""Defines a Square class."""

class Square:
    """Represents a square with private instance attribute size."""

    def __init__(self, size=0):
        """
        Initializes a square.

        Args:
            size (int): The size of the side of the square.

        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer.
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
