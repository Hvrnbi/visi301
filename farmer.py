import pygame
from tiles import *
from variables import *
from world import World
from player import Player

def create_farmer(world, display, player):
    """Crée un fermier sur une tuile au bord de la map"""
    random_border_tile_example = world.random_border_tile(world.border_tiles(world.tiles_list))
    farmer = Farmer(random_border_tile_example.x, random_border_tile_example.y, world, display, player)
    return farmer

def farmers_control(world, player, display):
    """Permet de controler l'apparition des fermiers, et de moduler leur nombre, ainsi que le moment ou ils apparraissent.
       On peut maintenant créer des vagues de fermiers en fonction du nombre de poussins"""
    if player.piou_piou_number in [0, 1, 2]:
        if world.egg == 4:
            world.farmers.append(create_farmer(world, display, player))
    elif player.piou_piou_number in [3, 4, 5]:
        if world.egg == 2:
            world.farmers.append(create_farmer(world, display, player))
    elif player.piou_piou_number > 5:
        if world.egg == 2:
            world.farmers.append(create_farmer(world, display, player))
        if world.egg == 4:
            world.farmers.append(create_farmer(world, display, player))
        if world.egg == 9:
            world.farmers.append(create_farmer(world, display, player))



class Farmer:
    def __init__(self, x: int, y: int, world: World, display: pygame.display, player: Player):
        """Un fermier, avec ses coordonnées (x, y)"""
        self.display = display
        self.x: int = x
        self.y: int = y
        self.world: World = world
        self.neighbors_list: list = self.neighbors(self.x, self.y, self.world)
        self.origin: Tile = {"x": self.find_current_tile().x, "y": self.find_current_tile().y}
        self.destination: Tile = world.pos_list[0]
        self.goal_done: bool = self.is_at_nest()
        self.alive: bool = True
        self.tuile_traversees = 0
        self.player = player
        self.numero = len(world.farmers)
        self.color = FARMER_COLOR[self.numero % len(FARMER_COLOR)]

    def draw(self):
        """Affiche le fermier"""
        if self.alive :
            image = pygame.transform.scale(FARMER, (self.world.tile_width, self.world.tile_height))
            self.display.blit(image, (self.x - self.world.tile_width // 2, self.y - self.world.tile_height // 2))  
            self.tuile_traversees += 1



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
        while not found and i < len(self.world.pos_list):
            if self.x - 8 < self.world.pos_list[i]["x"] < self.x + 8 and self.y - 8 < self.world.pos_list[i]["y"] < self.y + 8 :
                found = True
            else:
                i += 1

        if found:
            return self.world.tiles_list[i]
        else:
            print("Aucune tuile trouvée")

    def is_at_nest(self) -> bool:
        """Renvoie True si le fermier est au nid False sinon. Met automatiquement a jour "self.goal_done" """
        res = False
        if self.find_current_tile() == self.world.tiles_list[0]:
            res = True
            self.goal_done = True
            self.world.egg = 0
            self.world.tiles_list[0].tiletype = "nest"
        return res

    def is_at_origin(self) -> bool:
            """Renvoie True si le fermier est au nidn False sinon"""
            res = False
            if {"x": self.find_current_tile().x, "y":self.find_current_tile().y} == self.origin:
                res = True
            return res

    def change_destination(self) -> None:
        """Change la tuile destination du fermier lorsqu'il touche le nid"""
        if self.is_at_nest() :
            self.destination = self.origin
        elif self.is_at_origin():
            self.destination = self.world.pos_list[0]
        

    def way_to_follow(self) -> None:
        """Renvoie les coordonées par lesquelles va passer le fermier sous forme d'une liste"""
        return None

    def disappear(self) -> None:
        """Fais disparaitre le fermier si il a atteint le nid et si il est revenu à son point de départ"""
        if self.is_at_origin() and self.goal_done :
            self.alive = False
        return None

    def action(self) -> None:
        if self.alive:
            self.change_destination()
            self.x, self.y = self.next_tuile()
            self.neighbors_list = self.neighbors(self.x, self.y, self.world)
            self.find_current_tile()
            self.disappear()

            if self.collision():
                self.destination = self.origin
                self.goal_done = True

    def collision(self) -> bool:
        """Renvoie True si le fermier va se faire picorer les jambes, False sinon"""            
        if self.player.piou_piou_number == 0:
            return (self.player.x, self.player.y) in [(self.x, self.y), self.next_tuile()]
        else:
            return (self.x, self.y) in self.player.pos_history[-(self.player.piou_piou_number + 1):] or self.next_tuile() in self.player.pos_history[-(self.player.piou_piou_number + 1):]

    def closest_neighbor(self, x: int, y: int, destination: dict) -> tuple:
        """Renvoie la tuile voisine qui est la plus proche de la destination"""
        res = (x, y)
        distance_min = WINDOW_WIDTH ** 2 * 2

        for tuile in self.neighbors(x, y, self.world):
            nx, ny = tuile
            dx = nx - destination["x"]
            dy = ny - destination["y"]
            distance = dx ** 2 + dy ** 2

            if distance_min > distance:
                distance_min = distance
                res = tuile

        return res

    def next_tuile(self) -> tuple:
        """Renvoie les coordonnées sur lesquelles le fermier doit aller pour se rapprocher le plus de sa destination"""
        return self.closest_neighbor(self.x, self.y, self.destination)
    
    def same_position(self, x: int, y: int, tile: dict) -> bool:
        """Renvoie True si la position (x, y) est sur la tuile en paramètre"""
        return 8 > abs(x - tile["x"]) and 8 > abs(y - tile["y"])

    def path_to(self, x: int, y: int, destination: dict) -> list :
        """Renvoie la liste des positions par lesquelles on passe pour aller de (x, y) à la destination"""
        path = []
        while not self.same_position(x, y, destination) and 100 > len(path):
            x, y = self.closest_neighbor(x, y, destination)
            path.append((x, y))
        return path

    def future_path(self) -> list:
        """Renvoie toutes les positions par lesquelles le fermier va passer"""
        if not self.alive:
            return []

        nest = self.world.pos_list[0]

        if self.goal_done:
            return self.path_to(self.x, self.y, self.origin)

        way = self.path_to(self.x, self.y, self.destination)
        if way:
            way.pop(-1)
        return way

        
    def draw_path(self):
        """Va afficher le chemin d'un fermier"""
        image = pygame.transform.scale(PATH_TILES[self.numero % len(PATH_TILES)], (self.world.tile_width, self.world.tile_height))
        for x, y in self.future_path():
            self.display.blit(image, (x - self.world.tile_width // 2, y - self.world.tile_height // 2))