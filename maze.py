# maze.py
import random   # Module pour la génération aléatoire

# Constantes représentant les différents types de cases
WALL = '#'     # Mur
FREE = '.'     # Passage libre
START = 'S'    # Point de départ
GOAL = 'G'     # Point d'arrivée


class Maze:
    """
    Classe représentant un labyrinthe sous forme de grille carrée
    """

    def __init__(self, size=16, seed=None):
        # Taille du labyrinthe (size x size)
        self.size = size
        
        # Graine aléatoire pour rendre la génération reproductible
        self.seed = seed
        
        # Initialisation de la grille remplie uniquement de murs
        self.grid = [[WALL for _ in range(size)] for _ in range(size)]

    def generate(self):
        """
        Génère un labyrinthe avec un chemin garanti entre S et G
        """

        # Fixe la graine si elle est fournie
        if self.seed is not None:
            random.seed(self.seed)

        # Création du point de départ
        x, y = 1, 1
        self.grid[x][y] = START

        # Creuse un chemin aléatoire mais garanti jusqu'à l'arrivée
        while (x, y) != (self.size - 2, self.size - 2):

            # Choix aléatoire du déplacement
            if random.random() < 0.5:
                # Déplacement vertical
                if x < self.size - 2:
                    x += 1
            else:
                # Déplacement horizontal
                if y < self.size - 2:
                    y += 1

            # Marque la case comme libre
            self.grid[x][y] = FREE

        # Place la case d'arrivée
        self.grid[self.size - 2][self.size - 2] = GOAL

        # Ajout de passages libres aléatoires dans le labyrinthe
        for i in range(1, self.size - 1):
            for j in range(1, self.size - 1):
                if self.grid[i][j] == WALL:
                    # 30 % de chance de transformer un mur en passage
                    if random.random() < 0.3:
                        self.grid[i][j] = FREE

    def display(self):
        """
        Affiche le labyrinthe dans la console
        """
        for row in self.grid:
            print(" ".join(row))


# Permet de tester le fichier seul
if __name__ == "__main__":
    maze = Maze(seed=42)
    maze.generate()
    maze.display()