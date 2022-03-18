#!/usr/bin/env python3
from collections import deque


class ShortEnigma:
    def __init__(self, key):
        self.in_out = deque(['A', 'B', 'C', 'D', 'E'])

        self.rotor_1_in = deque(['V', 'Z', 'W', 'O', 'X'])
        self.rotor_1_ou = deque(['A', 'B', 'C', 'D', 'E'])
        self.rotor_2_in = deque(['E', 'M', 'L', 'G', 'D'])
        self.rotor_2_ou = deque(['A', 'B', 'C', 'D', 'E'])
        self.rotor_3_in = deque(['J', 'H', 'L', 'F', 'T'])
        self.rotor_3_ou = deque(['A', 'B', 'C', 'D', 'E'])

        self.rotors = {
            "left_in": self.rotor_1_in,
            "left_ou": self.rotor_1_ou,
            "center_in": self.rotor_2_in,
            "center_ou": self.rotor_2_ou,
            "right_in": self.rotor_3_in,
            "right_ou": self.rotor_3_ou,
        }

        self.key = key.upper()

    def left_rotor(self):
        [print(letter, end=" ") for letter in self.rotors["left_in"]]
        print()
        [print(letter, end=" ") for letter in self.rotors["left_ou"]]
        print("\n")

    def right_rotor(self):
        [print(letter, end=" ") for letter in self.rotors["right_in"]]
        print()
        [print(letter, end=" ") for letter in self.rotors["right_ou"]]
        print("\n")

    def center_rotor(self):
        [print(letter, end=" ") for letter in self.rotors["center_in"]]
        print()
        [print(letter, end=" ") for letter in self.rotors["center_ou"]]
        print("\n")


def main():
    enigma = ShortEnigma("ceb")
    enigma.right_rotor()
    enigma.center_rotor()
    enigma.left_rotor()


if __name__ == "__main__":
    from os import system
    system("clear")
    main()
