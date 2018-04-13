from constants import SIDE_DICT
from math import sqrt


class Player(object):
    def __init__(self, pos, destiny, global_path=None, path=None,):
        self.pos = pos
        self.destiny = destiny
        self.global_path = global_path if global_path else set()
        self.global_path.add(self.pos)
        self.path = list(path) if path else []
        self.path.append(self.pos)

    def get_child(self, side):
        pos = tuple([self.pos[i]+SIDE_DICT[side][i] for i in range(0, 2)])
        if pos not in self.global_path:
            return Player(self.pos, self.destiny, global_path=self.global_path, path=self.path)

    def done(self):
        return self.pos == self.destiny

    def __cmp__(self, other):
        return self.distance_to_destiny()-other.distance_to_destiny()

    def distance_to_destiny(self):
        delta_x = self.destiny[0]-self.pos[0]
        delta_y = self.destiny[1]-self.pos[1]
        return int(round(sqrt((delta_x**2)*(delta_y**2))))

    def move(self, available):
        children = []
        for i in available:
            children.append(self.get_child(i))
        return children
