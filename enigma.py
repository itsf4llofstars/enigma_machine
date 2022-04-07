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
from copy import copy

# TODO: Set reflector attribute in class init


# fmt: off
class Enigma:
    """Class model of the German Enigma Test Encoding machine
    """
    def __init__(self, reflector, selected_rotors, rings: str, key: str) -> None:
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
            "I": deque([
                "U", "L", "R", "X", "C", "Q", "O", "K", "G", "N", "J", "A", "F",
                "I", "H", "Z", "W", "S", "E", "Y", "M", "P", "D", "T", "B", "V"
            ]),
            "II": deque([
                "Y", "T", "K", "F", "J", "M", "D", "Q", "C", "H", "X", "R", "P",
                "E", "L", "W", "Z", "N", "V", "I", "S", "O", "G", "B", "U", "A"
            ]),
            "III": deque([
                "P", "X", "E", "Z", "B", "W", "Y", "L", "F", "G", "U", "C", "D",
                "S", "I", "R", "J", "O", "M", "A", "K", "H", "T", "N", "V", "Q"
            ]),
            "IV": deque([
                "R", "P", "X", "G", "K", "S", "B", "Y", "E", "C", "J", "I", "H",
                "U", "T", "N", "D", "M", "F", "Q", "A", "V", "L", "Z", "O", "W"
            ]),
            "V": deque([
                "S", "M", "I", "R", "X", "P", "J", "U", "O", "A", "V", "D", "Q",
                "F", "L", "C", "Z", "K", "T", "W", "G", "E", "N", "B", "H", "Y"
            ]),
        }

        self.rotors = {
            "right_input": deque([
                "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
            ]),
            "center_input": deque([
                "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
            ]),
            "left_input": deque([
                "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
            ]),
        }

        self.reflectorB = [
            "F", "B", "A", "V", "B", "A", "T", "Q", "K", "P", "H", "F", "T",
            "U", "Q", "P", "J", "X", "J", "K", "V", "X", "Y", "U", "H", "Y"
        ]
        self.reflectorC = [
            "E", "W", "Z", "F", "N", "W", "Q", "O", "E", "Z", "Y", "K", "V",
            "D", "L", "R", "D", "K", "N", "O", "Q", "V", "Y", "R", "F", "L"
        ]

        self.reflector = None
        if reflector.upper() == "B":
            self.reflector = copy(self.reflectorB)
        else:
            self.reflector = copy(self.reflectorC)

        self.selected_rotors = selected_rotors
        self.ring_setting = rings.upper()
        self.key_setting = key.upper()

    def show_rotors(self):
        print("\n")
        [print(letter, end=" ") for letter in self.keyboard]
        print("\n")

        [print(letter, end=" ") for letter in self.rotors["right_input"]]
        print()
        [print(letter, end=" ") for letter in self.rotors["right_output"]]
        print("\n")

        [print(letter, end=" ") for letter in self.rotors["center_input"]]
        print()
        [print(letter, end=" ") for letter in self.rotors["center_output"]]
        print("\n")

        [print(letter, end=" ") for letter in self.rotors["left_input"]]
        print()
        [print(letter, end=" ") for letter in self.rotors["left_output"]]
        print("\n")

        # TODO: This will need to be changed to the reflector in use
        [print(letter, end=" ") for letter in self.reflectorB]
        print("\n")

    def set_rotors(self):
        self.rotors["right_output"] = self.stored_rotors[self.selected_rotors[0]]
        self.rotors["center_output"] = self.stored_rotors[self.selected_rotors[1]]
        self.rotors["left_output"] = self.stored_rotors[self.selected_rotors[2]]

    def set_rings(self):
        while self.rotors["right_output"][0] != self.ring_setting[0]:
            deque.rotate(self.rotors["right_output"], -1)
        while self.rotors["center_output"][0] != self.ring_setting[1]:
            deque.rotate(self.rotors["center_output"], -1)
        while self.rotors["left_output"][0] != self.ring_setting[2]:
            deque.rotate(self.rotors["left_output"], -1)

    def set_key(self):
        while self.rotors["right_input"][0] != self.key_setting[0]:
            deque.rotate(self.rotors["right_input"], -1)
            deque.rotate(self.rotors["right_output"], -1)
        while self.rotors["center_input"][0] != self.key_setting[1]:
            deque.rotate(self.rotors["center_input"], -1)
            deque.rotate(self.rotors["center_output"], -1)
        while self.rotors["left_input"][0] != self.key_setting[2]:
            deque.rotate(self.rotors["left_input"], -1)
            deque.rotate(self.rotors["left_output"], -1)
    
    def rotate_rotor_right(self):
        deque.rotate(self.rotors["right_input"], -1)
        deque.rotate(self.rotors["right_output"], -1)

    def rotate_rotor_center(self):
        deque.rotate(self.rotors["center_input"], -1)
        deque.rotate(self.rotors["center_output"], -1)

    def rotate_rotor_left(self):
        deque.rotate(self.rotors["left_input"], -1)
        deque.rotate(self.rotors["left_output"], -1)

    def get_index_of_letter(self, rotor, letter):
        return rotor.index(letter)

    def get_letter_at_index(self, rotor, index):
        return rotor[index]

    def get_rotor_output_index(self, rotor, letter):
        return rotor.index(letter)

    def get_reflector_out_index(self, reflector, index, letter):
        index = (1 + index) % len(reflector)
        while reflector[index] != letter:
            index = (1 + index) % len(reflector)
        return index
