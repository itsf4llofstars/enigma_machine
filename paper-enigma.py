#!/usr/bin/env python3
from collections import deque


class PaperEnigma:
    def __init__(self, days_rotors):
        self.in_out = deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])

        self.rotor_i_out = deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
        self.rotor_i_in = deque(["E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P", "A", "I", "B", "R", "C", "J", "E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P", "A", "I", "B", "R", "C", "J"])

        self.rotor_ii_out = deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
        self.rotor_ii_in = deque(["A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z", "N", "P", "Y", "F", "V", "O", "E", "A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z", "N", "P", "Y", "F", "V", "O", "E"])

        self.rotor_iii_out = deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
        self.rotor_iii_in = deque(["B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G", "A", "K", "M", "U", "S", "Q", "O", "B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G", "A", "K", "M", "U", "S", "Q", "O"])

        self.reflector = deque(["A", "B", "C", "D", "E", "F", "G", "D", "I", "J", "K", "G", "M", "K", "M", "I", "E", "B", "F", "T", "C", "V", "V", "J", "A", "T"])

        self.rotors = {
            "left_in": deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]),
            "left_out": deque(["E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P", "A", "I", "B", "R", "C", "J", "E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P", "A", "I", "B", "R", "C", "J"]),
            "center_in": deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]),
            "center_out": deque(["A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z", "N", "P", "Y", "F", "V", "O", "E", "A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z", "N", "P", "Y", "F", "V", "O", "E"]),
            "right_in": deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]),
            "right_out": deque(["B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G", "A", "K", "M", "U", "S", "Q", "O", "B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G", "A", "K", "M", "U", "S", "Q", "O"]),
        }

        self.days_rotors = days_rotors

    def __repr__(self):
        rotors_string = f"{self.rotors['left_in']}\n{self.rotors['left_out']}\n\n{self.rotors['center_in']}\n{self.rotors['center_out']}\n\n{self.rotors['right_in']}\n{self.rotors['right_out']}"
        return rotors_string

    def print_left(self):
        for letter in self.rotors["left_in"]:
            print(letter, end="")
        print()
        for letter in self.rotors["left_out"]:
            print(letter, end="")
        print()
        print()

    def print_center(self):
        for letter in self.rotors["center_in"]:
            print(letter, end="")
        print()
        for letter in self.rotors["center_out"]:
            print(letter, end="")
        print()
        print()

    def print_right(self):
        for letter in self.rotors["right_in"]:
            print(letter, end="")
        print()
        for letter in self.rotors["right_out"]:
            print(letter, end="")
        print()
        print()
        
    def set_rotors(self):
        if self.days_rotors[0] == "I":
            self.rotors["left"][1] = self.rotor_i_in
        elif self.days_rotors[0] == "II":
            self.rotors["left"][1] = self.rotor_ii_in
        else:
            self.rotors["left"][1] = self.rotor_iii_in

        if self.days_rotors[1] == "I":
            self.rotors["center"][1] = self.rotor_i_in
        elif self.days_rotors[1] == "II":
            self.rotors["center"][1] = self.rotor_ii_in
        else:
            self.rotors["center"][1] = self.rotor_iii_in

        if self.days_rotors[2] == "I":
            self.rotors["right"][1] = self.rotor_i_in
        elif self.days_rotors[2] == "II":
            self.rotors["right"][1] = self.rotor_ii_in
        else:
            self.rotors["right"][1] = self.rotor_iii_in

    def rotate_left(self, n=-1):
        deque.rotate(self.rotors["left_in"], n)
        deque.rotate(self.rotors["left_out"], n)

    def rotate_center(self, n=-1):
        deque.rotate(self.rotors["center_in"], n)
        deque.rotate(self.rotors["center_out"], n)

    def rotate_right(self, n=-1):
        deque.rotate(self.rotors["right_in"], n)
        deque.rotate(self.rotors["right_out"], n)


def main():
    enigma = PaperEnigma(["I", "II", "III"])
    enigma.print_left()
    enigma.print_center()
    enigma.print_right()
    print("-" * 80)

    enigma.rotate_left()
    enigma.rotate_center()
    enigma.rotate_right()

    enigma.print_left()
    enigma.print_center()
    enigma.print_right()
    print("-" * 80)


if __name__ == "__main__":
    main()
