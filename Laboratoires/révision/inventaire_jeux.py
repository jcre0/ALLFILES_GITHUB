import sys

import fonctions_inventaire as fn_inv


def inventaire_jeux() -> None:
    """
    Fonction principale du programme
    :return: Aucun.
    """
    collection_jeux = [  # Titre, console, condition
                       ["Contra", "NES", 8],  # 18 $
                       ["Chrono Trigger", "SNES", 2],  # 14 $
                       ["Quest64", "N64", 10],  # 30 $
                       ["Resident Evil 4", "GC", 5]  # 10 $
                      ]

    user_choice = fn_inv.afficher_menu()
    if user_choice == "1":
        fn_inv.ajouter_jeu(collection_jeux)
    elif user_choice == "2":
        fn_inv.calculer_valeur(collection_jeux)
    elif user_choice == "3":
        fn_inv.afficher_inventaire()
    elif user_choice == "0":
        sys.exit("Merci d'avoir utiliser le programme!")
    else:
        sys.exit("Merci d'avoir utiliser le programme!")






if __name__ == "__main__":
    inventaire_jeux()
