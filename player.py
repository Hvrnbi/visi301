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
        self.moving = True
        self.egg = 0
        self.actions_till_next_farmer = 10
        self.last_tile = self.find_current_tile()

    def draw(self):
        """Affiche le joueur"""
        image = pygame.transform.scale(self.picture, (self.world.tile_width, self.world.tile_height))
        self.display.blit(image, (self.x - self.world.tile_width // 2, self.y - self.world.tile_height // 2))  #la valeur ici est arbitraire mais marche. elle est la pour centrer l'affichage du joueur sur une tuile, a changer dans le futur
        # On dessine l'oeuf si besoin
        
    
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
                    else:
                        self.next_move = "down"
                        self.move("left")

                elif self.next_move == "down":
                    if self.y + self.world.gap // 2 + self.world.tile_height // 2 <= self.world.bottom_border:
                        self.x -= self.world.gap + 3 * self.world.tile_width // 4
                        self.y += self.world.gap // 2 + self.world.tile_height // 2
                        self.next_move = "up"
                        self.picture = PLAYER_LU
                    else:
                        self.next_move = "up"
                        self.move("left")

        elif direction == "right":
            if self.x + self.world.gap + 3 * self.world.tile_width // 4 <= self.world.right_border:
                if self.next_move == "up":
                    if self.y - self.world.gap // 2 - self.world.tile_height // 2 >= self.world.top_border:
                        self.x += self.world.gap + 3 * self.world.tile_width // 4
                        self.y -= self.world.gap // 2 + self.world.tile_height // 2
                        self.next_move = "down"
                        self.picture = PLAYER_RD
                    else:
                        self.next_move = "down"
                        self.move("right")

                elif self.next_move == "down":
                    if self.y + self.world.gap // 2 + self.world.tile_height // 2 <= self.world.bottom_border:
                        self.x += self.world.gap + 3 * self.world.tile_width // 4
                        self.y += self.world.gap // 2 + self.world.tile_height // 2
                        self.next_move = "up"
                        self.picture = PLAYER_RU
                    else:
                        self.next_move = "up"
                        self.move("right")


    def find_current_tile(self):
        """Renvoie la tuile sur laquelle se trouve le joueur"""
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

    
    def action(self):
        """L'action de ce tour"""
        tile = self.find_current_tile()
        if (tile.x, tile.y) != (self.last_tile.x, self.last_tile.y):
            if tile.tiletype == "seed":
                self.moving = False
                self.seed()
                tile.tiletype = "green"
                self.world.spawn_new_seed()

            self.actions_till_next_farmer -= 1
            self.last_tile = tile
            self.moving = True

    
    def seed(self):
        if self.egg == 0:
            self.egg = 1
        else:
            print("Il y a déjà un oeuf")

