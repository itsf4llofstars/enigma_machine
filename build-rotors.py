#!/usr/bin/env python3
"""
Encodes and Decodes entered text in the manner an Enigma Macine does
Copyright (C) 2022  itsf4llofstars
https://www/github.com/itsf4llofstars Email: irooted4hal@mailfence.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

enigma_machine  Copyright (C) 2022  itsf4llofstars
This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
This is free software, and you are welcome to redistribute it
under certain conditions; type `show c' for details.
"""
import os
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

    filepath = "rotors.txt"  # Should be in the working directory
    check_for_rotor_file(filepath)

    write_rotor_file(rotor_i)
    write_rotor_file(rotor_ii)
    write_rotor_file(rotor_iii)
    write_rotor_file(rotor_iv)
    write_rotor_file(rotor_v)

    print("New Rotors built")

    # print(rotor_i)
    # print(rotor_ii)
    # print(rotor_iii)
    # print(rotor_iv)
    # print(rotor_v)


if __name__ == "__main__":
    main()
