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

import buildrotors as br
import utilities as f
from enigma import Enigma

reflector = f.get_reflector()
ring = f.get_rings()
key = f.get_key()
rotors = f.get_rotors()
letter = f.get_user_letter()

print(f"{reflector = }")
print(f"{ring = }")
print(f"{key = }")
print(f"{rotors = }")
print(f"{letter = }")

enigma = Enigma(reflector, rotors, ring, key)


go = True
while go:
    letter = f.get_user_letter()
    if letter == 'QQ':
        go = False
        continue

    print(f"{letter = }")

print(f"User quit")

