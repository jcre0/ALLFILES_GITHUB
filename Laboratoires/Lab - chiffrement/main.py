import sys
import fn_encode as encode

def main():  # This function ensures that the user enters valid values for the rotation and the encode type.
    print(f"""
    Veuillez choisir un choix ci-dessous:
    
    1. César
    2. Vigénère
""")
    while True:
        try:
            encode_type = input("Entrer le type d'encodage ici: ")
            if encode_type not in ["1", "2"]:
                raise ValueError
            else:
                break
        except ValueError:
            print("Veuillez entrer une valeur entre 1 et 2.")
            pass
    start_text = input("Entrer le text à encoder ici: ")
    while True:
        try:
            rotation = int(input("Entrer le nombre de rotation: "))
            if rotation < 0:
                raise ValueError
            else:
                break
        except ValueError or TypeError:
            print("Entrer un nombre positif!")
            pass
    if encode_type == "1":
        encode.cesar(start_text, rotation)
    elif encode_type == "2":
        pass









if __name__ == '__main__':
    main()
