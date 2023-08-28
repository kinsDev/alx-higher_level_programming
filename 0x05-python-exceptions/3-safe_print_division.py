#!/usr/bin/python3
def safe_print_division(numerator, denominator):
    try:
        result = numerator / denominator  # Try to perform the division
    except ZeroDivisionError:
        result = None  # Handle division by zero
    finally:
        print("Inside result: {}".format(result))  # Print the result (either division or None)
    return result
