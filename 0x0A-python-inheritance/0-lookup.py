#!/usr/bin/python3
"""
This script defines a function called 'lookup'.
"""

def lookup(obj):
    """
    This function takes an object as input and returns a list of attributes and methods available for that object.
    """
    return dir(obj)
