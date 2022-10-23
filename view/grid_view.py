from valueobject.position import Position


class GridView:
    def display(self, grid):
        # print(grid)
        print('\n\n\n\n\n\n\n\n\n\n')

        matrix = []
        for r in range(0, grid.number_of_rows):
            matrix.append([])
            for c in range(0, grid.number_of_cols):
                matrix[r].append(1)

        for empty_position in grid.empty_positions:
            matrix[empty_position.row][empty_position.col] = 0

        for matrix_row in matrix:
            print(matrix_row)
