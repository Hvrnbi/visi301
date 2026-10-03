import pygame, sys
from pygame.locals import * # Import des constantes de pygame
from world import *
from variables import *
from player import *
from nest import *


def main():
    """La fonction pricipale"""

    ### Initialmisation ###
    pygame.init()   # La fonction secrète, on sait pas ce qu'elle fait mais elle doit être là

    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Taille de la fenêtre
    display.fill(BACKGROUND_COLOR)

    pygame.display.set_caption("VISI301")   # Nom de la fenêtre, à changer à la fin TODO

    # Création du monde
    world = World(display, NB_COL, NB_ROW, GAP)
    world.draw()

    player = Player(0, 0, display)
    player.draw(world.pos_list[1])              #Le choix de la tuile a été arbitraire

    nest = Nest(0, display)
    nest.draw(world.pos_list[0], 0)

    ### Boucle principale ###
    while True:
        
        # À chaque tick on fait ce qu'il y a là
        # create_world(display, NB_COL, NB_ROW, GAP)

        for event in pygame.event.get():

            # On fait des trucs
            
            # Fermeture du jeu
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            pygame.display.update()

    # On quitte pygame
    pygame.quit()


# On lance la fonction principale
main()
