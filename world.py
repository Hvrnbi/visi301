from tiles import *
from variables import *


def create_world(display: pygame.display, nb_col: int, nb_row: int, gap: int) -> list:
    """Crée un monde avec le nombre de colonnes et de lignes données, et l'espacement donné entre les tuiles"""
    tile_width, tile_height = tile_size(nb_col, nb_row, gap)

    pos_list = position_of_tiles(nb_col, nb_row, gap, tile_height, tile_width, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

    for pos in pos_list:
        tile = Tile(pos["x"] - tile_width // 2, pos["y"] - tile_height // 2, tile_width, tile_height, "green", display)
        tile.draw()


def tile_size(nb_col: int, nb_row: int, gap: int) -> tuple:
    """Renvoie un tuple contenant la largeur et la hauteur d'une tuile en fonction du nombre de lignes, de colonnes, et de l'espacement entre le tuiles"""
    width = (WINDOW_WIDTH - nb_col * gap) // nb_col
    height = (WINDOW_HEIGHT - nb_row * gap) // nb_row

    # On cale le plus grand sur le plus petit pour conserver la forme des tuiles et ne pas dépasser d'un côté
    if height < 0.86 * width:
        width = height // 0.86
    else:
        height = round(width * 0.86)

    return (width, height)


def position_of_tiles(nb_col: int, nb_row: int, gap: int, tile_height: int, tile_width: int, center: tuple) -> list:
    """Renvoie la position du centre de toutes les tuiles du monde en fonction des paramètres donnés"""
    # Le nombre de colonnes doit être impair
    if nb_col % 2 != 0:
        nb_col += 1

    res = []
    x = center[0]

    # Si le nombre de lignes est pair
    if nb_row % 2 == 0:
        # Colonne centrale
        res += position_of_odd_columns(nb_row - 1, gap, tile_height, x)
        # Colonnes paires de droite
        x += (tile_width * 3) // 4 + gap
        res += position_of_even_columns(nb_row, gap, tile_height, x)
        for i in range(nb_col // 4 - 1):
            x += (tile_width * 3) // 2 + 2 * gap
            res += position_of_even_columns(nb_row, gap, tile_height, x)

        # Colonnes paires de gauche
        x = center[0] - (tile_width * 3) // 4 - gap
        res += position_of_even_columns(nb_row, gap, tile_height, x)
        for i in range(nb_col // 4 - 1):
            x -= (tile_width * 3) // 2 + 2 * gap
            res += position_of_even_columns(nb_row, gap, tile_height, x)

        # Colonnes impaires de droite
        x = center[0]
        for i in range(nb_col // 4):
            x += (tile_width * 3) // 2 + 2 * gap
            res += position_of_odd_columns(nb_row - 1, gap, tile_height, x)

        # Colonnes impaires de gauche
        x = center[0]
        for i in range(nb_col // 4):
            x -= (tile_width * 3) // 2 + 2 * gap
            res += position_of_odd_columns(nb_row - 1, gap, tile_height, x)

    # Si le nombre de lignes est impair
    else:
        # Colonne centrale
        res += position_of_odd_columns(nb_row, gap, tile_height, x)
        # Colonnes paires de droite
        x += (tile_width * 3) // 4 + gap
        res += position_of_even_columns(nb_row - 1, gap, tile_height, x)
        for i in range(nb_col // 4 - 1):
            x += (tile_width * 3) // 2 + 2 * gap
            res += position_of_even_columns(nb_row - 1, gap, tile_height, x)

        # Colonnes paires de gauche
        x = center[0] - (tile_width * 3) // 4 - gap
        res += position_of_even_columns(nb_row - 1, gap, tile_height, x)
        for i in range(nb_col // 4 - 1):
            x -= (tile_width * 3) // 2 + 2 * gap
            res += position_of_even_columns(nb_row - 1, gap, tile_height, x)

        # Colonnes impaires de droite
        x = center[0]
        for i in range(nb_col // 4 - 1):
            x += (tile_width * 3) // 2 + 2 * gap
            res += position_of_odd_columns(nb_row, gap, tile_height, x)

        # Colonnes impaires de gauche
        x = center[0]
        for i in range(nb_col // 4 - 1):
            x -= (tile_width * 3) // 2 + 2 * gap
            res += position_of_odd_columns(nb_row, gap, tile_height, x)

    return res


def position_of_odd_columns(nb_row: int, gap: int, tile_height: int, x: int) -> list:
    """Renvoie la position des tuiles dans une colonne au nombre de tuiles impair"""
    y = WINDOW_HEIGHT // 2

    # Tuile du milieu
    res = [{"x": x, "y": y}]

    # Tuiles en dessous du milieu
    for i in range(nb_row // 2):
        y += tile_height + gap
        res.append({"x": x, "y": y})
    
    y = WINDOW_HEIGHT // 2
    # Tuiles en dessous du milieu
    for i in range(nb_row // 2):
        y -= tile_height + gap
        res.append({"x": x, "y": y})

    return res


def position_of_even_columns(nb_row: int, gap: int, tile_height: int, x: int) -> list:
    res = []

    # Tuiles du bas
    y = WINDOW_HEIGHT // 2 + gap // 2 + tile_height // 2
    res.append({"x": x, "y": y})
    for i in range(nb_row // 2 - 1):
        y += tile_height + gap
        res.append({"x": x, "y": y})

    # Tuiles du haut
    y = WINDOW_HEIGHT // 2 - gap // 2 - tile_height // 2
    res.append({"x": x, "y": y})
    for i in range(nb_row // 2 - 1):
        y -= tile_height + gap
        res.append({"x": x, "y": y})

    return res
