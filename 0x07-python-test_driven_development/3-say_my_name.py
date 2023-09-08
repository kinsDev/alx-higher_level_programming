#!/usr/bin/python3
"""
This is the "3-say_my_name" module.
The 3-say_my_name module provides one function, say_my_name.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints "My name is" followed by the first name and an optional last name.
    
    Args:
        first_name (str): The first name to be included in the message.
        last_name (str, optional): The last name to be included in the message. Defaults to an empty string.
    
    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
