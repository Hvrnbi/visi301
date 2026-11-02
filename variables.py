from pygame import image
from os import path

# taille de la fenêtre
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

# Nombre d'images par secondes
FPS = 60

# Nombre de colonnes et de lignes sur la map
NB_COL = 17
NB_ROW = 12

# Espacement entre les tuiles (en px)
GAP = 8

# images
HEXA = image.load(path.join("images/hexa.png"))
SEED = image.load(path.join("images/seed.png"))
PATH_TILES = [
    image.load(path.join("images/path1.png")),
    image.load(path.join("images/path2.png")),
    image.load(path.join("images/path3.png")),
    image.load(path.join("images/path4.png")),
    image.load(path.join("images/path5.png")),
]
NEST = image.load(path.join("images/nest.png"))
EGG1 = image.load(path.join("images/egg1.png"))
EGG2 = image.load(path.join("images/egg2.png"))
EGG3 = image.load(path.join("images/egg3.png"))
EGG4 = image.load(path.join("images/egg4.png"))
EGG5 = image.load(path.join("images/egg5.png"))


PLAYER_RU = image.load(path.join("images/player-ru.png"))
PLAYER_RD = image.load(path.join("images/player-rd.png"))
PLAYER_LU = image.load(path.join("images/player-lu.png"))
PLAYER_LD = image.load(path.join("images/player-ld.png"))

PIOU_PIOU = image.load(path.join("images/piou-piou.png"))

FARMER = image.load(path.join("images/farmer.png"))

# tuile de base pour le personnage
ORIGIN = 0

# couleurs
BACKGROUND_COLOR = (24, 40, 69)
FARMER_COLOR = [(255, 80, 80), (80, 200, 255), (255, 210, 60), (200, 120, 255), (255, 150, 50), (255, 130, 200)]

# écart toléré pour trouvé une tuile (en px)
SPACE = 30