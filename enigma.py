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


class Enigma:
    """Class model of the German Enigma Test Encoding machine
    """
    def __init__(self, selected_rotors, rings: str, key: str) -> None:
        self.keyboard = deque([
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
        ])

        # May not be needed
        self.rotor1 = deque([
            "U", "L", "R", "X", "C", "Q", "O", "K", "G", "N", "J", "A", "F",
            "I", "H", "Z", "W", "S", "E", "Y", "M", "P", "D", "T", "B", "V"
        ])
        self.rotor2 = deque([
            "Y", "T", "K", "F", "J", "M", "D", "Q", "C", "H", "X", "R", "P",
            "E", "L", "W", "Z", "N", "V", "I", "S", "O", "G", "B", "U", "A"
        ])
        self.rotor3 = deque([
            "P", "X", "E", "Z", "B", "W", "Y", "L", "F", "G", "U", "C", "D",
            "S", "I", "R", "J", "O", "M", "A", "K", "H", "T", "N", "V", "Q"
        ])
        self.rotor4 = deque([
            "R", "P", "X", "G", "K", "S", "B", "Y", "E", "C", "J", "I", "H",
            "U", "T", "N", "D", "M", "F", "Q", "A", "V", "L", "Z", "O", "W"
        ])
        self.rotor5 = deque([
            "S", "M", "I", "R", "X", "P", "J", "U", "O", "A", "V", "D", "Q",
            "F", "L", "C", "Z", "K", "T", "W", "G", "E", "N", "B", "H", "Y"
        ])

        self.stored_rotors = {
            "I": deque(["U", "L", "R", "X", "C", "Q", "O", "K", "G", "N", "J", "A", "F", "I", "H", "Z", "W", "S", "E", "Y", "M", "P", "D", "T", "B", "V"]),
            "II": deque(["Y", "T", "K", "F", "J", "M", "D", "Q", "C", "H", "X", "R", "P", "E", "L", "W", "Z", "N", "V", "I", "S", "O", "G", "B", "U", "A"]),
            "III": deque(["P", "X", "E", "Z", "B", "W", "Y", "L", "F", "G", "U", "C", "D", "S", "I", "R", "J", "O", "M", "A", "K", "H", "T", "N", "V", "Q"]),
            "IV": deque(["R", "P", "X", "G", "K", "S", "B", "Y", "E", "C", "J", "I", "H", "U", "T", "N", "D", "M", "F", "Q", "A", "V", "L", "Z", "O", "W"]),
            "V": deque(["S", "M", "I", "R", "X", "P", "J", "U", "O", "A", "V", "D", "Q", "F", "L", "C", "Z", "K", "T", "W", "G", "E", "N", "B", "H", "Y"]),
        }

        self.rotors = {
            "right_input": deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]),
            "cener_input": deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]),
            "left_input": deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]),
        }

        self.selected_rotors = selected_rotors
        self.reflectorB = [
            "F", "B", "A", "V", "B", "A", "T", "Q", "K", "P", "H", "F", "T",
            "U", "Q", "P", "J", "X", "J", "K", "V", "X", "Y", "U", "H", "Y"
        ]
        self.reflectorC = [
            "E", "W", "Z", "F", "N", "W", "Q", "O", "E", "Z", "Y", "K", "V",
            "D", "L", "R", "D", "K", "N", "O", "Q", "V", "Y", "R", "F", "L"
        ]

        self.ring_setting = rings.upper()
        self.key_setting = key.upper()
    
    def set_rotors(self):
        self.rotors["right_output"] = self.stored_rotors[self.selected_rotors[0]]
        self.rotors["center_output"] = self.stored_rotors[self.selected_rotors[1]]
        self.rotors["left_output"] = self.stored_rotors[self.selected_rotors[2]]
    
    def get_index_of_letter(self, rotor, letter):
        return rotor.index(letter)

    def get_letter_at_index(self, rotor, index):
        return rotor[index]


def main():
    enigma = Enigma(["I", "II", "III"], "ABC", "XYZ")
    enigma.set_rotors()

    print("\n")
    [print(letter, end=" ") for letter in enigma.keyboard]
    print("\n")

    [print(letter, end=" ") for letter in enigma.rotors["right_input"]]
    print()
    [print(letter, end=" ") for letter in enigma.rotors["right_output"]]
    print("\n")

    [print(letter, end=" ") for letter in enigma.rotors["center_input"]]
    print()
    [print(letter, end=" ") for letter in enigma.rotors["center_output"]]
    print("\n")

    [print(letter, end=" ") for letter in enigma.rotors["left_input"]]
    print()
    [print(letter, end=" ") for letter in enigma.rotors["left_output"]]
    print("\n")

    [print(letter, end=" ") for letter in enigma.reflectorB]
    print("\n")


if __name__ == "__main__":
    import sys
    main()
