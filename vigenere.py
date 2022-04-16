#!/usr/bin/env python3

rotor_in = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
rotor_out = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]


def get_key() -> str:
    """Asks user for an n-letterd key used for encoding

    return:
        key [str]: String representation of the entered key
    """
    key = ""
    while True:
        key: str = str(input("Enter your key: ").upper())
        if len(key) == 0:
            print("Please enter a key of letters longer than 0\n")
            continue
        elif len(key) > 0:
            break
    return key


def set_key_letter(letter: str) -> None:
    """Removes and places, the first letter in the output rotor until the
    first letter of the output rotor is equal to the first letter of the key.
    """
    while rotor_out[0] != letter:
        temp_letter = rotor_out.pop(0)
        rotor_out.append(temp_letter)


def get_message():
    """
    """
    message = ""
    while message len(message) == 0:
        message: str = str(input("Enter your message: ").upper())
        if len(message) < 1:


user_key: str = get_key()
set_key_letter(user_key[0])

print(user_key)
print(rotor_in)
print(rotor_out)

