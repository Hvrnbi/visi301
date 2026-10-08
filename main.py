import pygame, sys
from pygame.locals import * # Import des constantes de pygame
from world import World
from variables import *
from player import *
from nest import *
from farmer import *


def main():
    """La fonction pricipale"""

    ### Initialmisation ###
    pygame.init()   # La fonction secrète, on sait pas ce qu'elle fait mais elle doit être là

    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Taille de la fenêtre

    pygame.display.set_caption("VISI301")   # Nom de la fenêtre, à changer à la fin TODO

    # Horloge du jeu
    clock = pygame.time.Clock()

    # Création du monde
    world = World(display, NB_COL, NB_ROW, GAP)

    player = Player(world.pos_list[1]["x"], world.pos_list[1]["y"], world, display) # On initialise le joueur sur la première tuile en dessous du nid

    nest = Nest(0, display)

    random_border_tile_example = world.random_border_tile(world.border_tiles(world.tiles_list))
    farmer = Farmer(random_border_tile_example.x, random_border_tile_example.y, world, display)

    farmer.draw()

    ### Boucle principale ###
    while True:

        # On gère les évènements
        for event in pygame.event.get():

            # On gère les touches
            if event.type == pygame.KEYDOWN:

                farmer.x, farmer.y = farmer.next_tuile(world)
                farmer.neighbors_list = farmer.neighbors(farmer.x, farmer.y, farmer.world)
                print("FARMER FARMER FARMER FARMER FARMER FARMER FARMER FARMER FARMER FARMER FARMER ")
                print(farmer.x, farmer.y)
                print("LISTE   LISTE   LISTE   LISTE   LISTE   LISTE   LISTE   LISTE   LISTE   LISTE   LISTE   ")
                farmer.way_to_follow(world)

                if event.key == pygame.K_z:
                    player.move("up")

                elif event.key == pygame.K_s:
                    player.move("down")
            
            # Fermeture du jeu
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # À chaque tick on fait ce qu'il y a là
        display.fill(BACKGROUND_COLOR)
        world.draw()
        player.draw()
        nest.draw(world.pos_list[0], 0)
        farmer.draw()

            
        pygame.display.update()
        clock.tick(FPS)


    # On quitte pygame
    pygame.quit()


# On lance la fonction principale
main()
