#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    termino = 0
    for a in range(x):
        try:
            print("{:d}".format(my_list[a]), end="")
            termino += 1
            if termino is x:
                break
        except (TypeError, ValueError):
            pass
    print()
    return termino
