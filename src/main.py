#!/usr/bin/env python3
import buildrotors as br
import utilities as f
from enigma import Enigma

# reflector = f.get_reflector()
# ring = f.get_rings()
# key = f.get_key()
# rotors = f.get_rotors()
# letter = f.get_user_letter()

reflector = "B"
ring = "ABC"
key = "XYZ"
rotors = ["I", "II", "III"]
letter = f.get_user_letter()

print(f"{reflector = }")
print(f"{ring = }")
print(f"{key = }")
print(f"{rotors = }")
print(f"{letter = }")

# The below four calls must be in their current order
enigma = Enigma(reflector, rotors, ring, key)  # 1
enigma.set_rotors()  # 2
enigma.set_rings()  # 3
enigma.set_key()  # 4

go = True
user_input_letter = ""
while go:
    letter = f.get_user_letter()
    if letter == "QQ":
        go = False
        continue
    else:
        user_input_letter = letter

    enigma.rotate_rotor_right()

    # enigma.show_rotors()

    index = enigma.get_index_of_letter(enigma.keyboard, letter)
    letter = enigma.get_letter_at_index(enigma.rotors["right_input"], index)
    index = enigma.get_rotor_output_index(enigma.rotors["right_output"], letter)

    # Center Rotor
    letter = enigma.get_letter_at_index(enigma.rotors["center_input"], index)
    index = enigma.get_rotor_output_index(enigma.rotors["center_output"], letter)

    # Left rotor
    letter = enigma.get_letter_at_index(enigma.rotors["left_input"], index)
    index = enigma.get_rotor_output_index(enigma.rotors["left_output"], letter)

    # Reflector
    reflector_in_letter = enigma.get_letter_at_index(enigma.reflector, index)
    reflector_out_index = enigma.get_reflector_out_index(
        enigma.reflector, index, reflector_in_letter
    )

    # Left rotor
    letter = enigma.get_letter_at_index(
        enigma.rotors["left_output"], reflector_out_index
    )
    index = enigma.get_index_of_letter(enigma.rotors["left_input"], letter)

    # Center rotor
    letter = enigma.get_letter_at_index(enigma.rotors["center_output"], index)
    index = enigma.get_index_of_letter(enigma.rotors["center_input"], letter)

    # Rigth rotor
    letter = enigma.get_letter_at_index(enigma.rotors["right_output"], index)
    index = enigma.get_index_of_letter(enigma.rotors["right_input"], letter)

    # Encoded letter
    encoded_letter = enigma.get_letter_at_index(enigma.keyboard, index)
    print(f"Input: {user_input_letter} -> {encoded_letter}")

# print(f"User quit")
# 
# example_str = "THEXEASTXMOONXRISESXWITHXNOXTIDEX"
# message: str = "THEXCHAIRXISXAGAINSTXTHEXWALLXJOHNXHASXAXLONGXMUSTACHEXALLXWORKXANDXNOXPLAYXMAKEXJACKXAXDULLXBOY"
# 
# f.print_out(example_str)
# print()
# f.print_out(message)
# print()
