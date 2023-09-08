#!/usr/bin/python3
"""
This script defines a function to divide a matrix by a scalar integer, 
rounding the result to two decimal places.
"""

def matrix_divided(matrix, div):
    """
    Divides a matrix by a scalar integer and returns a new matrix with the results.
    
    Args:
        matrix (list of lists): The input matrix, consisting of lists of integers/floats.
        div (int or float): The scalar value by which the matrix is to be divided.
        
    Returns:
        list of lists: A new matrix with elements divided by the scalar value and rounded to two decimal places.
    
    Raises:
        TypeError: If the matrix is not a list of lists containing integers or floats,
                   or if 'div' is not a number (int or float).
        ZeroDivisionError: If 'div' is equal to 0.
    """
    import decimal
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    
    # Check if the input matrix is a list
    if type(matrix) is not list:
        raise TypeError(error_msg)
    
    len_rows = []
    row_count = 0
    
    # Validate the matrix elements and count the rows
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_msg)
        
        len_rows.append(len(row))
        
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(error_msg)
        
        row_count += 1
    
    # Ensure all rows have the same size
    if len(set(len_rows)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if 'div' is a number and not equal to zero
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    
    # Perform matrix division and rounding
    new_matrix = list(map(lambda row:
                          list(map(lambda x: round(x/div, 2), row)), matrix))
    
    return new_matrix
