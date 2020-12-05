from objects.seed import Seed
import random
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
                ran = random.randint(0, 2)
                if ran == 0:
                    pygame.draw.circle(self.game.screen, pygame.color.Color('green'), (self.x, self.y), self.RADIUS)
                elif ran == 1:
                    pygame.draw.circle(self.game.screen, pygame.color.Color('red'), (self.x, self.y), self.RADIUS)
                elif ran == 2:
                    pygame.draw.circle(self.game.screen, pygame.color.Color('blue'), (self.x, self.y), self.RADIUS)
