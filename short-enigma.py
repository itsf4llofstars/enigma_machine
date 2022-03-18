#!/usr/bin/env python3
from collections import deque


class ShortEnigma:
    def __init__(self, key):
        self.in_out = deque(['A', 'B', 'C', 'D', 'E', 'F'])

        self.rotor_1_in = deque(['C', 'E', 'D', 'F', 'B', 'A'])
        self.rotor_1_ou = deque(['A', 'B', 'C', 'D', 'E', 'F'])

        self.rotor_2_in = deque(['F', 'E', 'C', 'A', 'D', 'B'])
        self.rotor_2_ou = deque(['A', 'B', 'C', 'D', 'E', 'F'])

        self.rotor_3_in = deque(['D', 'A', 'F', 'E', 'C', 'B'])
        self.rotor_3_ou = deque(['A', 'B', 'C', 'D', 'E', 'F'])

        self.reflector = ['K', 'E', 'B', 'E', 'K', 'B']

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
        print("Left")
        [print(letter, end=" ") for letter in self.rotors["left_in"]]
        print()
        [print(letter, end=" ") for letter in self.rotors["left_ou"]]
        print("\n")

    def right_rotor(self):
        print("Right")
        [print(letter, end=" ") for letter in self.rotors["right_in"]]
        print()
        [print(letter, end=" ") for letter in self.rotors["right_ou"]]
        print("\n")

    def center_rotor(self):
        print("Center")
        [print(letter, end=" ") for letter in self.rotors["center_in"]]
        print()
        [print(letter, end=" ") for letter in self.rotors["center_ou"]]
        print("\n")

    def show_reflector(self):
        [print(letter, end=" ") for letter in self.reflector]
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

    def get_index_of_letter(self, rotor, letter):
        return rotor.index(letter)

    def get_letter_at_index(self, rotor, index):
        return rotor[index]

    def find_rotor_out_info(self, rotor, letter, index):
        while rotor[index] != letter:
            index = (index + 1) % 6
        return index, rotor[index]


def main():
    enigma = ShortEnigma("ceb")
    enigma.set_key()

    enigma.right_rotor()
    enigma.rotate_right()

    enigma.right_rotor()
    enigma.center_rotor()
    enigma.left_rotor()
    enigma.show_reflector()

    letter = "b"
    index = enigma.get_index_of_letter(enigma.in_out, letter.upper())
    print(f"Input Letter: {letter.upper()} index: {index}")

    # Right rotor
    letter = enigma.get_letter_at_index(enigma.rotors["right_in"], index)
    print(f"Right rotor Input Letter: {letter}")
    rotor_out_info = enigma.find_rotor_out_info(enigma.rotors["right_ou"], letter, index)
    index, letter = rotor_out_info
    print(f"Right rotor output index: {index}")

    # Center rotor
    letter = enigma.get_letter_at_index(enigma.rotors["center_in"], index)
    print(f"Center rotor Input Letter: {letter}")
    rotor_out_info = enigma.find_rotor_out_info(enigma.rotors["center_ou"], letter, index)
    index, letter = rotor_out_info
    print(f"Center rotor output index: {index}")

    # Left rotor
    letter = enigma.get_letter_at_index(enigma.rotors["left_in"], index)
    print(f"Left rotor Input Letter: {letter}")
    rotor_out_info = enigma.find_rotor_out_info(enigma.rotors["left_ou"], letter, index)
    index, letter = rotor_out_info
    print(f"Left rotor output index: {index}")

    # Reflector
    reflector_letter = enigma.get_letter_at_index(enigma.reflector, index)
    print(f"Reflector Letter: {reflector_letter}")


if __name__ == "__main__":
    from os import system
    system("clear")
    main()
