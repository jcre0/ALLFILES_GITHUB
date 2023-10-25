def afficher_menu() -> str:
    """
    Function that makes the main menu isible and let's the user choose what action they want to do.
    :return: The user choice:
    """
    print(f"""
    Menu principal

    1. Ajouter un jeu
    2. Calculer la valeur totale
    3. Afficher l'inventaire
    0. Quitter

""")
    user_choice = input("Entré votre choix ici: ")
    return user_choice


def ajouter_jeu(liste_initiale: list) -> list:
    """
    Ajoute un jeu à la collection
    :param liste_initiale: La liste initiale, avant l'ajout.
    :return: La liste avec le(s) jeu(x) ajouté(s)
    """
    print("Enter the different values needed to add the game to your database: ")
    game = []
    console_choices = ["NES", "SNES", "N64", "GC"]
    condition_choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    game_title = input("Game title: ")
    while True:
        game_console = input("Game console (NES, SNES, N64, GC): ")
        if game_console.upper() in console_choices:
            break
        else:
            print("Console choice is invalid!")
            continue
    while True:
        game_condition = input("Game condition (1-10 where 0 is the best condition): ")
        if game_condition in condition_choices:
            break
        else:
            print("Condition is not valid!")
            continue
    game = [game_title, game_console, game_condition]
    liste_initiale.append(game)

def calculer_valeur(liste_jeux: list) -> float:
    """
    Calcule la valeur totale de la collection
    :param liste_jeux: La liste des jeux
    :return: La valeur totale de la collection
    """
    for i in liste_jeux:
        current_console_name = i[1]
        current_console_condition = i[2]
        if current_console_name == "NES":
            current_value = 10
            if current_console_condition < 5:
                current_value = current_value - (current_value * (5 - current_console_condition) / 10)
            elif current_console_condition == 5:
                current_value = current_value
            else:
                current_value =  current_value + (current_value * current_console_condition / 10)
        elif current_console_name == "SNES":
            current_value = 20
            if current_console_condition < 5:
                current_value = current_value - (current_value * (5 - current_console_condition) / 10)
            elif current_console_condition == 5:
                current_value = current_value
            else:
                current_value =  current_value + (current_value * current_console_condition / 10)




def afficher_inventaire(liste_jeux: list) -> None:
    """
    Affiche le détail de chaque jeu.
    :param liste_jeux: La liste des jeux
    :return: Aucun.
    """
    pass
