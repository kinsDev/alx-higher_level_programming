#!/usr/bin/python3
"""
This is the "add_integer" module.
The add_integer module provides a function, add_integer(a, b), to add two numbers.
"""

def add_integer(a, b):
    """
    Return the sum of two numbers.

    :param a: The first number (integer or float).
    :param b: The second number (integer or float).
    :return: The sum of 'a' and 'b' as an integer.
    :raises TypeError: If 'a' or 'b' is not an integer or float.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer or float")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer or float")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
