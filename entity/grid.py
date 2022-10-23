from entity.snek import Snek
from valueobject.position import Position


class Grid:
    def __init__(self, number_of_rows, number_of_cols):
        self.number_of_rows = number_of_rows
        self.number_of_cols = number_of_cols
        self.empty_positions = set()
        for r in range(number_of_rows):
            for c in range(number_of_cols):
                self.empty_positions.update({Position(r, c)})
        self._empty_grid = self.empty_positions.copy()
        self.snek = None
        self.food = None

    def __str__(self):
        out = ''
        for position in self.empty_positions:
            out += str(position)
        return out

    def add_snek(self, position):
        self.snek = Snek([position], self)
        self.empty_positions.remove(position)

    def update_with_snek_positions(self, snek):
        new_empty_positions = self._empty_grid.copy()

        for position in snek.positions:
            if position in new_empty_positions:
                new_empty_positions.remove(position)
        self.empty_positions = new_empty_positions
