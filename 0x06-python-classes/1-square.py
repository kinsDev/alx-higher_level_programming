#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of a side of the square.

    Methods:
        __init__(self, size): Initializes a square with a given size.
    """
    def __init__(self, size):
        """Initializes a square with a given size.

        Args:
            size (int): The size of a side of the square.

        Returns:
            None
        """
        self.__size = size
