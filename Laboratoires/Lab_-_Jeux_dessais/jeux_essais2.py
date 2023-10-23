def comparer_nombres(nombre1: float, nombre2: float) -> str:
    """
    Compare deux nombres et retourne le résultat.
    :param nombre1: Le premier nombre à comparer.
    :param nombre2: Le deuxième nombre à comparer.
    :return: Une phrase décrivant la comparaison.
    """
    if nombre2 < nombre1:
        return f"{nombre2} est plus petit que {nombre1}."
    else:
        return f"{nombre2} est plus grand que {nombre1}."


if __name__ == "__main__":
    # Variables
    nombre_debut = 0

    nombre_nouveau = input("\nEntrer un nombre à comparer : ")
    # Boucle jusqu'à ce que l'entrée ne soit pas un nombre réel
    while nombre_nouveau.isnumeric():
        # Convertir en nombre réel.
        nombre_nouveau = float(nombre_nouveau)

        # COMPARER les nombres et AFFICHER le résultat.
        print(comparer_nombres(nombre_debut, nombre_nouveau))

        # Remplacer nombre de base
        nombre_debut = nombre_nouveau

        # LIRE le nombre à comparer
        nombre_nouveau = input("\nEntrer un nombre à comparer : ")

    # Affichage de sortie
    print("Merci d'avoir joué.")
