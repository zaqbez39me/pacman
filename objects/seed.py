import pygame
from objects.base import DrawableObject
from constants import Color


class Seed(DrawableObject):
    RADIUS = 4
    DIAMETER = RADIUS * 2

    def __init__(self, game, x, y):
        super().__init__(game)
        self.x = x
        self.y = y
        self.rect = pygame.rect.Rect(x - Seed.RADIUS, y - Seed.RADIUS, Seed.DIAMETER, Seed.DIAMETER)

    def process_draw(self) -> None:
        pygame.draw.circle(self.game.screen, Color.YELLOW, (self.x, self.y), Seed.RADIUS)
