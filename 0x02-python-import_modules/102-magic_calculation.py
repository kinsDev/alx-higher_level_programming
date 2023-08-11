#!/usr/bin/python3

def magic_calculation(a, b):
    """
    Emulates the given Python bytecode pattern using add and sub functions from magic_calculation_102 module.
    
    :param a: An input value
    :param b: Another input value
    :return: Calculated result based on conditions
    """
    from magic_calculation_102 import add, sub
    
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
