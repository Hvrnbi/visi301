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

    def next_tuile(self, tuile_dest: Tile, world: World) -> tuple:
            """Prend la tuile à atteindre et renvoie les coordonnées de la tuile sur laquelle le fermier doit aller pour s'en rapprocher le plus"""
            res = (0, 0)
            x_nest = tuile_dest["x"]
            y_nest = tuile_dest["y"]
    
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
            while not found and i < len(self.world.pos_list):
                if self.world.pos_list[i] == {"x": self.x, "y": self.y}:
                    found = True
                else:
                    i += 1
    
            if found:
                return self.world.tiles_list[i]
            else:
                print("Aucune tuile trouvée")


    def way_to_follow(self, world: World):
        """Renvoie les coordonées par lesquelles va passer le fermier sous forme d'une liste"""
        return None
        