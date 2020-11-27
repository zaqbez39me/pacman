import pygame as pg
from objects.ghost import Ghost
from objects.wall import Wall
from objects.lives import Lives


class Player(Ghost):
    def __init__(self, game, drawing, color):
        Ghost.__init__(self, game, drawing, color)
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
        self.prev_pos_x = self.rect.x
        self.prev_pos_y = self.rect.y
        self.lives = Lives(self.game)

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

    def check_collision(self, rect):
        return self.rect.colliderect(rect)

    def collides_with(self, obj):
        if isinstance(obj, Wall):
            if self.check_collision(obj):
                self.rect.x = self.prev_pos_x
                self.rect.y = self.prev_pos_y
                self.move_stop()

    def process_draw(self):
        self.prev_pos_x = self.rect.x
        self.prev_pos_y = self.rect.y
        self.rect.x = self.rect.x + self.current_shift_x
        self.rect.y = self.rect.y + self.current_shift_y
        self.game.screen.blit(self.img, self.rect)
        self.lives.process_draw()
