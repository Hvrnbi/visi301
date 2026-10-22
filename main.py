import pygame, sys
from pygame.locals import * # Import des constantes de pygame
from world import World
from variables import *
from player import *
from farmer import *


# Fonctions

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
    

    ### Boucle principale ###
    while True:

        # On gère les évènements
        for event in pygame.event.get():

            # On gère les touches
            if event.type == pygame.KEYDOWN:

                # On gère la création et les actions des fermiers

                farmers_control(world, player, display)

                for farmer in world.farmers:
                    farmer.action()

                if event.key == pygame.K_z:
                    if player.moving:
                        player.move("up")

                elif event.key == pygame.K_s:
                    if player.moving:
                        player.move("down")

                elif event.key == pygame.K_q:
                    if player.moving:
                        player.move("left")

                elif event.key == pygame.K_d:
                    if player.moving:
                        player.move("right")
            
            # Fermeture du jeup
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # À chaque tick on fait ce qu'il y a là
        display.fill(BACKGROUND_COLOR)
        world.draw()
        player.draw()
        player.action()
        for farmer in world.farmers:
            farmer.draw()

        pygame.display.update()
        clock.tick(FPS)


    # On quitte pygame
    pygame.quit()


# On lance la fonction principale
main()
