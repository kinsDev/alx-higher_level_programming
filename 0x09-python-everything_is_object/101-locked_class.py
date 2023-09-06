#!/usr/bin/python3
"""
Module defining a class that restricts dynamic attribute creation.
"""

class LockedClass():
    """
    A class that restricts dynamic attribute creation.
    """

    __slots__ = ['first_name']

    def __init__(self):
        """
        Initialize the LockedClass instance.
        """
        pass
