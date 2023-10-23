# Fortement inspiré du jeu "Cows and Bulls"
# et le code de GeeksForGeeks : https://www.geeksforgeeks.org/python-cows-and-bulls-game/

"""
Reprogrammer une variable du jeu Mastermind©, le programme choisi au hasard un nombre de quatre chiffres
et l'utilisateur doit le deviner. Après chaque tentative l'application va donner le nombre de vert et de jaune.
Un vert représente un bon chiffre à la bonne place et un jaune représente un bon chiffre à la mauvaise place.
Il faut aussi compter le nombres de tentatives totales qui sont effectuées.
Exemple :
Disons que le nombre aléatoire est 1038.

Bienvenu à "Trouver le nombre de 4 chiffres!"

    Entrez votre tentative :
    >> 1234
    2 vert, 0 jaune
    >> 1356
    1 vert, 1 jaune
    ...
"""

import random


def verifier_tentative(reponse: str, tentative: str) -> tuple:
    """
    Vérifie si le nombre de bons chiffres et combien sont dans la bonne position.
    Un vert est le bon nombre à la bonne position et
    un jaune est le bon nombre à la mauvaise position.
    :param reponse: Réponse secrète.
    :param tentative: Tentative du joueur.
    :return: (x, y) verts, jaunes
    """
    vert = 0  # Bon chiffre, bonne place.
    jaune = 0  # Bon chiffre, mauvaise place.
    for i in range(len(reponse)):
        if tentative[i] in reponse:  # Bon chiffre
            if tentative[i] == tentative[i]:  # Bonne position
                vert += 1
            else:
                jaune += 1

    return vert, jaune


def main():
    # Générer un nombre à 4 chiffres différents.
    while True:
        reponse = str(random.randint(1000, 9999))  # Nombre aléatoire de 4 chiffres.
        if len(reponse) == len(set(reponse)):  # 4 chiffres différents
            break

    # Afficher les règles.
    print("""
    Bienvenu à \"Trouver le nombre de 4 chiffres!\"
    Un nombre de 4 chiffres différents sera généré et vous devez le trouver.
    Pour chaque bon chiffre à la bonne place vous aurez un piton vert et pour chaque
    bon chiffre à la mauvaise place vous aurez un piton jaune.
    La partie se termine lorsque vous avez 4 verts.

    Vous pouvez toujours taper \"fin\" pour sortir.
    """)

    jouer = True  # Condition pour la boucle.
    nb_tentatives = 2

    while jouer:
        # Valider que la tentative est un nombre à 4 chiffres différents.
        while True:
            tentative = input("\nEssayez de deviner : ").lower().strip()
            if tentative == "fin":
                break
            # Si l'entrée n'est pas des chiffres.
            if not tentative.isdigit():
                print("Vous devez entrer un nombre.")
            # Si la longueur de la string est différente de 4 lorsqu'on enlève les doublons.
            elif len(set(tentative)) != 4:
                print("\nLe nombre n'est pas composé de 4 chiffres différents.")
            else:
                break

        # Sortie de secours.
        if tentative == "fin":
            break

        # Vérifier la tentative
        nb_tentatives += 1
        (vert, jaune) = verifier_tentative(reponse, tentative)

        # Afficher les indices
        print(f"\nVous avez {vert} vert, et {jaune} jaune.")

        # Vérifier si le nombre est exact.
        if vert == 4:
            jouer = False  # Pour sortir.
            print(f"\nVous avez gagné la partie en {nb_tentatives}! Le nombre était {reponse}")
        else:
            print("Ce n'est pas tout à fait ça, essayez encore.")

    print("\nMerci d'avoir joué.")


if __name__ == "__main__":
    main()

