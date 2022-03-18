#!/usr/bin/env python3
from collections import deque


class ShortEnigma:
    def __init__(self, key):
        self.in_out = deque(['A', 'B', 'C', 'D', 'E'])

        self.rotor_1_in = deque(['V', 'Z', 'W', 'O', 'X', 'V', 'Z', 'W', 'O', 'X'])
        self.rotor_1_ou = deque(['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E'])
        self.rotor_2_in = deque(['E', 'M', 'L', 'G', 'D', 'E', 'M', 'L', 'G', 'D'])
        self.rotor_2_ou = deque(['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E'])
        self.rotor_3_in = deque(['J', 'H', 'L', 'F', 'T', 'J', 'H', 'L', 'F', 'T'])
        self.rotor_3_ou = deque(['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E'])

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

    def set_key(self):
        while self.rotors["left_ou"][0] != self.key[0]:
            deque.rotate(self.rotors["left_in"])
            deque.rotate(self.rotors["left_ou"])

        while self.rotors["center_ou"][0] != self.key[1]:
            deque.rotate(self.rotors["center_in"])
            deque.rotate(self.rotors["center_ou"])

        while self.rotors["right_ou"][0] != self.key[2]:
            deque.rotate(self.rotors["right_in"])
            deque.rotate(self.rotors["right_ou"])

    def rotate_left(self):
        deque.rotate(self.rotors["left_in"], -1)
        deque.rotate(self.rotors["left_ou"], -1)

    def rotate_center(self):
        deque.rotate(self.rotors["center_in"], -1)
        deque.rotate(self.rotors["center_ou"], -1)

    def rotate_right(self):
        deque.rotate(self.rotors["right_in"], -1)
        deque.rotate(self.rotors["right_ou"], -1)


def main():
    enigma = ShortEnigma("ceb")

    enigma.right_rotor()
    enigma.center_rotor()
    enigma.left_rotor()

    enigma.set_key()

    enigma.right_rotor()
    enigma.center_rotor()
    enigma.left_rotor()

    enigma.rotate_right()
    enigma.right_rotor()


if __name__ == "__main__":
    from os import system
    system("clear")
    main()
