from valueobject.direction import Direction
from valueobject.position import Position


class Snek:
    def __init__(self, positions, grid):
        self.grid = grid
        self.positions = positions
        self.direction = None

    def __str__(self):
        out = ''
        for position in self.positions:
            out += str(position)
        return out

    def move(self, direction):
        new_head = self._get_new_head_position(direction)
        self.positions.insert(0, new_head)
        self.positions.pop()

    def _get_new_head_position(self, new_direction):
        if new_direction is None:
            new_direction = self.direction

        if self.direction == Direction.UP:
            if new_direction == Direction.LEFT:
                return self._move_left()
            if new_direction == Direction.RIGHT:
                return self._move_right()
            else:
                return self._move_up()

        if self.direction == Direction.RIGHT:
            if new_direction == Direction.UP:
                return self._move_up()
            if new_direction == Direction.DOWN:
                return self._move_down()
            else:
                return self._move_right()

        if self.direction == Direction.DOWN:
            if new_direction == Direction.RIGHT:
                return self._move_right()
            if new_direction == Direction.LEFT:
                return self._move_left()
            else:
                return self._move_down()

        if self.direction == Direction.LEFT:
            if new_direction == Direction.DOWN:
                return self._move_down()
            if new_direction == Direction.UP:
                return self._move_up()
            else:
                return self._move_left()

        if new_direction == Direction.UP:
            return self._move_up()
        elif new_direction == Direction.RIGHT:
            return self._move_right()
        elif new_direction == Direction.DOWN:
            return self._move_down()
        elif new_direction == Direction.LEFT:
            return self._move_left()
        else:
            return self._stay_still()

    def _move_up(self):
        self.direction = Direction.UP
        return Position((self.positions[0].row - 1) % self.grid.number_of_rows, self.positions[0].col)

    def _move_right(self):
        self.direction = Direction.RIGHT
        return Position(self.positions[0].row, (self.positions[0].col + 1) % self.grid.number_of_cols)

    def _move_down(self):
        self.direction = Direction.DOWN
        return Position((self.positions[0].row + 1) % self.grid.number_of_rows, self.positions[0].col)

    def _move_left(self):
        self.direction = Direction.LEFT
        return Position(self.positions[0].row, (self.positions[0].col - 1) % self.grid.number_of_cols)

    def _stay_still(self):
        self.direction = None
        return self.positions[0]
