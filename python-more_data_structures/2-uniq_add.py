#!/usr/bin/python3
def uniq_add(my_list=[]):
    numbers = set(my_list)
    suma = 0
    for a in numbers:
        suma += a
    return suma
