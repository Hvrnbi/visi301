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
        self.actions_till_next_farmer = 10
        self.last_tile = self.find_current_tile()
        self.pos_history = [(self.x, self.y)]
        self.piou_piou_number = 0

    def draw(self):
        """Affiche le joueur"""
        image = pygame.transform.scale(self.picture, (self.world.tile_width, self.world.tile_height))
        self.display.blit(image, (self.x - self.world.tile_width // 2, self.y - self.world.tile_height // 2))  #la valeur ici est arbitraire mais marche. elle est la pour centrer l'affichage du joueur sur une tuile, a changer dans le futur
        # On dessine tous les poussins
        for i in range(2, self.piou_piou_number + 2):
            pioumage = pygame.transform.scale(PIOU_PIOU, (self.world.tile_width, self.world.tile_height))
            self.display.blit(pioumage, (self.pos_history[-i][0] - self.world.tile_width // 2, self.pos_history[-i][1] - self.world.tile_height // 2))
        
    
    def move(self, direction: str):
        """Modifie les coordonnées x et y du joueur en fonction de la direction donnée"""
        really_move = True

        if direction == "up":
            if self.y - self.world.gap - self.world.tile_height >= self.world.top_border:   # Il faut que ça soit supérieur parce que les coos descendent 
                self.y -= self.world.gap + self.world.tile_height
                self.next_move = "up"
                if self.picture == PLAYER_LD:
                    self.picture = PLAYER_LU
                elif self.picture == PLAYER_RD:
                    self.picture = PLAYER_RU
                # Si un poussin est déjà là
                if self.piou_piou_number > 1:
                    if (self.x, self.y) in self.pos_history[-self.piou_piou_number:]:
                        really_move = False
                        self.move("up")
            else:
                really_move = False

        elif direction == "down":
            if self.y + self.world.gap + self.world.tile_height <= self.world.bottom_border:    # Inversement ici
                self.y += self.world.gap + self.world.tile_height
                self.next_move = "down"
                if self.picture == PLAYER_LU:
                    self.picture = PLAYER_LD
                elif self.picture == PLAYER_RU:
                    self.picture = PLAYER_RD
                # Si un poussin est déjà là
                if self.piou_piou_number > 1:
                    if (self.x, self.y) in self.pos_history[-self.piou_piou_number:]:
                        really_move = False
                        self.move("down")
            else:
                really_move = False

        elif direction == "left":
            if self.x - self.world.gap - 3 * self.world.tile_width // 4 >= self.world.left_border:
                if self.next_move == "up":
                    if self.y - self.world.gap // 2 - self.world.tile_height // 2 >= self.world.top_border:
                        self.x -= self.world.gap + 3 * self.world.tile_width // 4
                        self.y -= self.world.gap // 2 + self.world.tile_height // 2
                        self.next_move = "down"
                        self.picture = PLAYER_LD
                        # Si un poussin est déjà là
                        if self.piou_piou_number > 1:
                            if (self.x, self.y) in self.pos_history[-self.piou_piou_number:]:
                                really_move = False
                                self.move("left")
                    else:
                        self.next_move = "down"
                        self.move("left")
                        really_move = False

                elif self.next_move == "down":
                    if self.y + self.world.gap // 2 + self.world.tile_height // 2 <= self.world.bottom_border:
                        self.x -= self.world.gap + 3 * self.world.tile_width // 4
                        self.y += self.world.gap // 2 + self.world.tile_height // 2
                        self.next_move = "up"
                        self.picture = PLAYER_LU
                        # Si un poussin est déjà là
                        if self.piou_piou_number > 1:
                            if (self.x, self.y) in self.pos_history[-self.piou_piou_number:]:
                                really_move = False
                                self.move("left")
                    else:
                        self.next_move = "up"
                        self.move("left")
                        really_move = False
            else:
                really_move = False

        elif direction == "right":
            if self.x + self.world.gap + 3 * self.world.tile_width // 4 <= self.world.right_border:
                if self.next_move == "up":
                    if self.y - self.world.gap // 2 - self.world.tile_height // 2 >= self.world.top_border:
                        self.x += self.world.gap + 3 * self.world.tile_width // 4
                        self.y -= self.world.gap // 2 + self.world.tile_height // 2
                        self.next_move = "down"
                        self.picture = PLAYER_RD
                        # Si un poussin est déjà là
                        if self.piou_piou_number > 1:
                            if (self.x, self.y) in self.pos_history[-self.piou_piou_number:]:
                                really_move = False
                                self.move("right")
                    else:
                        self.next_move = "down"
                        self.move("right")
                        really_move = False

                elif self.next_move == "down":
                    if self.y + self.world.gap // 2 + self.world.tile_height // 2 <= self.world.bottom_border:
                        self.x += self.world.gap + 3 * self.world.tile_width // 4
                        self.y += self.world.gap // 2 + self.world.tile_height // 2
                        self.next_move = "up"
                        self.picture = PLAYER_RU
                        # Si au moins deux poussins sont là
                        if self.piou_piou_number > 1:
                            if (self.x, self.y) in self.pos_history[-self.piou_piou_number:]:
                                really_move = False
                                self.move("right")
                    else:
                        self.next_move = "up"
                        self.move("right")
                        really_move = False
            else:
                really_move = False
        
        if really_move:
            self.handle_egg()
            self.pos_history.append((self.x, self.y))


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
        if self.world.egg == 0:
            self.world.egg = 1
            self.world.tiles_list[0].tiletype = "egg1"


    def handle_egg(self):
        """Gère l'oeuf"""
        if self.world.egg == 2:
            self.world.tiles_list[0].type = "egg2"
            self.world.tiles_list[0].tiletype = "egg2"

        elif self.world.egg == 4:
            self.world.tiles_list[0].type = "egg3"
            self.world.tiles_list[0].tiletype = "egg3"

        elif self.world.egg == 6:
            self.world.tiles_list[0].type = "egg4"
            self.world.tiles_list[0].tiletype = "egg4"

        elif self.world.egg == 8:
            self.world.tiles_list[0].type = "egg5"
            self.world.tiles_list[0].tiletype = "egg5"
        
        if self.world.egg == 10:
            self.world.egg = 0
            self.world.tiles_list[0].tiletype = "nest"
            self.piou_piou_number += 1
        elif self.world.egg != 0:
            self.world.egg += 1

