from entity.grid import Grid


class GridRepo:

    def __init__(self):
        self.grid = Grid(10, 10)

    def get_grid(self):
        return self.grid

    def set_grid(self, grid):
        self.grid = grid
        return self.grid
