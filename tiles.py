import pygame, os
from variables import *


class Tile:
    def __init__(self, x: int, y: int, width: int, height: int, tiletype: str, display: pygame.display):
        """Crée une tuile hexagonale, x et y sont les coordonnées du centre de la tuile."""
        self.x: int = x
        self.y: int = y
        self.width = width
        self.height = height
        self.tiletype: str = tiletype
        self.display: pygame.display = display

    def draw(self):
        """Affiche la tuile"""
        if self.tiletype == "seed" :
            image = pygame.transform.scale(SEED, (self.width, self.height))
        elif self.tiletype == "nest":
            image = pygame.transform.scale(NEST, (self.width, self.height))
        elif self.tiletype == "egg1":
            image = pygame.transform.scale(EGG1, (self.width, self.height))
        elif self.tiletype == "egg2":
            image = pygame.transform.scale(EGG2, (self.width, self.height))
        elif self.tiletype == "egg3":
            image = pygame.transform.scale(EGG3, (self.width, self.height))
        elif self.tiletype == "egg4":
            image = pygame.transform.scale(EGG4, (self.width, self.height))
        elif self.tiletype == "egg5":
            image = pygame.transform.scale(EGG5, (self.width, self.height))
        else :
            image = pygame.transform.scale(HEXA, (self.width, self.height))
        self.display.blit(image, (self.x - self.width // 2, self.y - self.height // 2))

        
        