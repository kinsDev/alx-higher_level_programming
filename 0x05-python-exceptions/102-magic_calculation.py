#!/usr/bin/python3

def custom_magic_calculation(x, y):
    final_result = 0

    for index in range(1, 3):
        try:
            if index > x:
                raise Exception('Limit Exceeded')

            final_result += x ** y / index
        except:
            final_result = y + x
            break

    return final_result
