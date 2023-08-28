#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        # Try to print the value as an integer
        print("{:d}".format(value))
    except (ValueError, TypeError) as error:
        # If an exception occurs, print the error message to stderr
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return False  # Indicate that printing failed
    else:
        return True  # Indicate that printing succeeded
