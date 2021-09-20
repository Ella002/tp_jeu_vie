from typing import List

class Grille:

    def __init__ (self):
        self.width: int = 0
        self.height: int = 0
        self.table: List[List[bool]] = []
        #table[y][x], x va vers la droite, y vers le bas

    def from_string(self, s : str) -> None :
        """
        Charge une grille depuis un string au format

        largeur hauteur
        1ere ligne
        ...
        """
        lines: List[str] = s.split("\n")
        fst_line: List[str] = lines[0].split(" ")
        self.width = int(fst_line[0])
        self.height = int(fst_line[1])

        for l in lines[1:self.height+1]:
            self.table.append([c=='*' for c in l[:self.width]])

    def is_alive(self, x: int, y:int) -> bool :
        """
        Renvoie l'etat d'abscisse x et d'ordonnee y.
        """
        return self.table[y][x]

    def count_neighboors(self, x: int, y: int) -> int :
        """
        Compte le nombre de voisins (horizontal, vertical, diagonal)
        d'une cellule
        """

        cpt : int = 0
        min_x : int = max(0, x - 1)
        max_x : int = min(x + 1, self.width-1)
        min_y : int = max(0, y - 1)
        max_y : int = min(y + 1, self.height-1)

        x_tmp : int
        y_tmp : int
        for x_tmp in range(min_x, max_x+1):
            for y_tmp in range(min_y, max_y+1):
                if self.is_alive(x_tmp, y_tmp) and not (x_tmp == x and y_tmp == y):
                    cpt += 1
        return cpt
