#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            division_result = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
            division_result = 0
        except ZeroDivisionError:
            print("division by 0")
            division_result = 0
        except IndexError:
            print("out of range")
            division_result = 0
        finally:
            result_list.append(division_result)
    return result_list

my_list_1 = [10, 8, 4]
my_list_2 = [2, 4, 4]
result = list_division(my_list_1, my_list_2, max(len(my_list_1), len(my_list_2)))
print(result)

print("--")

my_list_1 = [10, 8, 4, 4]
my_list_2 = [2, 0, "H", 2, 7]
result = list_division(my_list_1, my_list_2, max(len(my_list_1), len(my_list_2)))
print(result)
