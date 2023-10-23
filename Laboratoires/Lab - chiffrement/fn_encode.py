# Tuple des caractères qui seront décalés.
_tp_decalage = (
    ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C',
    'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6',
    '7', '8', '9', '!', 'é', 'É', 'À', 'à', 'ù', 'Ù',
    'è', 'È', 'ô', 'Ô', 'Î', 'î', 'ï', 'Ï', "'", '/',
    '$', '%', '?', '&', '*', '(', ')', '_', '+', '=',
    '.', ',', '-', '"', "@")


def cesar(starting_text: str, offset: int) -> str:
    """
    :param start_text: The start text is determined by the user on the main_menu() function
    :param nb_rotation: This determines the encrypting rotation ammount
    :return: The returned value should be the encrypted message
    Steps to encrypt:
        1. Locate the letter's location in the _tp_decalage tuple.
        2. Change the position of the letter depending on the user's input (rotation var)
        3. Return the complete encrypted message
    """
    end_text = []
    for i in starting_text:
        if i == "@":
            i = '"'
        starting_letter_pos = _tp_decalage.index(i)
        encrypt_letter_pos = starting_letter_pos + offset
        end_text.append(_tp_decalage[encrypt_letter_pos])

    print(end_text)



def vigenere():
    print("Hello world")
