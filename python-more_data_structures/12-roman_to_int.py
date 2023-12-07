#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    if roman_string is None:
        return 0

    roman_dictionary = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    sum_of_values = 0
    previous_value = 0
    for char in reversed(roman_string):
        value = roman_dictionary.get(char)
        if value < previous_value:
            sum_of_values -= value
        else:
            sum_of_values += value
        previous_value = value
    return sum_of_values
