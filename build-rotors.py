#!/usr/bin/env python3
"""build-rotors.py file"""
import random
import os


def build_rotor(rotor_list):
    letter_list = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    while len(rotor_list) < 26:
        rotor_letter = random.choice(letter_list)
        if rotor_letter not in rotor_list:
            rotor_list.append(rotor_letter)


def shuffle_rotor(rotor, n=17576):
    for _ in range(n):
        random.shuffle(rotor)


def check_for_rotor_file(filename):
    if os.path.isfile(filename):
        os.unlink(filename)


def write_rotor_file(rotor):
    try:
        with open("rotors.txt", "a") as write:
            write.write(str(rotor))
            write.write("\n")
    except FileNotFoundError as fnfe:
        print(f"ERROR: {fnfe}")


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

    shuffle_rotor(rotor_i, 1)
    shuffle_rotor(rotor_ii, 1)
    shuffle_rotor(rotor_iii, 1)
    shuffle_rotor(rotor_iv, 1)
    shuffle_rotor(rotor_v, 1)

    filepath = "path_to_file"
    check_for_rotor_file(filepath)

    write_rotor_file(rotor_i)
    write_rotor_file(rotor_ii)
    write_rotor_file(rotor_iii)
    write_rotor_file(rotor_iv)
    write_rotor_file(rotor_v)

    # print(rotor_i)
    # print(rotor_ii)
    # print(rotor_iii)
    # print(rotor_iv)
    # print(rotor_v)


if __name__ == "__main__":
    main()
