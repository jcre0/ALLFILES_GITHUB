def verifier_gagnant(joueur1, joueur2) -> str:
    """
    Vérifie le résultat d'une joute de roche, papier et ciseau.
    :param joueur1: L'arme du joueur 1
    :param joueur2: L'arme du joueur 2
    :return: Une phrase qui décrit le résultat du combat.
    """
    # Logique conditionnelle pour trouver le gagnant
    if joueur1 == joueur2:
        return "Partie nulle !"
    elif joueur1 == 'roche':
        if joueur2 == 'ciseau':
            joueur_gagnant = joueur1
        else:
            joueur_gagnant = joueur2
    elif joueur1 == 'ciseau':
        if joueur2 == 'roche':
            joueur_gagnant = joueur1
        else:
            joueur_gagnant = joueur2
    elif joueur1 == 'papier':
        if joueur2 == 'roche':
            joueur_gagnant = joueur1
        else:
            joueur_gagnant = joueur2
    else:
        return "Partie invalide, les armes ne sont pas réglementaires."

    if joueur_gagnant == joueur1:
        return f"Le joueur 1 a gagné avec {joueur1} contre {joueur2}."
    else:
        return f"Le joueur 2 a gagné avec {joueur2} contre {joueur1}."


def main():
    jouer = "oui"
    # Boucle de jeu, dite "non" pour sortir.
    while jouer in ["oui", "o", "y", "yes"]:
        # Afficher menu
        print("""
        Bienvenu au jeu Roche-Papier-Ciseau.
        Veuillez faire un choix parmi les suivants : 
        - roche
        - papier
        - ciseau
        """)

        # Lire choix des joueurs.
        joueur1 = input("Choix du joueur 1 : ").lower().strip()
        joueur2 = input("Choix du joueur 2 : ").lower().strip()

        # Validation des armes
        if joueur1 not in ["roche", "papier", "ciseau"] or joueur2 not in ["roche", "papier", "ciseau"]:
            print("Au moins un des joueurs a choisi une arme non réglementaire.")
        else:
            resultat = verifier_gagnant(joueur1, joueur2)
            print(resultat)

        # Lire, est-ce qu'il y aura une autre partie.
        jouer = (input("\nVoulez-vous jouer de nouveau [oui, non] ? ").lower().strip())


if __name__ == "__main__":
    main()