# fmt: on


def main():
    # The below four calls must remain in this order
    enigma = Enigma("B", ["I", "II", "III"], "XGE", "WMC")
    enigma.set_rotors()
    enigma.set_rings()
    enigma.set_key()

    enigma.show_rotors()

    user_input_letter = "D"

    enigma.rotate_rotor_right()

    enigma.show_rotors()
    print(f"Letter input to be encoded: {user_input_letter}")

    # Right rotor
    index = enigma.get_index_of_letter(enigma.keyboard, user_input_letter)
    letter = enigma.get_letter_at_index(enigma.rotors["right_input"], index)
    index = enigma.get_rotor_output_index(enigma.rotors["right_output"], letter)
    print(f"output index: {index} {letter = }")

    # Center Rotor
    letter = enigma.get_letter_at_index(enigma.rotors["center_input"], index)
    index = enigma.get_rotor_output_index(enigma.rotors["center_output"], letter)
    print(f"output index: {index} {letter = }")

    # Left rotor
    letter = enigma.get_letter_at_index(enigma.rotors["left_input"], index)
    index = enigma.get_rotor_output_index(enigma.rotors["left_output"], letter)
    print(f"output index: {index} {letter = }")

    # Reflector
    reflector_in_letter = enigma.get_letter_at_index(enigma.reflectorB, index)
    reflector_out_index = enigma.get_reflector_out_index(
        enigma.reflectorB, index, reflector_in_letter
    )
    print(f"{reflector_in_letter = } {reflector_out_index = }")

    # Left rotor
    letter = enigma.get_letter_at_index(
        enigma.rotors["left_output"], reflector_out_index
    )
    index = enigma.get_index_of_letter(enigma.rotors["left_input"], letter)
    print(f"output index: {index} {letter = }")

    # Center rotor
    letter = enigma.get_letter_at_index(enigma.rotors["center_output"], index)
    index = enigma.get_index_of_letter(enigma.rotors["center_input"], letter)
    print(f"output index: {index} {letter = }")

    # Rigth rotor
    letter = enigma.get_letter_at_index(enigma.rotors["right_output"], index)
    index = enigma.get_index_of_letter(enigma.rotors["right_input"], letter)
    print(f"output index: {index} {letter = }")

    # Encoded letter
    encoded_letter = enigma.get_letter_at_index(enigma.keyboard, index)
    print(f"Input: {user_input_letter} -> {encoded_letter}")


if __name__ == "__main__":
    main()
