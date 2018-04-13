from constants import GRID_SET, WIDTH, HEIGHT, COMPLEXITY_LEVEL, BLACK, CELLSIZE, WHITE, SIDE_DICT
from random import random
from pygame.surface import Surface
from pygame import HWSURFACE, draw


def randomize():
    return random() < COMPLEXITY_LEVEL


class Grid(object):
    def __init__(self):

        self.grid = {}
        self.surf = None

        for i in GRID_SET:
            if randomize():
                self.grid[i] = True

    def get_cell(self, pos):
        cell = self.grid.get(pos)
        return cell if cell else False

    def get_available_cells(self, pos):
        available = []
        for i in ['top', 'left', 'right', 'bottom']:
            if not self.get_cell((pos[0]+SIDE_DICT[i][0], pos[1]+SIDE_DICT[i][1])):
                available.append(i)

        return available

    def build_draw(self, disp):
        self.surf = Surface((WIDTH, HEIGHT), HWSURFACE)
        self.surf.fill(WHITE)
        for i in self.grid:
            draw.circle(self.surf,
                        BLACK,
                        (
                            (i[0]*CELLSIZE)+(CELLSIZE/2),
                            (i[1]*CELLSIZE)+(CELLSIZE/2)
                        ),
                        CELLSIZE/2)
        self.surf.convert(disp)

    def draw(self, disp):
        if not self.surf:
            self.build_draw(disp)
        disp.blit(self.surf, self.surf.get_rect())
