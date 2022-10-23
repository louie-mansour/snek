class NextFrameUseCase:

    def __init__(self, grid_repo, snek_command_repo):
        self.grid_repo = grid_repo
        self.snek_command_repo = snek_command_repo

    def next_frame(self):
        grid = self.grid_repo.get_grid()
        direction = self.snek_command_repo.get_direction()

        grid.snek.move(direction)

        return self.grid_repo.update_with_snek(grid.snek)
