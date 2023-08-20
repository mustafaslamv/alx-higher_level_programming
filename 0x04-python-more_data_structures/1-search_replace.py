#!/usr/bin/python3
def search_replace(my_list, search, replace):

    def find_search(element):
        return replace if element == search else element

    new_list = [find_search(element) for element in my_list]

    return new_list
