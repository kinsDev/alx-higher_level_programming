#!/usr/bin/python3
"""
This script defines the MyList class, a custom list subclass.
"""

class MyList(list):
    """
    A specialized subclass of the built-in list class.
    """
    def __init__(self):
        """
        Initializes an instance of the MyList class.
        """
        super().__init__()

    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.
        """
        print(sorted(self))
