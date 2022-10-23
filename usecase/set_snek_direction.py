class SetSnekDirectionUseCase:

    def __init__(self, snek_command_repo):
        self.snek_command_repo = snek_command_repo

    def use_case(self, direction):
        print('Set snek direction ' + str(direction))

        return self.snek_command_repo.set_direction(direction)
