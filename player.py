import pygame
from tiles import *
from variables import *
from world import World


class Player:
    def __init__(self, x: int, y: int, world: World, display: pygame.display):
        """Un joueur, avec ses coordonnées (x, y)"""
        self.display = display
        self.x: int = x
        self.y: int = y
        self.picture: str = "player"
        self.world: World = world

    def draw(self, tile: dict):
        """Affiche le joueur"""
        image = pygame.transform.scale(PLAYER, (self.world.tile_width, self.world.tile_height))
        self.display.blit(image, (tile['x'] - self.world.tile_width // 2, tile['y'] - self.world.tile_height // 2))  #la valeur ici est arbitraire mais marche. elle est la pour centrer l'affichage du joueur sur une tuile, a changer dans le futur
    
    