# dfs.py

def dfs(maze):
    # Récupération de la grille du labyrinthe
    grid = maze.grid
    
    # Taille du labyrinthe (supposé carré)
    size = maze.size

    # Position de départ (entrée du labyrinthe)
    start = (1, 1)
    
    # Position de sortie (objectif)
    goal = (size - 2, size - 2)

    # Pile pour l'algorithme DFS (Last In, First Out)
    stack = [start]
    
    # Ensemble des noeud  visitees
    visited = set([start])
    
    # Dictionnaire pour mémoriser le parent de chaque case
    # (utile pour reconstruire le chemin final)
    parent = {}

    # Compteur du nombre de nœuds explorés
    explored_nodes = 0

    # Ordre d'exploration : droite, bas, gauche, haut
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Boucle principale : tant qu'il reste des cases à explorer
    while stack:
        # Retire la dernière case ajoutée à la pile
        current = stack.pop()
        explored_nodes += 1

        # Si on atteint l'objectif, on arrête la recherche
        if current == goal:
            break

        # Coordonnées de la case courante
        x, y = current

        # Exploration des voisins selon l'ordre défini
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Vérifie que la case voisine est dans les limites du labyrinthe
            if (0 <= nx < size and 0 <= ny < size):
                # Vérifie que ce n'est pas un mur et qu'elle n'a pas été visitée
                if grid[nx][ny] != '#' and (nx, ny) not in visited:
                    visited.add((nx, ny))          # Marque la case comme visitée
                    parent[(nx, ny)] = current     # Enregistre son parent
                    stack.append((nx, ny))         # Ajoute la case à la pile

    # Reconstruction du chemin depuis l'objectif jusqu'au départ
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = parent[node]
    path.append(start)

    # Inverse le chemin pour l'avoir du départ à l'objectif
    path.reverse()

    # Retourne :
    # - le chemin trouvé
    # - l'ensemble des cases visitées
    # - le nombre total de nœuds explorés
    return path, visited, explored_nodes