#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nlist = []
    for n in my_list:
        if n % 2 == 0:
            nlist.append(True)
        else:
            nlist.append(False)
    return nlist
