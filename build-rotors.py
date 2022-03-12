#!/usr/bin/env python3
"""create-rotors.py file"""
import random


letter_list = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]


def build_rotor(rotor_list):
    while len(rotor_list) < 26:
        rotor_letter = random.choice(letter_list)
        if rotor_letter in rotor_list:
            continue
        elif rotor_letter not in rotor_list:
            rotor_list.append(rotor_letter)


def main():
    rotor_i = []
    build_rotor(rotor_i)


if __name__ == "__main__":
    main()
