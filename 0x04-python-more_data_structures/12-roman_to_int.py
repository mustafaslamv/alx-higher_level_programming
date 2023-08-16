#!/usr/bin/python3

def roman_to_int(roman_string):

    if not roman_string or not isinstance(roman_string, str):
        return 0

    values = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    total = 0
    for roman in reversed(roman_string):
        current = values[roman]
        next_value = values[next(reversed(roman_string))] if roman_string[
            1:] else 0

        total += current if current <= next_value else -current

    return total
