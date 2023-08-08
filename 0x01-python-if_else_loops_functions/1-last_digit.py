#!/usr/bin/python3
import random

def check_last_digit(number):
    last_digit = abs(number) % 10
    if number < 0:
        last_digit *= -1

    return last_digit

def print_last_digit_info(number, last_digit):
    print(f'Last digit of {number} is {last_digit}', end=' ')
    if last_digit > 5:
        print('and is greater than 5')
    elif last_digit == 0:
        print('and is 0')
    elif last_digit < 6 and last_digit != 0:
        print('and is less than 6 and not 0')

number = random.randint(-10000, 10000)
last_digit = check_last_digit(number)
print_last_digit_info(number, last_digit)
