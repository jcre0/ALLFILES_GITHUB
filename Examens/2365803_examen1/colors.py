couleurs_secondaires = [["orange", "rouge", "jaune"], ["vert", "jaune", "bleu"], ["violet", "bleu", "rouge"]]

color_choices = ["orange", "vert", "violet"]


def choose_color_input():
    global color_choices
    global chosen_color
    color_choices = ["orange", "vert", "violet"]
    chosen_color = input("What color do you want to make between orange, vert, and violet? Enter here: ")
    if chosen_color.lower() == couleurs_secondaires[0][0]:
        print("To make orange you must mix the colors", couleurs_secondaires[0][1], "and", couleurs_secondaires[0][2])
        quit()
    elif chosen_color.lower() == couleurs_secondaires[1][0]:
        print("To make vert you must mix the colors", couleurs_secondaires[1][1], "and", couleurs_secondaires[1][2])
        quit()
    elif chosen_color.lower() == couleurs_secondaires[2][0]:
        print("To make violet you must mix the colors", couleurs_secondaires[2][1], "and", couleurs_secondaires[2][2])
        quit()
    else:
        print("Invalid choice!!! Please retry to input a valid color between", color_choices)
        return choose_color_input()

choose_color_input()