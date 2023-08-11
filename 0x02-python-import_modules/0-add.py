#!/usr/bin/python3
if __name__ == "__main__":
    """Print the result of adding 1 and 2"""
    
    # Import the add function from add_0.py
    from add_0 import add
    
    # Assign values to variables a and b
    a = 1
    b = 2
    
    # Print the sum of a and b using the add function
    print("{} + {} = {}".format(a, b, add(a, b)))
