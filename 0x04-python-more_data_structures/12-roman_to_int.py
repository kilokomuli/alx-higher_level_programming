#!/usr/bin/python3
def roman_to_int(roman_string):
    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev = 0

    if not isinstance(roman_string, str) or not roman_string:
        return 0
    for numeral in reversed(roman_string):
        v = value[numeral]

        if v < prev:
            result -= v
        else:
            result += v
        prev = v
    return result
