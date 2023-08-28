#!/usr/bin/python3
def safe_function(func, *args):
    try:
        result = func(*args)
        return result
    except Exception as exception:
        import sys
        print("Exception: {}".format(exception), file=sys.stderr)
        return None
