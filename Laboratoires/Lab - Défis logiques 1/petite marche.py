# Une petite marche en attendant
# Nicolas habite la ville de Cartésia, là où toutes les routes forment une grille parfaite, 
# un peu comme Manhattan en fait. Il arrive 10 minutes en avance à son rendez-vous et 
# n’a pas envie d’attendre sans bouger. Heureusement, 
# il s’est programmé une petite application qui lui génère des parcours de marche sur son téléphone. 
# Nicolas veut marcher 10 minutes pour être de retour à l’heure et l’endroit exact du rendez-vous. 

# L’application de marche lui envoie donc ces parcours : 
# ls_parcours = [
# ['n'],
# ['n','s','n','s','n','s','n','s','n','s'],
# ['n','s'],
# ['e','w','e','w','n','s','n','s','e','w'],
# ['n','s','n','s','n','s','n','s','n','s','n','s'],
# ['n','s','e','w','n','s','e','w','n','s'],
# ['n','s','e','w','n','s','e','w','n','s','e','w','n','s','e','w'],
# ['n','s','n','s','n','s','n','s','n','n'], 
# ['e','e','e','w','n','s','n','s','e','w'],
# ['s','e','w','n','n','s','e','w','n','s']
# ]
    
# Votre application doit afficher lesquels de ces parcours répondent à son besoin.

# Important :
# Chaque parcours (liste) contient uniquement les caractères [n, s, e, w].
# Un parcours n’est jamais vide.
# Il faut marcher 1 minute à chaque indication par le parcours.

# Liste de liste(parcours) à vérifier
ls_parcours = [
['n'],
['n','s','n','s','n','s','n','s','n','s'],
['n','s'],
['e','w','e','w','n','s','n','s','e','w'],
['n','s','n','s','n','s','n','s','n','s','n','s'],
['n','s','e','w','n','s','e','w','n','s'],
['n','s','e','w','n','s','e','w','n','s','e','w','n','s','e','w'],
['n','s','n','s','n','s','n','s','n','n'], 
['e','e','e','w','n','s','n','s','e','w'],
['s','e','w','n','n','s','e','w','n','s']
]


def main():
    # Insérer code ici
    for i in range(len(ls_parcours)):
        if len(ls_parcours[i]) * 2 < 10:
            print(ls_parcours[i])





if __name__ == '__main__':
    main()
