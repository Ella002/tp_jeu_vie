import pytest
from jeu_vie import *

s : str ='''4 8
....
....
....
.**.
....
....
....
....'''


grille = Grille ()
grille.from_string(s)

def test_init () -> None:
    assert grille.width == 4 and grille.height == 8
    assert (grille.is_alive(1,3))
    assert (not grille.is_alive(0,0))

def test_count_neighboors():
    assert grille.count_neighboors(0,0) == 0
    assert grille.count_neighboors(1,3) == 1
    assert grille.count_neighboors(1,2) == 2
