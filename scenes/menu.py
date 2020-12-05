import pygame as pg

from constants import Color
from objects import ButtonObject
from scenes import BaseScene


class MenuScene(BaseScene):
    def draw_logo(self):
        self.img = pg.image.load('images/pacman_0.png')
        self.img = pg.transform.scale(self.img, (100, 100))
        self.rect = self.img.get_rect()
        self.rect.x = 350
        self.rect.y = 100
        self.game.screen.blit(self.img, self.rect)

    def create_objects(self) -> None:
        self.button_start = ButtonObject(
            self.game,
            self.game.WIDTH // 2 - 100, self.game.HEIGHT // 2 - 20 - 25, 200, 50,
            Color.RED, self.start_game, "Запуск игры"
        )
        self.button_exit = ButtonObject(
            self.game,
            self.game.WIDTH // 2 - 100, self.game.HEIGHT // 2 + 25, 200, 50,
            Color.RED, self.game.exit_game, 'Выход'
        )
        self.button_results = ButtonObject(
            self.game,
            self.game.WIDTH // 2 - 100, self.game.HEIGHT // 2 + 95, 200, 50,
            Color.RED, self.show_results, 'Таблица результатов'
        )
        self.draw_logo()
        self.objects = [self.button_start, self.button_exit, self.button_results]

    def start_game(self) -> None:
        self.game.set_scene(self.game.MAIN_SCENE_INDEX)

    def show_results(self):
        self.game.set_scene(self.game.RESULT_SCENE_INDEX)

    def on_window_resize(self) -> None:
        self.button_start.move(self.game.WIDTH // 2 - 100, self.game.HEIGHT // 2 - 20 - 25)
        self.button_exit.move(self.game.WIDTH // 2 - 100, self.game.HEIGHT // 2 + 25)

    def additional_draw(self) -> None:
        self.draw_logo()
