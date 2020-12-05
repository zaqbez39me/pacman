from objects.seed import Seed
import pygame as pygame


class Energizer(Seed):
    RADIUS = 13
    DIAMETER = RADIUS * 2

    def __init__(self, game, x, y):
        super().__init__(game, x, y)

    def process_draw(self) -> None:
        if self.stay == True:
            change = pygame.time.get_ticks()
            if change // 1000 % 2 != 0:
                pygame.draw.circle(self.game.screen, pygame.color.Color('yellow'), (self.x, self.y), self.RADIUS)
            else:
                pygame.draw.circle(self.game.screen, pygame.color.Color('green'), (self.x, self.y), self.RADIUS)
