
from math import log10
FULLSCREEN = True
START_PAUSED = False

if FULLSCREEN:
    import pygame
    # SCREEN SIZE
    pygame.display.init()
    SCREEN = pygame.display.Info()
    WIDTH = int(SCREEN.current_w*0.9)
    HEIGHT = int(SCREEN.current_h*0.9)
else:
    WIDTH = 800
    HEIGHT = 600

# consts :
#	COLORS
RED = (255, 000, 000)
GREEN = (000, 255, 000)
BLUE = (000, 000, 255)
WHITE = (255, 255, 255)
BLACK = (000, 000, 000)
BROWN = (139, 69, 19)
YELLOW = (255, 255, 0)
PINK = (248, 24, 148)

FPS = 60

WALLWIDTH = 1
CELLSIZE = 10

COMPLEXITY_LEVEL = 1/log10((WIDTH/CELLSIZE)*(HEIGHT/CELLSIZE))
COMPLEXITY_LEVEL = COMPLEXITY_LEVEL if COMPLEXITY_LEVEL > 0.25 and COMPLEXITY_LEVEL < 0.35 else (
    COMPLEXITY_LEVEL*1.1 if COMPLEXITY_LEVEL < 0.25 else 0.35)

print 'complexity', COMPLEXITY_LEVEL

# FROM = [
#     (0, y) for y in range(0, (HEIGHT/CELLSIZE)-1)
# ]+[
#     (x, 0) for x in (range(0, (HEIGHT/CELLSIZE)-1) if WIDTH > HEIGHT else range(0, (WIDTH/CELLSIZE)-1))
# ]
FROM = [(0, 0)]

DESTINY = [((WIDTH/CELLSIZE)-1, (HEIGHT/CELLSIZE)-1)]
# DESTINY = [(((WIDTH/CELLSIZE)-1)/2, ((HEIGHT/CELLSIZE)-1)/2)]
# DESTINY = [((WIDTH/CELLSIZE)-1, y+((HEIGHT/CELLSIZE)/2)-1)
#            for y in range(0, (HEIGHT/CELLSIZE)/2)]

DESTINY = set(DESTINY)
print DESTINY

GRID_SET = set()
for x in range(0, WIDTH/CELLSIZE):
    for y in range(0, HEIGHT/CELLSIZE):
        GRID_SET.add((x, y))

SIDE_DICT = {
    'top': [0, -1],
    'left': [-1, 0],
    'right': [1, 0],
    'bottom': [0, 1],
}
