from objects.seed import Seed


class Energizer(Seed):
    RADIUS = 13
    DIAMETER = RADIUS * 2

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
