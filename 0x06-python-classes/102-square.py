#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square object.
    
    Attributes:
        __size (int): The size of a side of the square.
    """
    def __init__(self, size=0):
        """Initializes the square.
        
        Args:
            size (int): The size of a side of the square.
        Returns:
            None
        """
        self.size = size

    def area(self):
        """Calculates the area of the square.
        
        Returns:
            The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter method for the size attribute.
        
        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute.
        
        Args:
            value (int): The size of a side of the square.
        Returns:
            None
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    # Comparison methods for comparators
    
    def __lt__(self, other):
        """Compares if this square is less than another square by area.
        
        Args:
            other (Square): The square to compare against.
        Returns:
            True or False
        """
        return self.size < other.size

    # Other comparison methods (__le__, __eq__, __ne__, __ge__, __gt__) follow a similar pattern

# End of the Square class definition
