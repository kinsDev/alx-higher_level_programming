#!/usr/bin/python3
"""
This module defines the function is_same_class
"""

def is_same_class(obj, a_class):
    """
    Returns True if 'obj' is an instance of the exact class 'a_class', otherwise returns False.
    """
    return (type(obj) == a_class)
