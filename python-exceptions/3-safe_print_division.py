#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        ab = a / b
    except Exception:
        ab = None
    finally:
        print("Inside result: {}".format(ab))
        return ab
