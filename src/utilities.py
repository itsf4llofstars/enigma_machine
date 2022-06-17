def get_reflector() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    return str(input("Enter the reflector you wish to use [B/C]: ").upper())


def get_rings() -> str:
    """_summary_

    Returns:
        str: _description_
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
    """_summary_

    Returns:
        _type_: _description_
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
