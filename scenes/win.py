from scenes import FinalScene


class WinScene(FinalScene):
    TEXT_FMT = 'Вы победили ({})'

    def __init__(self, game):
        super().__init__(game)
