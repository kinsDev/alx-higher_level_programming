#!/usr/bin/python3
if __name__ == "__main__":
    # Import the add function from add_0 module
    from add_0 import add

    # Assign values to variables a and b
    a = 1
    b = 2

    # Call the add function with a and b as arguments
    result = add(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, result))
