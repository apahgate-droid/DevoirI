# bfs.py
from collections import deque  # deque permet une file FIFO efficace pour BFS

def bfs(maze):
    # Recuperation de la grille du labyrinthe
    grid = maze.grid
    
    # Taille du labyrinthe (suppose carre)
    size = maze.size

    # Position de depart (entree du labyrinthe)
    start = (1, 1)
    
    # Position d arrivee (sortie du labyrinthe)
    goal = (size - 2, size - 2)

    # Initialisation de la file FIFO avec le point de depart
    queue = deque([start])
    
    # Ensemble des cases deja visitees pour eviter les boucles
    visited = set([start])
    
    # Dictionnaire pour memoriser le parent de chaque case (utile pour reconstruire le chemin)
    parent = {}

    # Compteur du nombre de noeuds explores
    explored_nodes = 0

    # Ordre de deplacement : droite, bas, gauche, haut
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Boucle principale du BFS
    while queue:
        # On retire le premier element de la file
        current = queue.popleft()
        explored_nodes += 1

        # Si on atteint  objectif, on arrete la recherche
        if current == goal:
            break

        # Coordonnées de la case courante
        x, y = current

        # Exploration des voisins
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Vérification que la case est dans les limites de la grille
            if (0 <= nx < size and 0 <= ny < size):
                # Vérification que la case n'est pas un mur et n'a pas ete visitee
                if grid[nx][ny] != '#' and (nx, ny) not in visited:
                    visited.add((nx, ny))             # Marquer comme visitee
                    parent[(nx, ny)] = current        # Sauvegarder le parent
                    queue.append((nx, ny))            # Ajouter a la file

    # Reconstruction du chemin depuis l'objectif jusqu'au depart
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = parent[node]  # Remonter au parent
    path.append(start)

    # Inverser le chemin pour avoir start goal
    path.reverse()

    # Retourne :
    # - le chemin trouve
    # - l'ensemble des cases visitees
    # - le nombre total de noeuds explores
    return path, visited, explored_nodes