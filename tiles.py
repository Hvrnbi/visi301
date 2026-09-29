import pygame, os
from variables import *


class Tile:
    def __init__(self, x: int, y: int, width: int, height: int, tiletype: str, display: pygame.display):
        """A class for hexagonal tiles"""
        self.x: int = x
        self.y: int = y
        self.width = width
        self.height = height
        self.tiletype: str = tiletype
        self.display: pygame.display = display

    def draw(self):
        """Draw the tile"""
        image = pygame.transform.scale(HEXA, (self.width, self.height))
        self.display.blit(image, (self.x, self.y))
        
        
