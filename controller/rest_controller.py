import time

from valueobject.direction import Direction


class RestController:
    def __init__(self, use_cases, grid_view):
        self.use_cases = use_cases
        self.grid_view = grid_view

    def join_game(self):
        self.use_cases.add_snek()
        while True:
            grid = self.use_cases.next_frame()
            self.grid_view.display(grid)
            time.sleep(0.3)

    def set_direction(self, request):
        direction_input = request.get_json(force=True)['direction']

        if direction_input == 'up':
            direction = Direction.UP
        elif direction_input == 'right':
            direction = Direction.RIGHT
        elif direction_input == 'down':
            direction = Direction.DOWN
        elif direction_input == 'left':
            direction = Direction.LEFT
        else:
            raise 'Invalid input'

        direction = self.use_cases.set_direction(direction)

        return "{ 'direction': '" + str(direction) + "' }"
