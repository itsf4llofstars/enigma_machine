def get_reflector() -> str:
    """Polls the secret agant to select which reflector they wish to use
    and returns it.

    Returns:
        str: The letter of the rotor B or C
    """
    return str(input("Enter the reflector you wish to use [B/C]: ").upper())


def get_rings() -> str:
    """Polls the secret agent for a three letter ring setting and returns
    it.

    Returns:
        str: Three letters as a ring-setting
    """
    rings = str(input("Enter a three letter ring setting: "))
    return rings.upper()


def get_key() -> str:
    """Polls the secret agent for a three letter key setting and returns
    it.

    Returns:
        str: Three letters as a string key-setting
    """
    key = str(input("Enter a three letter key: "))
    return key.upper()


# TODO: Add error checking
def get_rotors():
    """Polls the secret agent for each individual rotor as a Roman numeral
    and appends it to a rotor list in order of first-left, second-center,
    third-right and returns the list.

    Returns:
        list(str): A list of three strings
    """
    rotors = []
    rotor = str(input("Enter the left rotor: "))
    rotors.append(rotor.upper())

    rotor = str(input("Enter the center rotor: "))
    rotors.append(rotor.upper())

    rotor = str(input("Enter the center rotor: "))
    rotors.append(rotor.upper())

    return list(rotors)


def get_user_letter() -> str:
    """Ask the secret agent to enter a single letter to be encoded and prints
    how to quit the task of entering letters.

    Returns:
        str: The letter to be encoded
    """
    return str(input("Enter your letter (qq to quit): ").upper())


def print_out(message) -> None:
    """Prints the encoded or decoded message in blocks of four letters
    and lines of 7 blocks.
    """
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
    import sys

    sys.exit(main())
