import pygame

from constants import Color
from objects.base import DrawableObject


class Seed(DrawableObject):
    RADIUS = 4
    DIAMETER = RADIUS * 2

    def __init__(self, game, x, y):
        super().__init__(game)
        self.x = x
        self.y = y
        self.rect = pygame.rect.Rect(x - self.RADIUS, y - self.RADIUS, self.DIAMETER, self.DIAMETER)
        self.stay = True

    def process_draw(self) -> None:
        if self.stay == True:
            pygame.draw.circle(self.game.screen, Color.YELLOW, (self.x, self.y), self.RADIUS)
