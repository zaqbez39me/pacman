import pygame
from objects.base import DrawableObject
from constants import Color


class Seed(DrawableObject):
    def __init__(self, game, x, y):
        super().__init__(game)
        self.rect.x = x
        self.rect.y = y
        self.radius = 5

    def process_draw(self) -> None:
        pygame.draw.circle(self.game.screen, Color.YELLOW, (self.rect.x, self.rect.y), self.radius)
