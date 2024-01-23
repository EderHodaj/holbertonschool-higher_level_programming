#!/usr/bin/python3
def uppercase(str):
	for letter in str:
		letter = ord(letter)
		if letter >= 97 and letter <= 122:
			letter = letter - 32
		print(chr(letter), end="")
	print()

uppercase("best")
uppercase("Best School 98 Battery street")