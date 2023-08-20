#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    div_num = 0
    if not my_list:
        return 0
    for tuples in my_list:
        sum += (tuples[0] * tuples[1])
        div_num += tuples[1]
    return (sum / div_num)
