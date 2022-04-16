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


def get_message() -> str:
    """Gets the users message and retruns it as a string

    return:
        message [str]: Users inputted message
    """
    message = ""
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
    index = 0
    while index < len(message):
        while rotor_out[0] != key_list[0]:
            temp = rotor_out.pop(0)
            rotor_out.append(temp)
        letter_index = rotor_in.index(message[index])
        encoded_letter = rotor_out[letter_index]
        encoded_message.append(encoded_letter)
        index += 1
    return encoded_message


user_key: str = get_key()
# set_key_letter(user_key[0])
user_message: str = get_message()
user_encoded_message = encode_message(user_message, user_key)

print(user_key)
print(rotor_in)
print(rotor_out)
print(user_message)
[print(letter, end="") for letter in user_encoded_message]
print()

