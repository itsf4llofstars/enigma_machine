#!/usr/bin/env python3
from collections import deque


class PaperEnigma:
    def __init__(self, days_rotors, key):
        self.in_out = deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])

        self.rotor_i_out = deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
        self.rotor_i_in = deque(["E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P", "A", "I", "B", "R", "C", "J", "E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P", "A", "I", "B", "R", "C", "J"])

        self.rotor_ii_out = deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
        self.rotor_ii_in = deque(["A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z", "N", "P", "Y", "F", "V", "O", "E", "A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z", "N", "P", "Y", "F", "V", "O", "E"])

        self.rotor_iii_out = deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
        self.rotor_iii_in = deque(["B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G", "A", "K", "M", "U", "S", "Q", "O", "B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G", "A", "K", "M", "U", "S", "Q", "O"])

        self.reflector = deque(["A", "B", "C", "D", "E", "F", "G", "D", "I", "J", "K", "G", "M", "K", "M", "I", "E", "B", "F", "T", "C", "V", "V", "J", "A", "T"])

        self.rotors = {
            "left_in": deque(["E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P", "A", "I", "B", "R", "C", "J", "E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P", "A", "I", "B", "R", "C", "J"]),
            "left_out": deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]),
            "center_in": deque(["A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z", "N", "P", "Y", "F", "V", "O", "E", "A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z", "N", "P", "Y", "F", "V", "O", "E"]),
            "center_out": deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]),
            "right_in": deque(["B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G", "A", "K", "M", "U", "S", "Q", "O", "B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G", "A", "K", "M", "U", "S", "Q", "O"]),
            "right_out": deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]),
        }

        self.days_rotors = days_rotors
        self.key = key.upper()

    def __repr__(self):
        rotors_string = f"{self.rotors['left_in']}\n{self.rotors['left_out']}\n\n{self.rotors['center_in']}\n{self.rotors['center_out']}\n\n{self.rotors['right_in']}\n{self.rotors['right_out']}"
        return rotors_string

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

    def find_rotor_out_info(self, rotor, letter, index):
        while rotor[index] != letter:
            index = (index + 1) % 26

        return index, rotor[index]


def main():
    enigma = PaperEnigma(["I", "II", "III"], 'mck')
    enigma.set_key()
    enigma.print_right()

    enigma.rotate_right()
    enigma.print_right()
    enigma.print_center()
    enigma.print_left()

    print("-" * 80)

    letter = "e"
    index = enigma.get_index_of_letter(enigma.in_out, letter.upper())
    print(f"Input Letter: {letter.upper()} index: {index}")

    letter = enigma.get_letter_at_index(enigma.rotors["right_in"], index)
    print(f"Right rotor input letter: {letter}")
    rotor_out_info = enigma.find_rotor_out_info(enigma.rotors["right_out"], letter, index)
    index, letter = rotor_out_info
    print(f"Right rotor output index: {index}\n")

    # Operating on the center rotor
    letter = enigma.get_letter_at_index(enigma.rotors["center_in"], index)
    print(f"Center rotor input letter: {letter}")
    rotor_out_info = enigma.find_rotor_out_info(enigma.rotors["center_out"], letter, index)
    index, letter = rotor_out_info
    print(f"Center rotor output index: {index}\n")

    # Operating on the left rotor
    letter = enigma.get_letter_at_index(enigma.rotors["left_in"], index)
    print(f"Left rotor input letter: {letter}")
    rotor_out_info = enigma.find_rotor_out_info(enigma.rotors["left_out"], letter, index)
    index, letter = rotor_out_info
    print(f"Left rotor output index: {index}\n")

if __name__ == "__main__":
    import os
    os.system("clear")
    main()
