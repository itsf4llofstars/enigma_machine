from collections import deque


# fmt: off
class Enigma:
    """_summary_
    """
    def __init__(self, reflector, selected_rotors, rings: str, key: str) -> None:
        self.keyboard = deque([
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ])

        self.stored_rotors = {
            "I": deque([
                'U', 'L', 'R', 'X', 'C', 'Q', 'O', 'K', 'G', 'N', 'J', 'A', 'F',
                'I', 'H', 'Z', 'W', 'S', 'E', 'Y', 'M', 'P', 'D', 'T', 'B', 'V'
            ]),
            "II": deque([
                'Y', 'T', 'K', 'F', 'J', 'M', 'D', 'Q', 'C', 'H', 'X', 'R', 'P',
                'E', 'L', 'W', 'Z', 'N', 'V', 'I', 'S', 'O', 'G', 'B', 'U', 'A'
            ]),
            "III": deque([
                'P', 'X', 'E', 'Z', 'B', 'W', 'Y', 'L', 'F', 'G', 'U', 'C', 'D',
                'S', 'I', 'R', 'J', 'O', 'M', 'A', 'K', 'H', 'T', 'N', 'V', 'Q'
            ]),
            "IV": deque([
                'R', 'P', 'X', 'G', 'K', 'S', 'B', 'Y', 'E', 'C', 'J', 'I', 'H',
                'U', 'T', 'N', 'D', 'M', 'F', 'Q', 'A', 'V', 'L', 'Z', 'O', 'W'
            ]),
            "V": deque([
                'S', 'M', 'I', 'R', 'X', 'P', 'J', 'U', 'O', 'A', 'V', 'D', 'Q',
                'F', 'L', 'C', 'Z', 'K', 'T', 'W', 'G', 'E', 'N', 'B', 'H', 'Y'
            ]),
        }

        self.rotors = {
            "right_input": deque([
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
            ]),
            "center_input": deque([
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
            ]),
            "left_input": deque([
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
            ]),
        }

        self.stored_reflectors = {
            "B": [
                'F', 'B', 'A', 'V', 'B', 'A', 'T', 'Q', 'K', 'P', 'H', 'F', 'T',
                'U', 'Q', 'P', 'J', 'X', 'J', 'K', 'V', 'X', 'Y', 'U', 'H', 'Y'
            ],
            "C": [
                'E', 'W', 'Z', 'F', 'N', 'W', 'Q', 'O', 'E', 'Z', 'Y', 'K', 'V',
                'D', 'L', 'R', 'D', 'K', 'N', 'O', 'Q', 'V', 'Y', 'R', 'F', 'L'
            ],
        }
# fmt: on
        self.reflector = self.stored_reflectors[reflector]

        self.selected_rotors = selected_rotors
        self.ring_setting = rings.upper()
        self.key_setting = key.upper()

    def show_rotors(self):
        """_summary_
        """
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

        [print(letter, end=" ") for letter in self.reflector]
        print("\n")

    def set_rotors(self):
        """_summary_
        """
        self.rotors["right_output"] = self.stored_rotors[self.selected_rotors[0]]
        self.rotors["center_output"] = self.stored_rotors[self.selected_rotors[1]]
        self.rotors["left_output"] = self.stored_rotors[self.selected_rotors[2]]

    def set_rings(self):
        """_summary_
        """
        while self.rotors["right_output"][0] != self.ring_setting[0]:
            deque.rotate(self.rotors["right_output"], -1)
        while self.rotors["center_output"][0] != self.ring_setting[1]:
            deque.rotate(self.rotors["center_output"], -1)
        while self.rotors["left_output"][0] != self.ring_setting[2]:
            deque.rotate(self.rotors["left_output"], -1)

    def set_key(self):
        """_summary_
        """
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
        """_summary_
        """
        deque.rotate(self.rotors["right_input"], -1)
        deque.rotate(self.rotors["right_output"], -1)

    def rotate_rotor_center(self):
        """_summary_
        """
        deque.rotate(self.rotors["center_input"], -1)
        deque.rotate(self.rotors["center_output"], -1)

    def rotate_rotor_left(self):
        """_summary_
        """
        deque.rotate(self.rotors["left_input"], -1)
        deque.rotate(self.rotors["left_output"], -1)

    @staticmethod
    def get_index_of_letter(rotor, letter):
        """_summary_

        Args:
            rotor (_type_): _description_
            letter (_type_): _description_

        Returns:
            _type_: _description_
        """
        return rotor.index(letter)

    @staticmethod
    def get_letter_at_index(rotor, index):
        return rotor[index]

    @staticmethod
    def get_rotor_output_index(rotor, letter):
        """_summary_

        Args:
            rotor (_type_): _description_
            letter (_type_): _description_

        Returns:
            _type_: _description_
        """
        return rotor.index(letter)

    @staticmethod
    def get_reflector_out_index(reflector, index, letter):
        """_summary_

        Args:
            reflector (_type_): _description_
            index (_type_): _description_
            letter (_type_): _description_

        Returns:
            _type_: _description_
        """
        index = (1 + index) % len(reflector)
        while reflector[index] != letter:
            index = (1 + index) % len(reflector)
        return index


