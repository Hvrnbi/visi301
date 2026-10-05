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
        self.picture =  PLAYER_RU
        self.world: World = world
        self.next_move = "up"

    def draw(self):
        """Affiche le joueur"""
        image = pygame.transform.scale(self.picture, (self.world.tile_width, self.world.tile_height))
        self.display.blit(image, (self.x - self.world.tile_width // 2, self.y - self.world.tile_height // 2))  #la valeur ici est arbitraire mais marche. elle est la pour centrer l'affichage du joueur sur une tuile, a changer dans le futur
    
    
    def move(self, direction: str):
        """Modifie les coordonnées x et y du joueur en fonction de la direction donnée"""
        if direction == "up":
            if self.y - self.world.gap - self.world.tile_height >= self.world.top_border:   # Il faut que ça soit supérieur parce que les coos descendent 
                self.y -= self.world.gap + self.world.tile_height
                self.next_move = "up"
                if self.picture == PLAYER_LD:
                    self.picture = PLAYER_LU
                elif self.picture == PLAYER_RD:
                    self.picture = PLAYER_RU

        elif direction == "down":
            if self.y + self.world.gap + self.world.tile_height <= self.world.bottom_border:    # Inversement ici
                self.y += self.world.gap + self.world.tile_height
                self.next_move = "down"
                if self.picture == PLAYER_LU:
                    self.picture = PLAYER_LD
                elif self.picture == PLAYER_RU:
                    self.picture = PLAYER_RD

        elif direction == "left":
            if self.x - self.world.gap - 3 * self.world.tile_width // 4 >= self.world.left_border:
                if self.next_move == "up":
                    if self.y - self.world.gap // 2 - self.world.tile_height // 2 >= self.world.top_border:
                        self.x -= self.world.gap + 3 * self.world.tile_width // 4
                        self.y -= self.world.gap // 2 + self.world.tile_height // 2
                        self.next_move = "down"
                        self.picture = PLAYER_LD

                elif self.next_move == "down":
                    if self.y + self.world.gap // 2 + self.world.tile_height // 2 <= self.world.bottom_border:
                        self.x -= self.world.gap + 3 * self.world.tile_width // 4
                        self.y += self.world.gap // 2 + self.world.tile_height // 2
                        self.next_move = "up"
                        self.picture = PLAYER_LU

        elif direction == "right":
            if self.x + self.world.gap + 3 * self.world.tile_width // 4 <= self.world.right_border:
                if self.next_move == "up":
                    if self.y - self.world.gap // 2 - self.world.tile_height // 2 >= self.world.top_border:
                        self.x += self.world.gap + 3 * self.world.tile_width // 4
                        self.y -= self.world.gap // 2 + self.world.tile_height // 2
                        self.next_move = "down"
                        self.picture = PLAYER_RD

                elif self.next_move == "down":
                    if self.y + self.world.gap // 2 + self.world.tile_height // 2 <= self.world.bottom_border:
                        self.x += self.world.gap + 3 * self.world.tile_width // 4
                        self.y += self.world.gap // 2 + self.world.tile_height // 2
                        self.next_move = "up"
                        self.picture = PLAYER_RU

