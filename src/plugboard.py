"""Plug Board Test Script"""

# fmt: off
letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
# fmt: on

plugboard = []
plugstring = ''

in_letter = 'C'

def main():
    global letters, plugboard, plugstring, in_letter
    while True:
        pair = input(str('Enter a letter pair [qq quits]: ')).upper()
        if len(pair) != 2:
            print('len error')
            continue

        if pair == 'QQ':
            break
        elif pair[0] in plugstring or pair[1] in plugstring or pair[0] == pair[1]:
            print('Double letter error')
            exit(1)
        else:
            plugstring += pair
            plugboard.append(pair)

        if len(plugboard) == 13:
            break

    print(plugboard)
    print(plugstring)
    print()
    print(in_letter)

    for letter_pair in plugboard:
        if in_letter == letter_pair[0]:
            in_letter = letter_pair[1]


    print(in_letter)
