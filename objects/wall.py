import pygame as pg


class Wall:
    def __init__(self, x, y, width, height, size, screen):
        self.size = size
        self.screen = screen
        self.img = pg.image.load('klipartz.com.png')
        if height >= 40:
            self.img = pg.transform.rotate(self.img, 90)
            self.img = pg.transform.scale(self.img, (width, height))
        else:
            self.img = pg.transform.scale(self.img, (width, height))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen
        self.current_shift = 0
        self.width = width
        self.height = height

    def draw(self):
        self.screen.blit(self.img, self.rect)

    def collides_with(self, b):
        return self.rect.colliderect(b.rect)
