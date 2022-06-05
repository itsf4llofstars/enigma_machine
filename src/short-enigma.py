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
from collections import deque
from sys import exit


# fmt: off
class ShortEnigma:
    def __init__(self, key):
        self.in_out = deque(['A', 'B', 'C', 'D', 'E', 'F'])

        self.rotor1_in = deque(['C', 'E', 'D', 'F', 'B', 'A'])
        self.rotor1_out = deque(['A', 'B', 'C', 'D', 'E', 'F'])

        self.rotor2_in = deque(['F', 'E', 'C', 'A', 'D', 'B'])
        self.rotor2_out = deque(['A', 'B', 'C', 'D', 'E', 'F'])

        self.rotor3_in = deque(['D', 'A', 'F', 'E', 'C', 'B'])
        self.rotor3_out = deque(['A', 'B', 'C', 'D', 'E', 'F'])

        self.reflector = ['K', 'E', 'B', 'E', 'K', 'B']

        self.rotors = {
            "left_in": self.rotor1_in,
            "left_out": self.rotor1_out,
            "center_in": self.rotor2_in,
            "center_out": self.rotor2_out,
            "right_in": self.rotor3_in,
            "right_out": self.rotor3_out,
        }

        self.key = key.upper()

    def input_output(self):
        print("Input/Output")
        [print(letter, end=" ") for letter in self.in_out]
        print("\n")

    def left_rotor(self):
        print("Left")
        [print(letter, end=" ") for letter in self.rotors["left_in"]]
        print()
        [print(letter, end=" ") for letter in self.rotors["left_out"]]
        print("\n")

    def right_rotor(self):
        print("Right")
        [print(letter, end=" ") for letter in self.rotors["right_in"]]
        print()
        [print(letter, end=" ") for letter in self.rotors["right_out"]]
        print("\n")

    def center_rotor(self):
        print("Center")
        [print(letter, end=" ") for letter in self.rotors["center_in"]]
        print()
        [print(letter, end=" ") for letter in self.rotors["center_out"]]
        print("\n")

    def show_reflector(self):
        [print(letter, end=" ") for letter in self.reflector]
        print("\n")

    def set_key(self):
        while self.rotors["left_out"][0] != self.key[0]:
            deque.rotate(self.rotors["left_in"])
            deque.rotate(self.rotors["left_out"])

        while self.rotors["center_out"][0] != self.key[1]:
            deque.rotate(self.rotors["center_in"])
            deque.rotate(self.rotors["center_out"])

        while self.rotors["right_out"][0] != self.key[2]:
            deque.rotate(self.rotors["right_in"])
            deque.rotate(self.rotors["right_out"])

    def rotate_left(self):
        deque.rotate(self.rotors["left_in"], -1)
        deque.rotate(self.rotors["left_out"], -1)

    def rotate_center(self):
        deque.rotate(self.rotors["center_in"], -1)
        deque.rotate(self.rotors["center_out"], -1)

    def rotate_right(self):
        deque.rotate(self.rotors["right_in"], -1)
        deque.rotate(self.rotors["right_out"], -1)

    def get_index_of_letter(self, rotor, letter):
        return rotor.index(letter)

    def get_letter_of_index(self, rotor, index):
        return rotor[index]

    def get_letter_at_index(self, rotor, index):
        return rotor[index]

    def find_rotor_out_info(self, rotor, letter, index):
        while rotor[index] != letter:
            index = (index + 1) % 6
        return index, rotor[index]

    def get_reflector_out_index(self, in_index, reflector_in_letter):
        in_index = (1 + in_index) % 6
        while self.reflector[in_index] != reflector_in_letter:
            in_index = (1 + in_index) % 6
        return in_index
# fmt: on


def main():
    enigma = ShortEnigma("ceb")
    enigma.set_key()

    """Going To The Reflector"""
    while True:
        input_letter = input("Letter [qq to quit]: ")
        # input_letter = input("")
        enigma.rotate_right()

        if enigma.rotors["right_out"][0] == "C":
            enigma.rotate_center()
            if enigma.rotors["center_out"][0] == "E":
                enigma.rotate_left()

        if input_letter.upper() == "QQ":
            break

        index = enigma.get_index_of_letter(enigma.in_out, input_letter.upper())

        # Right rotor
        letter = enigma.get_letter_at_index(enigma.rotors["right_in"], index)
        index = enigma.get_index_of_letter(enigma.rotors["right_out"], letter)

        # Center rotor
        letter = enigma.get_letter_at_index(enigma.rotors["center_in"], index)
        index = enigma.get_index_of_letter(enigma.rotors["center_out"], letter)

        # Left rotor
        letter = enigma.get_letter_at_index(enigma.rotors["left_in"], index)
        index = enigma.get_index_of_letter(enigma.rotors["left_out"], letter)

        """Inside the Reflector"""
        # Reflector
        reflector_letter = enigma.get_letter_at_index(enigma.reflector, index)
        reflector_index = index

        # Reflector output index
        reflector_output_index = enigma.get_reflector_out_index(
            reflector_index, reflector_letter
        )

        """Going To The Output"""
        letter = enigma.get_letter_at_index(
            enigma.rotors["left_out"], reflector_output_index
        )
        index = enigma.get_index_of_letter(enigma.rotors["left_in"], letter)

        letter = enigma.get_letter_at_index(enigma.rotors["center_out"], index)
        index = enigma.get_index_of_letter(enigma.rotors["center_in"], letter)

        letter = enigma.get_letter_at_index(enigma.rotors["right_out"], index)
        index = enigma.get_index_of_letter(enigma.rotors["right_in"], letter)

        encoded_letter = enigma.get_letter_at_index(enigma.in_out, index)

        print(f"{input_letter} --> {encoded_letter}")


if __name__ == "__main__":
    from os import system

    # system("clear")
    main()
