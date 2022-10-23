import time

from valueobject.direction import Direction


class RestController:
    def __init__(self, snek_direction_use_case, next_frame_use_case, grid_view):
        self.snek_direction_use_case = snek_direction_use_case
        self.next_frame_use_case = next_frame_use_case
        self.grid_view = grid_view

    def join_game(self):
        while True:
            grid = self.next_frame_use_case.next_frame()
            self.grid_view.display(grid)
            time.sleep(0.1)

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

        direction = self.snek_direction_use_case.use_case(direction)

        return "{ 'direction': '" + str(direction) + "' }"
