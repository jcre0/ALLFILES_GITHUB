import math


def arrondir_haut(nombre: float) -> int:
    """Arrondit au plus haut entier.

    :param nombre: Un nombre réel.
    :return: L'entier supérieur.
    :raises TypeError: Le nombre n'est pas valide.
    """
    if not isinstance(nombre, (int, float)):
        raise TypeError("Votre nombre n'est pas valide.")
    return math.ceil(nombre)


def arrondir_bas(nombre: float) -> int:
    """Arrondit au plus bas entier.

    :param nombre: Un nombre réel.
    :return: L'entier inférieur.
    :raises TypeError: Le nombre n'est pas valide.
    """
    if not isinstance(nombre, (int, float)):
        raise TypeError("Votre nombre n'est pas valide.")
    return math.floor(nombre)


def calculer_produit(ls_nombres: list) -> float:
    """Multiplie entre eux les nombres d'une liste.

    :param ls_nombres: Une liste de nombres réels.
    :return: Le produit de tous les nombres.
    :raises TypeError: La liste n'est pas valide.
    """
    for nombre in ls_nombres:
        if type(nombre) not in (float, int):
            raise TypeError(f"Votre liste n'est pas valide. {nombre} n'est pas un nombre.")
    return math.prod(ls_nombres)
