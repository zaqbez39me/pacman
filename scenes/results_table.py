from constants import Color
from objects import ButtonObject
from objects import TextObject
from scenes import BaseScene


class ResultsScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)

    def create_objects(self):
        sorted_list = []
        self.objects = []
        f = open("high_scores/high_scores.txt", "r")
        for line in f.readlines():
            sorted_list.append(int(line))
        sorted_list.sort(reverse=True)
        for i in range(min(5, len(sorted_list))):
            self.objects.append(TextObject(self.game, text=str(sorted_list[i]), x=400, y=120 + 50 * i))
        f.close()
        self.button_start = ButtonObject(
            self.game,
            self.game.WIDTH // 2 - 100, self.game.HEIGHT // 2 + 95, 200, 50,
            Color.RED, self.return_to_menu, "Вернуться в меню"
        )
        self.objects.append(self.button_start)
        self.objects.append(TextObject(self.game, text=str("Лучшие результаты:"), x=400, y=70))

    def return_to_menu(self) -> None:
        self.game.set_scene(self.game.MENU_SCENE_INDEX)

    def on_activate(self) -> None:
        self.create_objects()
