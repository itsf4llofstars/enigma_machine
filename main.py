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

import build-rotors as br
import utilities as f
from enigma import Enigma

rotor_i = []
rotor_ii = []
rotor_iii = []
rotor_iv = []
rotor_v = []

br.build_rotor(rotor_i)
br.build_rotor(rotor_ii)
br.build_rotor(rotor_iii)
br.build_rotor(rotor_iv)
br.build_rotor(rotor_v)

br.shuffle_rotor(rotor_i)
br.shuffle_rotor(rotor_ii)
br.shuffle_rotor(rotor_iii)
br.shuffle_rotor(rotor_iv)
br.shuffle_rotor(rotor_v)

filepath = "path_to_file"
br.check_for_rotor_file(filepath)

br.write_rotor_file(rotor_i)
br.write_rotor_file(rotor_ii)
br.write_rotor_file(rotor_iii)
br.write_rotor_file(rotor_iv)
br.write_rotor_file(rotor_v)
