#/usr/bin/env python3
"""main.py file"""
from enigma import Enigma
import utilities as f
import build-rotors as br

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

print(rotor_i)
print(rotor_ii)
print(rotor_iii)
print(rotor_iv)
print(rotor_v)
