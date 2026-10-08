from tiles import *
from variables import *
from random import choice


class World:
    def __init__(self, display: pygame.display, nb_col: int, nb_row: int, gap: int):
        """Un monde avec le nombre de colonnes et de lignes données, et l'espacement donné entre les tuiles"""
        self.display = display
        self.nb_col = nb_col
        self.nb_row = nb_row
        self.gap = gap
        self.tile_width, self.tile_height = self.tile_size()
        self.pos_list = self.position_of_tiles((WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.tiles_list = self.create_tiles()
        self.left_border = min([tile["x"] for tile in self.pos_list])
        self.right_border = max([tile["x"] for tile in self.pos_list])
        self.top_border = min([tile["y"] for tile in self.pos_list])
        self.bottom_border = max([tile["y"] for tile in self.pos_list])
        self.border_tiles_list = self.border_tiles(self.tiles_list)

    
    def draw(self):
        """Dessine les tuiles du monde"""
        for tile in self.tiles_list:
            tile.draw()


    def random_tile_type(self) -> str:
        """Renvoie une chaine de caractère contenant 'green' ou 'seed' avec une probabilité respective de 80% et 20%"""
        t_type = ["green"] * 4 + ["seed"]
        return choice(t_type)

    
    def create_tiles(self):
        """Renvoie une liste avec toutes les tuiles du monde, générées en partie aléatoirement"""
        res = []
        # Tuile centrale
        res.append(Tile(self.pos_list[0]["x"], self.pos_list[0]["y"], self.tile_width, self.tile_height, "green", self.display))
        # Toutes les autres
        for pos in self.pos_list[1:]:
            res.append(Tile(pos["x"], pos["y"], self.tile_width, self.tile_height, self.random_tile_type(), self.display))
        return res


    def tile_size(self) -> tuple:
        """Renvoie un tuple contenant la largeur et la hauteur d'une tuile en fonction du nombre de lignes, de colonnes, et de l'espacement entre le tuiles"""
        width = (WINDOW_WIDTH - self.nb_col * self.gap) // self.nb_col
        height = (WINDOW_HEIGHT - self.nb_row * self.gap) // self.nb_row

        # On cale le plus grand sur le plus petit pour conserver la forme des tuiles et ne pas dépasser d'un côté
        if height < 0.86 * width:
            width = height // 0.86
        else:
            height = round(width * 0.86)

        return (width, height)


    def position_of_tiles(self, center: tuple) -> list:
        """Renvoie la position du centre de toutes les tuiles du monde en fonction des paramètres donnés"""
        # Le nombre de colonnes doit être impair
        if self.nb_col % 2 != 0:
            self.nb_col += 1

        res = []
        x = center[0]

        # Si le nombre de lignes est pair
        if self.nb_row % 2 == 0:
            # Colonne centrale
            res += self.position_of_odd_columns(self.nb_row - 1, x)
            # Colonnes paires de droite
            x += (self.tile_width * 3) // 4 + self.gap
            res += self.position_of_even_columns(self.nb_row, x)
            for i in range(self.nb_col // 4 - 1):
                x += (self.tile_width * 3) // 2 + 2 * self.gap
                res += self.position_of_even_columns(self.nb_row, x)

            # Colonnes paires de gauche
            x = center[0] - (self.tile_width * 3) // 4 - self.gap
            res += self.position_of_even_columns(self.nb_row, x)
            for i in range(self.nb_col // 4 - 1):
                x -= (self.tile_width * 3) // 2 + 2 * self.gap
                res += self.position_of_even_columns(self.nb_row, x)

            # Colonnes impaires de droite
            x = center[0]
            for i in range(self.nb_col // 4):
                x += (self.tile_width * 3) // 2 + 2 * self.gap
                res += self.position_of_odd_columns(self.nb_row - 1, x)

            # Colonnes impaires de gauche
            x = center[0]
            for i in range(self.nb_col // 4):
                x -= (self.tile_width * 3) // 2 + 2 * self.gap
                res += self.position_of_odd_columns(self.nb_row - 1, x)

        # Si le nombre de lignes est impair
        else:
            # Colonne centrale
            res += self.position_of_odd_columns(self.nb_row, x)
            # Colonnes paires de droite
            x += (self.tile_width * 3) // 4 + self.gap
            res += self.position_of_even_columns(self.nb_row - 1, x)
            for i in range(self.nb_col // 4 - 1):
                x += (self.tile_width * 3) // 2 + 2 * self.gap
                res += self.position_of_even_columns(self.nb_row - 1, x)

            # Colonnes paires de gauche
            x = center[0] - (self.tile_width * 3) // 4 - self.gap
            res += self.position_of_even_columns(self.nb_row - 1, x)
            for i in range(self.nb_col // 4 - 1):
                x -= (self.tile_width * 3) // 2 + 2 * self.gap
                res += self.position_of_even_columns(self.nb_row - 1, x)

            # Colonnes impaires de droite
            x = center[0]
            for i in range(self.nb_col // 4 - 1):
                x += (self.tile_width * 3) // 2 + 2 * self.gap
                res += self.position_of_odd_columns(self.nb_row, x)

            # Colonnes impaires de gauche
            x = center[0]
            for i in range(self.nb_col // 4 - 1):
                x -= (self.tile_width * 3) // 2 + 2 * self.gap
                res += self.position_of_odd_columns(self.nb_row, x)

        return res


    def position_of_odd_columns(self, nb_row: int, x: int) -> list:
        """Renvoie la position des tuiles dans une colonne au nombre de tuiles impair"""
        y = WINDOW_HEIGHT // 2

        # Tuile du milieu
        res = [{"x": x, "y": y}]

        # Tuiles en dessous du milieu
        for i in range(nb_row // 2):
            y += self.tile_height + self.gap
            res.append({"x": x, "y": y})
        
        y = WINDOW_HEIGHT // 2
        # Tuiles en dessous du milieu
        for i in range(nb_row // 2):
            y -= self.tile_height + self.gap
            res.append({"x": x, "y": y})

        return res


    def position_of_even_columns(self, nb_row: int, x: int) -> list:
        """Renvoie la position des tuiles dans une colonne au nombre de tuiles pair"""
        res = []

        # Tuiles du bas
        y = WINDOW_HEIGHT // 2 + self.gap // 2 + self.tile_height // 2
        res.append({"x": x, "y": y})
        for i in range(nb_row // 2 - 1):
            y += self.tile_height + self.gap
            res.append({"x": x, "y": y})

        # Tuiles du haut
        y = WINDOW_HEIGHT // 2 - self.gap // 2 - self.tile_height // 2
        res.append({"x": x, "y": y})
        for i in range(nb_row // 2 - 1):
            y -= self.tile_height + self.gap
            res.append({"x": x, "y": y})

        return res

    def border_tiles(self, tiles_list: list) -> list:
        """Renvoie une liste contenant les tuiles des bordures de la map, les tuiles étant les plus éloignées concernant celles d'en haut et d'en bas"""
        res = []
        for tuile in tiles_list:
            if tuile.y == self.top_border or tuile.y == self.bottom_border:
                res.append(tuile)
            elif tuile.x == self.left_border or tuile.x == self.right_border:
                res.append(tuile)                               #######################A EFFACER ####################################
        return res

    def random_border_tile(self, border_tiles_list: list) -> list:
        """Renvoie une tuile aléatoire du bord de la map"""
        res = choice(border_tiles_list)
        return res









#           res.append(Tile(self.pos_list[0]["x"], self.pos_list[0]["y"], self.tile_width, self.tile_height, "green", self.display))