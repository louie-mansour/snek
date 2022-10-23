class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __str__(self):
        return '(' + str(self.row) + ',' + str(self.col) + ')'

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __ne__(self, other):
        return self.row != other.row or self.col != other.col

    def __hash__(self):
        return self.row * 10 + self.col
