import random

from entity.snek import Snek
from valueobject.position import Position


class Grid:
    def __init__(self, number_of_rows, number_of_cols):
        self.number_of_rows = number_of_rows
        self.number_of_cols = number_of_cols

        self.matrix = []
        for _ in range(0, self.number_of_rows):
            self.matrix.append(self.number_of_cols * [0])

        self.snek =\
            Snek([Position(random.randint(0, self.number_of_rows), random.randint(0, self.number_of_cols))], self)
