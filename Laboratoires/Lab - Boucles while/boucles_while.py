import sys
import textwrap
import random


def statistiques_nombre() -> tuple:
    """
    Demande des nombres et sort sur zéro (0).
    :return: Les plus grands et plus petits nombres entrés.
    """
    pass


def trouver_nombre(p_nb: int) -> int:
    """
    Demande de trouver le nombre initial et aide en donnant des indices.
    :param p_nb: Nombre à trouver.
    :return: La quantité de tentatives nécessaires.
    """
    pass


def payer_dette(p_dette: float) -> tuple:
    """
    Déduit les remboursements d'une dette et retourne des statistiques.
    :param p_dette: Montant de la dette initiale.
    :return: Le nombre de paiements et leur moyenne.
    """
    pass


def byebye():
    """ Sortir du programme."""
    print("Au revoir !")
    sys.exit()


def main():
    autre_tour = True
    while autre_tour:

        # Menu
        choix = input(textwrap.dedent(f"""
        Voici les options :    
        1. Statistiques de nombres
        2. Trouver un nombre
        3. Payer une dette
        0. Sortir

        Quel est votre choix ? """))

        # Exécuter la fonction selon le choix
        match choix:
            case "1":
                grand_nombre, petit_nombre = statistiques_nombre()
                # Affichage des statistiques
                print(textwrap.dedent("""
                Plus grand nombre : {grand_nombre}
                Plus petit nombre : {petit_nombre}
                """))

            case "2":
                nb_a_deviner = random.randint(1, 100)
                nb_tentatives = trouver_nombre(nb_a_deviner)
                print(f"\n{nb_tentatives} tentatives ont été nécessaires.\n")

            case "3":
                dette = float(input("\nQuel est le montant de la dette ? "))
                nb_paiement, moy_paiement = payer_dette(dette)
                print(textwrap.dedent(f"""
                Nombre de paiements :   {nb_paiement:8}
                Moyenne des paiements : {moy_paiement:8.2f}$
                """))

            case _:  # (else) Sortir sur 0 ou choix invalide.
                byebye()

        # Revenir au menu ?
        autre_tour = input("Voulez-vous revenir au menu ? (o/n) ").casefold() in ["o", "oui", "y", "yes"]

    byebye()


if __name__ == '__main__':
    main()
