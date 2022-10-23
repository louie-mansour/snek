from valueobject.direction import Direction
from valueobject.position import Position


class Snek:
    def __init__(self, positions, grid):
        self.grid = grid
        self.positions = positions
        self.direction = None

    def move(self, direction):
        new_head = self._get_new_head_position(direction)
        self.positions.insert(0, new_head)
        self.positions.pop()

    def _get_new_head_position(self, new_direction):
        if new_direction is None:
            new_direction = self.direction

        if new_direction == Direction.UP:
            return Position((self.positions[0].row - 1) % self.grid.number_of_rows, self.positions[0].col)
        elif new_direction == Direction.RIGHT:
            return Position(self.positions[0].row, (self.positions[0].col + 1) % self.grid.number_of_cols)
        elif new_direction == Direction.DOWN:
            return Position((self.positions[0].row + 1) % self.grid.number_of_rows, self.positions[0].col)
        elif new_direction == Direction.LEFT:
            return Position(self.positions[0].row, (self.positions[0].col - 1) % self.grid.number_of_cols)
        else:
            return self.positions[0]
