#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    Prints all integers in the given list.
    
    :param my_list: List of integers to be printed
    """
    for number in my_list:
        print("{:d}".format(number))
