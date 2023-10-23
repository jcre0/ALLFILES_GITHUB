import textwrap


def menu_grandeurs(ls_grandeurs: list):
    """
    Affiche un menu qui offre une variété de grandeurs différentes.
    :param ls_grandeurs: Toutes les grandeurs disponibles.
    """
    print("Bienvenue au menu des grandeurs!")
    for size in ls_grandeurs:
        print(size)
    while True:
        print(f"""
        1. Modifier la liste de grandeurs
        2. Enlever une valeur de la liste de grandeurs
        3. Ajouter une nouvelle grandeur à la liste
        4. Quitter le programme
""")
        action = int(input("Voulez vous modifier la liste de grandeurs?"))
        return user_action(action, ls_grandeurs)



def user_action(choice:int, ls_grandeurs):
    print("Votre choix: ", choice)
    if choice == 1:
        print("Quelle valeur voulez vous modifier dans la liste suivante?")
        for i in ls_grandeurs:
            print(i)
        user_edit_choice = input()
        return edit(user_edit_choice, ls_grandeurs)

def edit(user_edit_choice, ls_grandeurs):
    ls_grandeurs[user_edit_choice] = input("Entrer une nouvelle valeur: ")
    print("Voici la nouvelle version de la liste de grandeurs: ", ls_grandeurs)



def afficher_questionnaire(p_nb_questions: int, p_nb_choix: int):
    """
    Affiche le gabarit pour la quantité de questions et choix demandés.
    :param p_nb_questions: Le nombre de questions.
    :param p_nb_choix: Le nombre de choix par question.
    """
    for i in range(p_nb_questions):
        print("Question", i+1)
        for nb in range(p_nb_choix):
            print("---choix", nb+1)



def main():
    # Afficher le choix des fonctions
    choix = input(textwrap.dedent("""
    Choississez une option :
    1. Menu des grandeurs
    2. Afficher un questionnaire

    Quel est votre choix ? """))
    print()

    # Exécuter la fonction choisie
    match choix:
        case "1":
            ls_grandeurs = ["petit", "moyen", "grand"]
            menu_grandeurs(ls_grandeurs)

        case "2":
            nb_questions = int(input("Combien de questions dans le questionnaire ? "))
            nb_choix = int(input("Combien de choix par question ? "))
            afficher_questionnaire(nb_questions, nb_choix)


if __name__ == '__main__':
    main()
