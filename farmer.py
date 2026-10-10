import pygame
from tiles import *
from variables import *
from world import World

class Farmer:
    def __init__(self, x: int, y: int, world: World, display: pygame.display):
        """Un fermier, avec ses coordonnées (x, y)"""
        self.display = display
        self.x: int = x
        self.y: int = y
        self.world: World = world
        self.neighbors_list: list = self.neighbors(self.x, self.y, self.world)
        self.origin: Tile = self.find_current_tile()
        self.destination: Tile = world.pos_list[0]

    def draw(self):
        """Affiche le fermier"""
        image = pygame.transform.scale(FARMER, (self.world.tile_width, self.world.tile_height))
        self.display.blit(image, (self.x - self.world.tile_width // 2, self.y - self.world.tile_height // 2))  



    def neighbors(self, x: int, y: int, world: World) -> list:
        """Prend la position d'une tuile ((x, y), qui n'est pas son centre), et renvoie la position des tuiles adjacentess dans une liste"""
        x_centre = x
        y_centre = y

        res = []

        top_tile = (x_centre, y_centre - world.gap - world.tile_height)
        bottom_tile = (x_centre, y_centre  + world.gap + world.tile_height)
        left_high_tile = (x_centre - world.gap - 3 * world.tile_width // 4, y_centre - world.gap // 2 - world.tile_height // 2)
        left_bottom_tile = (x_centre - world.gap - 3 * world.tile_width // 4, y_centre + world.gap // 2 + world.tile_height // 2)
        right_high_tile = (x_centre + world.gap + 3 * world.tile_width // 4, y_centre - world.gap // 2 - world.tile_height // 2)
        right_bottom_tile = (x_centre + world.gap + 3 * world.tile_width // 4, y_centre + world.gap // 2 + world.tile_height // 2)

        res.append(top_tile)
        res.append(bottom_tile)
        res.append(left_high_tile)
        res.append(left_bottom_tile)
        res.append(right_high_tile)
        res.append(right_bottom_tile)
        
        return res

    def next_tuile(self) -> tuple:
            """Prend la tuile à atteindre et renvoie les coordonnées de la tuile sur laquelle le fermier doit aller pour s'en rapprocher le plus"""
            res = (0, 0)
            x_nest = self.destination["x"]
            y_nest = self.destination["y"]
    
            min = WINDOW_WIDTH ** 2 * 2
            for tuile in self.neighbors_list:
                x, y = tuile   
    
                x = abs(x - x_nest)
                y = abs(y - y_nest)
    
                hypo = x ** 2 + y ** 2
    
                if min > hypo :
                    min = hypo
                    res = tuile

            return(res)

    def find_current_tile(self):
            """Renvoie la tuile sur laquelle se trouve le fermier"""
            found = False
            i = 0
            for tile in self.world.pos_list:
                if  SPACE > abs(tile["x"] - self.x) and SPACE > abs(tile["y"] - self.y):
                    found = True

                if found:
                    return tile
            else:
                print("Aucune tuile trouvée")

    def is_at_nest(self) -> bool:
        """Renvoie True si le fermier est au nidn False sinon"""
        res = False
        if self.find_current_tile() == self.world.pos_list[0]:
            res = True
        return res

    def is_at_origin(self) -> bool:
            """Renvoie True si le fermier est au nidn False sinon"""
            res = False
            if self.find_current_tile() == self.origin:
                res = True
            return res

    def change_destination(self) -> None:
        """Change la tuile destination du fermier lorsqu'il touche le nid"""
        if self.is_at_nest() :
            self.destination = self.origin
        elif self.is_at_origin():
            self.destination = self.world.pos_list[0]
        

    def way_to_follow(self):
        """Renvoie les coordonées par lesquelles va passer le fermier sous forme d'une liste"""
        return None
        