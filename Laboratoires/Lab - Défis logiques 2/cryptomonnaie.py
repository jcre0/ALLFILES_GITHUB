"""
Nicolas gère des serveurs qui minent de la cryptomonnaie. Il a un nombre variable de calculs à effectuer et de
serveurs pour les faire.
L’information sur son travail ainsi que ses ressources lui est transmis sous forme de 
tuple (x, y) où x représente le nombre de serveurs qu’il a de disponible et y le nombre de calculs à faire.

Important : 
Nicolas veut toujours répartir le travail le plus équitablement possible sur ses serveurs pour de meilleures
performances.
Si les calculs ne peuvent pas être divisés également ce sont les premiers serveurs qui prennent un calcul
supplémentaire.

Ce qu’il faut obtenir comme résultat est une liste de liste qui affiche quels calculs sont
effectués sur quels serveurs.

Exemples : 
Nicolas a 2 serveurs et 4 calculs à faire.
Il reçoit (2, 4) et la réponse doit être [[0, 1], [2, 3]]

Une autre journée, Nicolas a 3 serveurs et 3 calculs à faire.
Il reçoit (4, 3) et la réponse doit être [[0], [1], [2], []]

Quelques jours plus tard, un autre scénario de 4 serveurs et 10 calculs.
Il reçoit (4, 10) et la réponse doit être  [[0, 1, 2], [3, 4, 5], [6, 7], [8, 9]]

Vous devez créer une application qui va répartir la charge des serveurs selon les préférences de Nicolas. 
Ne vous en faites pas, les demandes sont toujours des entiers positifs.
"""


def main():
    ls_a_gerer = [
        (2, 4), (3, 3), (3, 9),
        (2, 5), (4, 10), (4, 5),
        (1, 1), (2, 1), (5, 4), (5, 1)
    ]

    ls_reponse_prof = [
        [[0, 1], [2, 3]],
        [[0], [1], [2]],
        [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
        [[0, 1, 2], [3, 4]],
        [[0, 1, 2], [3, 4, 5], [6, 7], [8, 9]],
        [[0, 1], [2], [3], [4]],
        [[0]],
        [[0], []],
        [[0], [1], [2], [3], []],
        [[0], [], [], [], []]
    ]

    # Insérer code ici
    pass


if __name__ == '__main__':
    main()


