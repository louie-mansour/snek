import random


class UseCases:

    def __init__(self, grid_repo, snek_command_repo):
        self.grid_repo = grid_repo
        self.snek_command_repo = snek_command_repo

    def add_snek(self):
        grid = self.grid_repo.get_grid()
        random_snek_position = random.choice(list(grid.empty_positions))
        grid.add_snek(random_snek_position)

    def next_frame(self):
        direction = self.snek_command_repo.get_direction()
        grid = self.grid_repo.get_grid()
        snek = grid.snek
        snek.move(direction)
        grid.update_with_snek_positions(snek)

        return self.grid_repo.set_grid(grid)

    def set_direction(self, direction):
        return self.snek_command_repo.set_direction(direction)