def main():
    # <editor-fold desc="MAPPING ONE">
    # MAPPING ONE
    """
    # The below four calls must remain in this order
    enigma = Enigma("C", ["I", "II", "III"], "XGE", "WMC")
    enigma.set_rotors()
    enigma.set_rings()
    enigma.set_key()

    enigma.show_rotors()

    user_input_letter = "D"
    enigma.rotate_rotor_right()
    enigma.show_rotors()

    # Keyboard
    index = enigma.get_index_of_letter(enigma.keyboard, user_input_letter)
    print(f"Letter input to be encoded: {user_input_letter} Index: {index}\n")

    # Right rotor
    letter = enigma.get_letter_at_index(enigma.rotors["right_input"], index)
    index = enigma.get_rotor_output_index(enigma.rotors["right_output"], letter)
    print(f"Right Rotor: output index: {index} {letter = }")

    # Center Rotor
    letter = enigma.get_letter_at_index(enigma.rotors["center_input"], index)
    index = enigma.get_rotor_output_index(enigma.rotors["center_output"], letter)
    print(f"Middle Rotor: output index: {index} {letter = }")

    # Left rotor
    letter = enigma.get_letter_at_index(enigma.rotors["left_input"], index)
    index = enigma.get_rotor_output_index(enigma.rotors["left_output"], letter)
    print(f"Left Rotor: output index: {index} {letter = }")

    # Reflector
    reflector_in_letter = enigma.get_letter_at_index(enigma.reflector, index)
    reflector_out_index = enigma.get_reflector_out_index(
        enigma.reflector, index, reflector_in_letter
    )
    print(f"\nReflector: {reflector_in_letter = } {reflector_out_index = }\n")

    # Left rotor
    letter = enigma.get_letter_at_index(
        enigma.rotors["left_output"], reflector_out_index
    )
    index = enigma.get_index_of_letter(enigma.rotors["left_input"], letter)
    print(f"Left Rotor: output index: {index} {letter = }")

    # Center rotor
    letter = enigma.get_letter_at_index(enigma.rotors["center_output"], index)
    index = enigma.get_index_of_letter(enigma.rotors["center_input"], letter)
    print(f"Center Rotor: output index: {index} {letter = }")

    # Rigth rotor
    letter = enigma.get_letter_at_index(enigma.rotors["right_output"], index)
    index = enigma.get_index_of_letter(enigma.rotors["right_input"], letter)
    print(f"Right Rotor: output index: {index} {letter = }\n")

    # Encoded letter
    encoded_letter = enigma.get_letter_at_index(enigma.keyboard, index)
    print(f"Input: {user_input_letter} Encoded to: {encoded_letter}\n")
    """
    # </editor-fold>

    # MAPPING TWO
    reflector = 'C'
    rotors = ['III', 'IV', 'I']
    ring = 'BDF'
    key = 'HJL'
    enigma = Enigma(reflector, rotors, ring, key)
    enigma.set_rotors()
    enigma.set_rings()
    enigma.set_key()

    letter_in = 'B'
    enigma.rotate_rotor_right()
    enigma.show_rotors()

    index_of_letter = enigma.get_index_of_letter(enigma.keyboard, letter_in)
    letter_at_index = enigma.get_letter_at_index(enigma.rotors["right_input"], index_of_letter)
    index_of_letter = enigma.get_index_of_letter(enigma.rotors["right_output"], letter_at_index)
    letter_at_index = enigma.get_letter_at_index(enigma.rotors["center_input"], index_of_letter)
    index_of_letter = enigma.get_index_of_letter(enigma.rotors["center_output"], letter_at_index)
    letter_at_index = enigma.get_letter_at_index(enigma.rotors["left_input"], index_of_letter)
    index_of_letter = enigma.get_index_of_letter(enigma.rotors["left_output"], letter_at_index)

    letter_at_index = enigma.get_letter_at_index(enigma.reflector, index_of_letter)
    reflectro_out_index = enigma.get_reflector_out_index(enigma.reflector, index_of_letter, letter_at_index)
    print(reflectro_out_index)

    # TODO: From here look a mapping one to see how we progress up the rotors.


if __name__ == "__main__":
    main()
