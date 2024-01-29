#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numerals = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000
    }
    count = 0
    for letter in roman_string:
        for key, value in roman_numerals.items():
            if letter == key:
                count += value
    return count
