#!/usr/bin/python3
def list_division(my_list_a, my_list_b, list_len):
    new_list = []
    for i in range(list_len):
        try:
            quotient = my_list_a[i] / my_list_b[i]
        except (ValueError, TypeError):
            print("wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            new_list.append(quotient)
    return new_list
