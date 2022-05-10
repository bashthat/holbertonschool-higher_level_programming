#!/usr/bin/python3
def search_replace(my_list, search, replace):
    current_list = my_list[:]
    for xyz in range(len(current_list)):
        if current_list[xyz] == search:
            current_list[xyz] = replace
            return (current_list)
