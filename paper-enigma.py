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
            ["left"]: [self.in_out,[]],
            ["center"]: [self.in_out, []],
            ["right"]: [self.in_out, []],
        }

        self.days_rotors = days_rotors

    def __repr__(self):
        rotors_string = f"{self.rotors['left'][0]}\n{self.rotors['left'][1]}\n\n{self.rotors['center'][0]}\n{self.rotors['center'][1]}\n\n{self.rotors['right'][0]}\n{self.rotors['right'][1]}"

    def set_rotors(self):
        if days_rotors[0] == "I":
            self.rotors["left"][1] = self.rotor_i_in
        elif days_rotors[0] == "II":
            self.rotors["left"][1] = self.rotor_ii_in
        else:
            self.rotors["left"][1] = self.rotor_iii_in

        if days_rotors[1] == "I":
            self.rotors["center"][1] = self.rotor_i_in
        elif days_rotors[1] == "II":
            self.rotors["center"][1] = self.rotor_ii_in
        else:
            self.rotors["center"][1] = self.rotor_iii_in

        if days_rotors[2] == "I":
            self.rotors["right"][1] = self.rotor_i_in
        elif days_rotors[2] == "II":
            self.rotors["right"][1] = self.rotor_ii_in
        else:
            self.rotors["right"][1] = self.rotor_iii_in


def main():
    enigma = PaperEnigma(["I", "II", "III"])
    enigma.set_rotors()
    print(enigma)


if __name__ == "__main__":
    main()
