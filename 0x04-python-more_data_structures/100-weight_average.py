#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        total_numerators = 0
        total_denominator = 0
        for score, weight in my_list:
            total_numerators += (score * weight)
            total_denominator += weight
        return (total_numerators / total_denominator) if total_denominator != 0 else 0
    return 0
