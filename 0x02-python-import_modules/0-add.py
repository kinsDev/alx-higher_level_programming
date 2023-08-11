#!/usr/bin/python3
if __name__ == "__main__":
    """Print the result of adding 1 and 2"""
    from add_0 import add

    num1 = 1
    num2 = 2
    result = add(num1, num2)
    print("{} + {} = {}".format(num1, num2, result))
