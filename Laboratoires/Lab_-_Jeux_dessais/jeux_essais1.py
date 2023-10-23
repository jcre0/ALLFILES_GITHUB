def add_nombres(nb1: int, nb2: int = 5) -> int:
    """
    Additionne deux nombres et retourne le résultat.
    Si seulement un nombre est entré, le deuxième nombre sera 5.
    :param nb1: Le premier nombre à additionner.
    :param nb2: Le deuxième nombre à additionner.
    :return: Le résultat de l'addition.
    """
    return abs(nb1) + abs(nb2)


if __name__ == "__main__":
    # LIRE les nombres à additionner CALCULER le résultat de l'addition.
    nombre1 = int(input("Premier nombre à additionner : "))
    entree2 = input("Voulez-vous entrer un deuxième nombre, sinon sa valeur par défaut sera de 5 [oui, non] ?")
    if entree2.lower().strip() in ["oui", "o", "y", "yes"]:
        nombre2 = int(input("Deuxième nombre à additionner : "))
        resultat = add_nombres(nombre1, nombre2)
    else:
        nombre2 = 5
        resultat = add_nombres(nombre1)

    # AFFICHER le résultat.
    print(f"\n{nombre1} + {nombre2} = {resultat}")
