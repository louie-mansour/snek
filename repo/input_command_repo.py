from valueobject.direction import Direction


class SnekCommandRepo:
    def __init__(self):
        self.direction = None

    def set_direction(self, direction):
        self.direction = direction
        return direction

    def get_direction(self):
        return self.direction
