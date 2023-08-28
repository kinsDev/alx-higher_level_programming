#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_count = 0  # Initialize the count of printed elements
    for i in range(x):
        try:
            print(my_list[i], end="")  # Print the element without moving to the next line
            printed_count += 1  # Increment the count of printed elements
        except IndexError:
            break  # If an IndexError occurs, exit the loop
        
    print()  # Print a new line after all elements are printed
    return printed_count  # Return the count of printed elements

# Test cases
my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

