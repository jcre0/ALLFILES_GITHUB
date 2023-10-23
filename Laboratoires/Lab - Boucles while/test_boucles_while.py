import pytest
import boucles_while
from contextlib import redirect_stdout
import io


@pytest.mark.parametrize("nombre", [
    [1, 2, 3, 4, 5, 0],
    [-4, -10, 5, 50, 6, 0]
])
def test_statistiques_nombre(monkeypatch, nombre):
    inputs = iter(nombre)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert [min(nombre[:-1]), max(nombre[:-1])] == sorted(boucles_while.statistiques_nombre())


@pytest.mark.parametrize("nb_a_trouver, nb_essaye, nb_tentative", [
    (5, [1, 2, 5], 3),
    (-4, [1, -8, 12, 16, -4], 5)
])
def test_quoi_les_chances(monkeypatch, nb_a_trouver, nb_essaye, nb_tentative):
    inputs = iter(nb_essaye)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    f = io.StringIO()
    with redirect_stdout(f):
        reponse = boucles_while.quoi_les_chances(nb_a_trouver)
    assert nb_tentative == reponse


@pytest.mark.parametrize("dette, remboursement, nb_remboursements", [
    (1000, [50, 900, 100], 3),
    (20, [2, 12, 3, 1, 2], 5)
])
def test_payer_dette(monkeypatch, dette, remboursement, nb_remboursements):
    inputs = iter(remboursement)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert nb_remboursements, dette / nb_remboursements == boucles_while.payer_dette(dette)
