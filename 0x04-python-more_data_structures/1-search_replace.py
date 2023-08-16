#!/usr/bin/python3
def search_replace(my_list, search, replace):

    def find_search(element):
        if element == search:
            return replace
        else:
            return element

    new_list = [find_search(element) for element in my_list]

    return new_list
