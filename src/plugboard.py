"""Plug Board Test Script"""

# fmt: off
letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
# fmt: on

plugboard = []
plugstring = ""

in_letter = "C"
out_letter = "H"


def main():
    global letters, plugboard, plugstring, in_letter, out_letter

    while True:
        pair = input(str("Enter a letter pair [qq quits]: ")).upper()
        if len(pair) != 2:
            print("len error")
            continue

        if pair == "QQ":
            break
        elif pair[0] in plugstring or pair[1] in plugstring or pair[0] == pair[1]:
            print("Double letter error")
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
    print(out_letter)

    # Maps an input letter to it's coresponding output plugboard letter
    for letter_pair in plugboard:
        if in_letter == letter_pair[0]:
            in_letter = letter_pair[1]

    # Maps an output letter to it's coresponding input plugboard letter
    for letter_pair in plugboard:
        if out_letter == letter_pair[1]:
            out_letter = letter_pair[0]

    print(in_letter)
    print(out_letter)


if __name__ == "__main__":
    import sys

    sys.exit(main())
