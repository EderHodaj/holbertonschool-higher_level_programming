#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return 0
    single = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    double = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    result = 0
    for key in double.keys():
        if key in roman_string:
            result += double[key]
            roman_string = roman_string.replace(key, "")
    for letter in roman_string:
        if letter in single:
            result += single[letter]
    return result
