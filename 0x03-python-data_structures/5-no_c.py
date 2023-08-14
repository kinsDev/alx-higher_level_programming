#!/usr/bin/python3

def no_c(my_string):
    without_c = my_string.translate({ord('c'): None})
    without_c = without_c.translate({ord('C'): None})
    return without_c
