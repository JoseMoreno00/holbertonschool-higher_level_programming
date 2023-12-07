#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for a in range(x):
        try:
            print(my_list[a], end="")
        except Exception:
            print()
            return a
    print()
    return x
