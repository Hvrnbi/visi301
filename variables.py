from pygame import image
from os import path

# taille de la fenêtre
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

# Nombre de colonnes et de lignes sur la map
NB_COL = 17
NB_ROW = 12

# Espacement entre les tuiles (en px)
GAP = 8


# images
HEXA = image.load(path.join("images/hexa.png"))

# couleurs
BACKGROUND_COLOR = (24, 40, 69)