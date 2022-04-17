#!/usr/bin/env python3

# fmt: off
rotor_in = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
rotor_out = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
# fmt: on


def get_key() -> str:
    """Asks user for an n-letterd key used for encoding

    return:
        key [str]: String representation of the entered key
    """
    key: str = ""
    while True:
        key = str(input("Enter your key: ").upper())
        if len(key) == 0:
            print("Please enter a key of letters longer than 0\n")
            continue
        elif len(key) > 0:
            break
    return key


def set_key_letter(letter: str) -> None:
    """Removes and places, the first letter in the output
    rotor until the first letter of the output rotor is
    equal to the first letter of the key.
    """
    while rotor_out[0] != letter:
        temp_letter = rotor_out.pop(0)
        rotor_out.append(temp_letter)


def get_message() -> str:
    """Gets the users message and retruns it as a string

    return:
        message [str]: Users inputted message
    """
    message: str = ""
    while len(message) == 0:
        message: str = str(input("Enter your message: ").upper())
        if len(message) < 1:
            print("Please enter a message longer than 0\n")
    return message


def encode_message(message: str, key: str):
    """Encodeds users message

    return:
        ecoded_message [list: str]: Users message encoded
    """
    key_list = list(key)
    encoded_message = []
    index: int = 0
    while True:
        while rotor_out[0] != key_list[0]:
            temp_letter = rotor_out.pop(0)
            rotor_out.append(temp_letter)

        temp_letter = key_list.pop(0)
        key_list.append(temp_letter)
        input_index = rotor_in.index(message[index])
        encoded_message.append(rotor_out[input_index])

        index += 1
        if index == len(message) - 1:
            break

    return encoded_message


def encode_letter(key: str) -> None:
    """Encodes a single inputted letter and prints the encoded
    output along with the rotor positions used to encode the letter.

    parameter:
        key [str]: User passed key string used to set the 0'th index
            of the output rotor
    """
    key_list = list(key)
    while True:
        letter: str = str(input("Enter a letter: ").upper())

        while rotor_out[0] != key_list[0]:
            temp_letter = rotor_out.pop(0)
            rotor_out.append(temp_letter)

        temp_letter = key_list.pop(0)
        key_list.append(temp_letter)
        input_index = rotor_in.index(letter)
        encoded_letter = rotor_out[input_index]

        print_rotors()
        print(encoded_letter)


def print_rotors() -> None:
    """Prints the input rotor and the output rotor each on
    a single line
    """
    [print(letter, end=" ") for letter in rotor_in]
    print()
    [print(letter, end=" ") for letter in rotor_out]
    print()


user_key: str = get_key()
encode_letter(user_key)
# user_message: str = get_message()
# user_encoded_message = encode_message(user_message, user_key)
# print_rotors()

# print(user_key)
# print(rotor_in)
# print(rotor_out)
# print(user_message)
# [print(letter, end="") for letter in user_encoded_message]
print()
