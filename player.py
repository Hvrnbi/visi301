import pygame
from tiles import *
from variables import *


class Player:
    def __init__(self, x: int, y: int, display: pygame.display):
        """Un joueur, avec ses coordonnées (x, y)"""
        self.display = display
        self.x: int = x
        self.y: int = y
        self.width: int = self.player_size()
        self.height: int = self.player_size()
        self.picture: str = "player"

    def draw(self, tile: dict):
        """Affiche le joueur"""
        image = pygame.transform.scale(PLAYER, (self.player_size(), self.player_size()))
        tile_size = self.tile_size()
        self.display.blit(image, (tile['x'] - tile_size // 3.7, tile['y'] - tile_size // 3.7))  #la valeur ici est arbitraire mais marche. elle est la pour centrer l'affichage du joueur sur une tuile, a changer dans le futur

    def player_size(self):
        """Renvoie la taille que fera le joueur (sa hauteur et sa largeur sont similaires)"""
        width = (WINDOW_WIDTH - NB_COL * GAP) // NB_COL
        height = (WINDOW_HEIGHT - NB_ROW * GAP) // NB_ROW

        #Réutilisation du calcul de la taille des tuilles pour calculer la taille du joueur
        if height < 0.86 * width:
            width = height // 0.86
        else:
            height = round(width * 0.86)
        return int(width) // 1.8

    def tile_size(self):
        """Renvoie la taille d'une tuille                       CECI EST UNE FONCTION TEST QUI POURRAS SUREMENT ETRE ENLEVEE"""
        width = (WINDOW_WIDTH - NB_COL * GAP) // NB_COL
        height = (WINDOW_HEIGHT - NB_ROW * GAP) // NB_ROW

        #Réutilisation du calcul de la taille des tuilles pour calculer la taille du joueur
        if height < 0.86 * width:
            width = height // 0.86
        else:
            height = round(width * 0.86)
        return int(width)

    
    