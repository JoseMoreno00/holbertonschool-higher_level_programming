#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for a in new:
        new[a] *= 2
    return (new)
