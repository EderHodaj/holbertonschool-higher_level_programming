#!/usr/bin/python3
def print_last_digit(number):
	last_d = abs(number) % 10 * (-1 if number < 0 else 1)
	return last_d
