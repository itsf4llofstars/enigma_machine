#!/usr/bin/env python3
"""Plug Board Test Script"""

letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

plugboard = []
plugstring = ''

in_letter = 'C'

while True:
    pair = input(str('Enter a letter pair [qq quits]: ')).upper()
    if len(pair) != 2:
        print('len error')
        continue

    if pair == 'QQ':
        break

    if pair[0] in plugstring or pair[1] in plugstring:
        print('Double letter error')
        del plugboard
        del plugstring
        break

    plugstring += pair
    plugboard.append(pair)

    if len(plugboard) == 13:
        break

print(plugboard)
print(plugstring)
print()
print(in_letter)

for one in plugboard:
    if in_letter in one and in_letter == one[0]:
        in_letter = one[1]
    elif in_letter in one and in_letter == one[1]:
        in_letter = one[0]

print(in_letter)
