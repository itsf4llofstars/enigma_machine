#!/usr/bin/env python3
"""Plug Board Test Script"""

letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

plugboard = []

while True:
    pair = input(str('Enter a letter pair [qq quits]: ').upper())
    if pair == 'QQ':
        break
    else:
        plugboard.append(pair)

    print(plugboard)

print(plugboard)
