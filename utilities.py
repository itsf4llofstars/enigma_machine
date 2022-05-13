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


def get_reflector() -> str:
    """Polls the secret agant to select which reflector
    and returns it.

    Returns:
        str: The letter of the rotor B or C
    """
    return str(input("Enter the reflector you wish to use [B/C]: ").upper())


def get_rings() -> str:
    """Polls the secret agent for a three letter ring setting and returns
    it.

    Returns:
        str: Three letter as a ring-setting
    """
    rings = str(input("Enter a three letter ring setting: "))
    return rings.upper()


def get_key() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    key = str(input("Enter a three letter key: "))
    return key.upper()


# TODO: Add error checking
def get_rotors():
    """_summary_

    Returns:
        _type_: _description_
    """
    rotors = []
    rotor = str(input("Enter the left rotor: "))
    rotors.append(rotor.upper())

    rotor = str(input("Enter the center rotor: "))
    rotors.append(rotor.upper())

    rotor = str(input("Enter the center rotor: "))
    rotors.append(rotor.upper())

    return list(rotors)


def get_user_letter():
    return str(input("Enter your letter (qq to quit): ").upper())


def print_out(message):
    print("Message:\n")
    for i, letter in enumerate(message):
        if i > 0 and i % 4 == 0:
            print(" ", end="")
        if i > 0 and i % 28 == 0:
            print()
        print(letter, end="")
    print("\n")


def main():
    user_reflector = get_reflector()
    user_rings = get_rings()
    user_key = get_key()
    user_rotors = get_rotors()
    print(f"{user_reflector = } {user_rings = } {user_key = } {user_rotors = }")

    user_letter = get_user_letter()
    print(f"{user_letter = }")

    user_letter = get_user_letter()
    print(f"{user_letter = }")


if __name__ == "__main__":
    main()
