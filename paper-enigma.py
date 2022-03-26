#!/usr/bin/env python3
from collections import deque


class PaperEnigma:
    def __init__(self, days_rotors, key):
        self.in_out = deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])

        self.rotor1_in = deque(["E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P", "A", "I", "B", "R", "C", "J"])
        self.rotor1_out = deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])

        self.rotor2_in = deque(["A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z", "N", "P", "Y", "F", "V", "O", "E"])
        self.rotor2_out = deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])

        self.rotor3_in = deque(["B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G", "A", "K", "M", "U", "S", "Q", "O"])
        self.rotor3_out = deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])

        self.reflector = deque(["A", "B", "C", "D", "E", "F", "G", "D", "I", "J", "K", "G", "M", "K", "M", "I", "E", "B", "F", "T", "C", "V", "V", "J", "A", "T"])

        self.rotors = {
            "left_in": deque(["E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P", "A", "I", "B", "R", "C", "J"]),
            "left_out": deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]),
            "center_in": deque(["A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z", "N", "P", "Y", "F", "V", "O", "E"]),
            "center_out": deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]),
            "right_in": deque(["B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G", "A", "K", "M", "U", "S", "Q", "O"]),
            "right_out": deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]),
        }

        self.days_rotors = days_rotors
        self.key = key.upper()

    def __repr__(self):
        return f'{self.in_out}\n{self.rotors["right_in"]}\n{self.rotors["right_out"]}\n{self.rotors["center_in"]}\n{self.rotors["center_out"]}\n{self.rotors["left_in"]}\n{self.rotors["left_out"]}'

    def show_rotor(self, rotor):
        [print(letter, end="") for letter in rotor]

    def print_left(self):
        print("Left Rotor")
        for letter in self.rotors["left_in"]:
            print(letter, end=" ")
        print()
        for letter in self.rotors["left_out"]:
            print(letter, end=" ")
        print()
        print()

    def print_center(self):
        print("Center Rotor")
        for letter in self.rotors["center_in"]:
            print(letter, end=" ")
        print()
        for letter in self.rotors["center_out"]:
            print(letter, end=" ")
        print()
        print()

    def print_right(self):
        print("Right Rotor")
        for letter in self.rotors["right_in"]:
            print(letter, end=" ")
        print()
        for letter in self.rotors["right_out"]:
            print(letter, end=" ")
        print()
        print()

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

    def rotate_left(self, n=-1):
        deque.rotate(self.rotors["left_in"], n)
        deque.rotate(self.rotors["left_out"], n)

    def rotate_center(self, n=-1):
        deque.rotate(self.rotors["center_in"], n)
        deque.rotate(self.rotors["center_out"], n)

    def rotate_right(self, n=-1):
        deque.rotate(self.rotors["right_in"], n)
        deque.rotate(self.rotors["right_out"], n)

    def get_index_of_letter(self, rotor, letter):
        return rotor.index(letter)

    def get_letter_at_index(self, rotor, index):
        return rotor[index]


def main():
    enigma = PaperEnigma(["I", "II", "III"], 'mck')
    enigma.show_rotor(enigma.in_out)
    enigma.set_key()

    enigma.rotate_right()

    print("\n")
    enigma.show_rotor(enigma.rotors["right_in"])
    print()
    enigma.show_rotor(enigma.rotors["right_out"])
    print("\n")
    enigma.show_rotor(enigma.rotors["center_in"])
    print()
    enigma.show_rotor(enigma.rotors["center_out"])
    print("\n")
    enigma.show_rotor(enigma.rotors["left_in"])
    print()
    enigma.show_rotor(enigma.rotors["left_out"])
    print("\n")

    letter = "e"
    print(f"User Input Letter: {letter.upper()}")
    index = enigma.get_index_of_letter(enigma.in_out, letter.upper())
    print(f"Input Letter: {letter.upper()} index of input letter: {index}")

    letter = enigma.get_letter_at_index(enigma.rotors["right_in"], index)
    print(f"Right rotor input letter: {letter} Right rotor input index: {index}")
    index = enigma.get_index_of_letter(enigma.rotors["right_out"], letter)
    print(f"Right rotor output letter: {letter} index of output letter: {index}")

    ## Operating on the center rotor
    letter = enigma.get_letter_at_index(enigma.rotors["center_in"], index)
    print(f"Center rotor input letter: {letter} Center rotor input index: {index}")
    index = enigma.get_index_of_letter(enigma.rotors["center_out"], letter)
    print(f"Center rotor output letter: {letter} index of output letter: {index}")

    ## Operating on the left rotor
    letter = enigma.get_letter_at_index(enigma.rotors["left_in"], index)
    print(f"Left rotor input letter: {letter} Left rotor input index: {index}")
    index = enigma.get_index_of_letter(enigma.rotors["left_out"], letter)
    print(f"Left rotor output letter: {letter} index of output letter: {index}")

if __name__ == "__main__":
    import os
    os.system("clear")
    main()
