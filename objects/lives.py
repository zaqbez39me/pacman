import pygame as pg


class Lives:
    MAX_LIVES = 2

    def __init__(self, size, screen):
        self.screen = screen
        self.lives = 2
        self.img = pg.image.load('pacman_0.png')
        self.width = 30
        self.height = 30
        self.img = pg.transform.scale(self.img, (self.width, self.height))
        self.rect = self.img.get_rect()

    def draw(self):
        x = 0
        y = 600
        for i in range(self.lives):
            self.rect.x = x
            self.rect.y = y
            self.screen.blit(self.img, self.rect)
            x += self.width
