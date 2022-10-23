from entity.grid import Grid


class GridRepo:

    def __init__(self):
        self.grid = Grid(10, 20)

    def get_grid(self):
        return self.grid

    def update_with_snek(self, snek):
        for i, row in enumerate(self.grid.matrix):
            for j, _ in enumerate(row):
                self.grid.matrix[i][j] = 0
        for position in snek.positions:
            self.grid.matrix[position.row][position.col] = 1
        return self.grid
