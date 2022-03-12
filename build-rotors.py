#!/usr/bin/env python3
"""create-rotors.py file"""
import random


def build_rotor(rotor_list):
    letter_list = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    while len(rotor_list) < 26:
        rotor_letter = random.choice(letter_list)
        if rotor_letter not in rotor_list:
            rotor_list.append(rotor_letter)


def shuffle_rotor(rotor, n = 10000):
    for _ in range(n):
        random.shuffle(rotor)


def main():
    rotor_i = []
    rotor_ii = []
    rotor_iii = []
    rotor_iv = []
    rotor_v = []

    build_rotor(rotor_i)
    build_rotor(rotor_ii)
    build_rotor(rotor_iii)
    build_rotor(rotor_iv)
    build_rotor(rotor_v)

    shuffle_rotor(rotor_i)
    shuffle_rotor(rotor_ii)
    shuffle_rotor(rotor_iii)
    shuffle_rotor(rotor_iv)
    shuffle_rotor(rotor_v)

    print(rotor_i)
    print(rotor_ii)
    print(rotor_iii)
    print(rotor_iv)
    print(rotor_v)


if __name__ == "__main__":
    main()
