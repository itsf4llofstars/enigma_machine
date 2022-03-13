#!/usr/bin/env python3
"""main.py file"""
import build_rotors as br
import utilities as f
from enigma import Enigma

rotor_i: List[str] = []
rotor_ii: List[str] = []
rotor_iii: List[str] = []
rotor_iv: List[str] = []
rotor_v: List[str] = []

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
