#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = 0
    for element in set(my_list):
        a += element
    return a
