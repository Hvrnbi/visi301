import pygame
from tiles import *
from world import World


class Player:
    def __init__(self, x: int, y: int, world: World, display: pygame.display):
        """Un joueur, avec ses coordonnées (x, y)"""
        self.display = display
        self.x: int = x
        self.y: int = y
        self.picture: str = "player"
        self.world: World = world

    def draw(self):
        """Affiche le joueur"""
        image = pygame.transform.scale(PLAYER, (self.world.tile_width, self.world.tile_height))
        self.display.blit(image, (self.x - self.world.tile_width // 2, self.y - self.world.tile_height // 2))  #la valeur ici est arbitraire mais marche. elle est la pour centrer l'affichage du joueur sur une tuile, a changer dans le futur
    
    def move(self, direction: str):
        """Modifie les coordonnées x et y du joueur en fonction de la direction donnée"""
        if direction == "up":
            if self.y - self.world.gap - self.world.tile_height >= self.world.top_border:   # Il faut que ça soit supérieur parce que les coos descendent 
                self.y -= self.world.gap + self.world.tile_height
        elif direction == "down":
            if self.y + self.world.gap + self.world.tile_height <= self.world.bottom_border:    # Inversement ici
                self.y += self.world.gap + self.world.tile_height

    