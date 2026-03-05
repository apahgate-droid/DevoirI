# main.py

import time              # Pour mesurer le temps d'execution
from maze import Maze    # Classe representant le labyrinthe
from dfs import dfs      # Algorithme Depth First Search
from bfs import bfs      # Algorithme Breadth First Search
from astar import astar  # Algorithme A*
import copy              # Pour creer une copie independante du labyrinthe


def run_algorithm(name, algo_func, maze):
    """
    Execute un algorithme de recherche sur une copie du labyrinthe,
    mesure ses performances et affiche les resultats.
    """

    # Creation d'une copie du labyrinthe pour eviter de le modifier
    maze_copy = copy.deepcopy(maze)

    # Demarrage du chronometre
    start_time = time.perf_counter()
    
    # Execution de l'algorithme (DFS, BFS ou A*)
    path, visited, explored = algo_func(maze_copy)
    
    # Arret du chronometre
    end_time = time.perf_counter()

    # Marquage des cases explorees par l'algorithme
    for (x, y) in visited:
        if maze_copy.grid[x][y] == '.':
            maze_copy.grid[x][y] = 'p'

    # Marquage du chemin final trouvé
    for (x, y) in path:
        if maze_copy.grid[x][y] not in ('S', 'G'):
            maze_copy.grid[x][y] = '*'

    # Affichage des resultats
    print(f"\n===== {name} =====")
    maze_copy.display()
    print("\nChemin :", path)
    print("Nœuds explores :", explored)
    print("Longueur du chemin :", len(path))
    print("Temps (ms) :", round((end_time - start_time) * 1000, 3))

    # Retourne les statistiques pour le tableau comparatif
    return explored, len(path), (end_time - start_time) * 1000


def main():
    """
    Fonction principale :
    - Génère un labyrinthe
    - Exécute DFS, BFS et A*
    - Compare leurs performances
    """

    # Création du labyrinthe avec une graine fixe (résultats reproductibles)
    maze = Maze(seed=42)
    maze.generate()

    # Liste pour stocker les résultats des algorithmes
    results = []

    # Exécution des différents algorithmes
    results.append(("DFS",) + run_algorithm("DFS", dfs, maze))
    results.append(("BFS",) + run_algorithm("BFS", bfs, maze))
    results.append(("A* (Manhattan)",) + run_algorithm("A*", astar, maze))

    # Affichage du tableau comparatif final
    print("\n===== TABLEAU COMPARATIF =====")
    print(f"{'Algorithme':<20}{'Noeuds':<10}{'Longueur':<12}{'Temps (ms)':<10}")
    print("-" * 55)
    for name, nodes, length, time_ms in results:
        print(f"{name:<20}{nodes:<10}{length:<12}{round(time_ms,3):<10}")


# Point d'entrée du programme
if __name__ == "__main__":
    main()