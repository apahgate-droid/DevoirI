# astar.py
import heapq   # Module pour gérer une file de priorité (tas binaire)


def manhattan(a, b):
    """
    Calcule la distance de Manhattan entre deux points.
    Utilisée comme heuristique pour l'algorithme A*.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(maze):
    """
    Implémentation de l'algorithme A* pour trouver
    le plus court chemin dans un labyrinthe.
    """

    # Accès à la grille et à la taille du labyrinthe
    grid = maze.grid
    size = maze.size

    # Position de départ et d'arrivée
    start = (1, 1)
    goal = (size - 2, size - 2)

    # Ensemble des nœuds à explorer (file de priorité)
    open_set = []
    heapq.heappush(open_set, (0, start))

    # Dictionnaire des parents pour reconstruire le chemin
    parent = {}

    # Coût réel depuis le départ jusqu'à chaque nœud
    g_score = {start: 0}

    # Ensemble des nœuds déjà explorés
    visited = set()

    # Compteur du nombre de nœuds explorés
    explored_nodes = 0

    # Ordre d'exploration : droite, bas, gauche, haut
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Boucle principale de l'algorithme A*
    while open_set:
        # Récupère le nœud avec le plus petit coût f
        _, current = heapq.heappop(open_set)
        explored_nodes += 1

        # Si l'objectif est atteint, on arrête la recherche
        if current == goal:
            break

        # Marque le nœud comme exploré
        visited.add(current)
        x, y = current

        # Exploration des voisins
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            neighbor = (nx, ny)

            # Vérifie que le voisin est dans les limites du labyrinthe
            if 0 <= nx < size and 0 <= ny < size:

                # Ignore les murs
                if grid[nx][ny] == '#':
                    continue

                # Coût pour atteindre le voisin depuis le départ
                tentative_g = g_score[current] + 1

                # Ignore le voisin si un meilleur chemin existe déjà
                if neighbor in visited and tentative_g >= g_score.get(neighbor, float('inf')):
                    continue

                # Met à jour le chemin si une meilleure solution est trouvée
                if tentative_g < g_score.get(neighbor, float('inf')):
                    parent[neighbor] = current
                    g_score[neighbor] = tentative_g

                    # Calcul du coût total f = g + h
                    f_score = tentative_g + manhattan(neighbor, goal)

                    # Ajoute le voisin à la file de priorité
                    heapq.heappush(open_set, (f_score, neighbor))

    # Reconstruction du chemin depuis l'arrivée jusqu'au départ
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = parent[node]
    path.append(start)

    # Inverse le chemin pour l'avoir dans le bon sens
    path.reverse()

    # Retourne le chemin, les nœuds visités et le nombre de nœuds explorés
    return path, visited, explored_nodes