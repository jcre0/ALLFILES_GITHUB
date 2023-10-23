# Nicolas est devenu un fou des chats, il pense que ça le rend charmant. 
# Il a 100 chats ! Une journée où son isolation de COVID le rend un peu cinglé, 
# il décide de faire un grand rond avec ses chats et de leur mettre des chapeaux. 
# Cependant, il a une méthode bien particulière. 
# À chaque fois qu’il passe devant un chat sans chapeau il lui en met un, mais s’il a déjà un chapeau, il lui enlève. 
# Nicolas va faire 100 tours, voici comment il procède.
import sys

# Le premier tour, il arrête à chaque chat, ils auront donc tous un chapeau.
# Le deuxième tour, il arrête seulement à chaque 2 chats.
# Le troisième tour, il arrête à chaque 3 chats, et ainsi de suite.
# Le centième et dernier tour, il va arrêter seulement au 100e et dernier chat.

# Finalement, votre application doit afficher quels chats ont encore un chapeau
# sur la tête et dites à Nicolas qu’il a besoin de nouveaux passe-temps.

cat_ls = [0] * 10000


def flip(x):
    if x == 0:
        x = 1
        return x
    else:
        x = 0
        return x


def main():
    turn = 0
    turn_limit = len(cat_ls)
    try:
        while turn < turn_limit:
            for i in range(len(cat_ls)):
                current_cat = cat_ls[i + turn]
                cat_ls[i + turn] = flip(current_cat)
                print(cat_ls)
                turn += 1
    except IndexError:
        sys.exit("The program has finished.")


if __name__ == "__main__":
    main()

