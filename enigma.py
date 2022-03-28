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
    def __init__(self, rotors, key) -> None:
        self.keyboard = deque(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])

        self.rotorI = ['V', 'Z', 'W', 'O', 'G', 'B', 'Y', 'H', 'M', 'L', 'D', 'I', 'J', 'U', 'P', 'R', 'X', 'C', 'E', 'A', 'N', 'K', 'F', 'Q', 'T', 'S']
        self.rotorII = ['D', 'T', 'H', 'A', 'B', 'P', 'O', 'J', 'M', 'I', 'W', 'L', 'E', 'N', 'V', 'U', 'Z', 'F', 'S', 'K', 'Q', 'X', 'Y', 'R', 'C', 'G']
        self.rotorIII = ['E', 'M', 'L', 'G', 'V', 'Q', 'C', 'Z', 'K', 'I', 'H', 'P', 'D', 'X', 'T', 'R', 'F', 'S', 'A', 'J', 'W', 'O', 'N', 'Y', 'B', 'U']
        self.rotorIV = ['E', 'K', 'V', 'O', 'T', 'H', 'L', 'M', 'S', 'D', 'P', 'Z', 'Q', 'C', 'J', 'R', 'B', 'N', 'F', 'U', 'Y', 'A', 'X', 'G', 'W', 'I']
        self.rotorV = ['J', 'H', 'L', 'F', 'O', 'W', 'R', 'A', 'E', 'M', 'G', 'S', 'Y', 'N', 'X', 'P', 'U', 'T', 'V', 'B', 'I', 'D', 'Z', 'Q', 'C', 'K']

        self.rotors = {
            "right_input": deque([]),
            "right_output": deque([]),
            "cener_input": deque([]),
            "cener_output": deque([]),
            "left_input": deque([]),
            "left_output": deque([]),
        }

        self.reflectorB = []
        self.reflectorC = []

def main():
    pass


if __name__ == "__main__":
    main()

