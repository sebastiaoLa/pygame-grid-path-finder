from constants import WIDTH, HEIGHT, WHITE, CELLSIZE
import pygame
from grid import Grid
from player import Player
from pygame import QUIT, Rect


pygame.init()


class Game(object):
    def __init__(self):
        self.grid = Grid()
        self.display_surf = pygame.display.set_mode(
            (WIDTH, HEIGHT),
            pygame.HWSURFACE | pygame.SRCALPHA  # |pygame.DOUBLEBUF
        )
        self.players = [Player((0, 0),
                               (int(WIDTH/CELLSIZE)-1, int(HEIGHT/CELLSIZE)-1))]

    def update(self):
        children = []
        for i in self.players:
            children += i.move(
                self.grid.get_available_cells(
                    i.pos
                )
            )
        self.players = children
        self.players.sort()
        while len(self.players) > 50:
            self.players.pop()

    def draw(self):
        self.display_surf.fill(WHITE, Rect(0, 0, WIDTH, HEIGHT))
        self.grid.draw(self.display_surf)

    def main_loop(self):
        while True:
            self.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
            self.draw()
            pygame.display.flip()
