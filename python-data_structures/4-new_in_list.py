#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        iktiylbiac = my_list.copy()
        iktiylbiac[idx] = element
        return iktiylbiac
    else:
        return my_list
