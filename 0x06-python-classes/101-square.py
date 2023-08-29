#!/usr/bin/python3

"""
This module defines a class Square that represents a geometric square.
"""

class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square.

        Args:
            size (int): The size of the new square.
            position (tuple of int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get or set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple of int): The new position value.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using '#' and spaces."""
        if self.__size == 0:
            print("")
            return

        for _ in range(0, self.__position[1]):
            print("")
        for _ in range(0, self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    def __str__(self):
        """Return a string representation of the square."""
        if self.__size != 0:
            for _ in range(0, self.__position[1]):
                print("")
        for _ in range(0, self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
            if _ != self.__size - 1:
                print("")
        return ""
