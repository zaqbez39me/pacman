import pygame as pg
from objects.ghost import Ghost
from objects.wall import Wall


class Player(Ghost):
    def __init__(self, game, drawing):
        Ghost.__init__(self, game, drawing)
        self.img = pg.image.load(drawing)
        self.width = 50
        self.height = 50
        self.img = pg.transform.scale(self.img, (self.width, self.height))
        self.rect = self.img.get_rect()
        self.speed_x = 0
        self.speed_y = 0
        self.rect.y = 530
        self.rect.x = 375
        self.pl_speed = 5
        self.current_shift_y = 0
        self.current_shift_x = 0
        self.prev_posx = self.rect.x
        self.prev_posy = self.rect.y

    def move_right(self):
        if self.rect.x < 780 - self.width:
            self.current_shift_x = self.pl_speed
            self.current_shift_y = 0
        else:
            self.current_shift_x = 0
        self.img = pg.image.load('images/pacman_0.png')
        self.img = pg.transform.scale(self.img, (self.width, self.height))

    def move_left(self):
        if self.rect.x > 20:
            self.current_shift_x = -self.pl_speed
            self.current_shift_y = 0
        else:
            self.current_shift_x = 0
        self.img = pg.image.load('images/pacman_180.png')
        self.img = pg.transform.scale(self.img, (self.width, self.height))

    def move_up(self):
        if self.rect.y > 20:
            self.current_shift_y = -self.pl_speed
            self.current_shift_x = 0
        else:
            self.current_shift_y = 0
        self.img = pg.image.load('images/pacman_90.png')
        self.img = pg.transform.scale(self.img, (self.width, self.height))

    def move_down(self):
        if self.rect.y < 580 - self.height:
            self.current_shift_y = self.pl_speed
            self.current_shift_x = 0
        else:
            self.current_shift_y = 0
        self.img = pg.image.load('images/pacman_270.png')
        self.img = pg.transform.scale(self.img, (self.width, self.height))

    def move_stop(self):
        self.current_shift_x = 0
        self.current_shift_y = 0

    def check_collide(self, rect):
        return self.rect.colliderect(rect)

    def collides_with(self, obj):
        if isinstance(obj, list) and isinstance(obj[0], Wall):
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            for i in range(len(obj)):
                if self.check_collide(obj[i]):
                    self.rect.x = self.prev_posx
                    self.rect.y = self.prev_posy
                    self.move_stop()
                    break

    def process_draw(self):
        self.prev_posx = self.rect.x
        self.prev_posy = self.rect.y
        self.rect.x = self.rect.x + self.current_shift_x
        self.rect.y = self.rect.y + self.current_shift_y
        self.game.screen.blit(self.img, self.rect)
