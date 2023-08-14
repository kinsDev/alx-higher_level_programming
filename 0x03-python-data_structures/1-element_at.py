#!/usr/bin/python3
"""
 Retrieves an element from a list, similar to C-style indexing.
    
    :param my_list: The list from which to retrieve the element
    :param idx: The index of the element to retrieve
    :return: The element at the specified index, or None if index is out of range
"""
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
