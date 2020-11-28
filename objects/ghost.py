import pygame as pg
import random


class Ghost:
    def respawn(self):
        self.rect.x = random.randint(341, 409)
        self.rect.y = 280
        f = random.randint(0, 1)
        if f == 0:
            self.speed_x = 1
        else:
            self.speed_x = -1
        del f
        self.speed_y = 0

    def __init__(self, game, drawing, color, kill_cost):
        self.angle = 0
        self.color = color
        self.game = game
        self.img = pg.image.load(drawing)
        self.width = 50
        self.height = 50
        self.img = pg.transform.scale(self.img, (self.width, self.height))
        self.rect = self.img.get_rect()
        self.kill_cost = kill_cost
        self.respawn()

    def process_logic(self):
        pass

    def move(self, speed):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y < 20:
            self.rect.y += 20 - self.rect.y
            self.speed_y = 0
            n = random.randint(0, 1)
            if n == 0:
                self.speed_x = speed
            else:
                self.speed_x = -speed
            del n
        if self.rect.y > 580 - self.height:
            self.rect.y -= (self.rect.y + self.height) - 580
            self.speed_y = 0
            n = random.randint(0, 1)
            if n == 0:
                self.speed_x = speed
            else:
                self.speed_x = -speed
            del n
        if (self.rect.x > 780 - self.width) and (self.rect.y < 275 or self.rect.y > 325):
            self.rect.x -= (self.rect.x + self.width) - 780
            self.speed_x = 0
            n = random.randint(0, 1)
            if n == 0:
                self.speed_y = speed
            else:
                self.speed_y = -speed
            del n
        if self.rect.x < 20 and self.rect.y != 275:
            self.rect.x += 20 - self.rect.x
            self.speed_x = 0
            n = random.randint(0, 1)
            if n == 0:
                self.speed_y = speed
            else:
                self.speed_y = -speed
            del n
        if self.rect.x == 410:
            if self.rect.y == 20:
                n = random.randint(0, 1)
                if n == 0:
                    self.speed_y = speed
                    self.speed_x = 0
                else:
                    self.speed_x = speed
                del n
            elif self.rect.y == 120:
                n = random.randint(0, 2)
                if n == 0:
                    self.speed_y = -speed
                    self.speed_x = 0
                elif n == 1:
                    self.speed_x = speed
                    self.speed_y = 0
                else:
                    self.speed_x = -speed
                    self.speed_y = 0
                del n
            elif self.rect.y == 580 - self.height:
                n = random.randint(0, 2)
                if n == 0:
                    self.speed_y = -speed
                    self.speed_x = 0
                elif n == 1:
                    self.speed_x = speed
                    self.speed_y = 0
                else:
                    self.speed_x = -speed
                    self.speed_y = 0
                del n
            elif self.rect.y == 580 - 160:
                n = random.randint(0, 1)
                if n == 0:
                    self.speed_y = speed
                    self.speed_x = 0
                else:
                    self.speed_x = speed
                    self.speed_y = 0
                del n
        if self.rect.x == 390 - self.width:
            if self.rect.y == 580 - self.height:
                n = random.randint(0, 2)
                if n == 0:
                    self.speed_y = -speed
                    self.speed_x = 0
                elif n == 1:
                    self.speed_x = speed
                    self.speed_y = 0
                else:
                    self.speed_x = -speed
                    self.speed_y = 0
                del n
            elif self.rect.y == 20:
                n = random.randint(0, 1)
                if n == 0:
                    self.speed_y = speed
                    self.speed_x = 0
                else:
                    self.speed_x = -speed
                del n
            elif self.rect.y == 580 - 160:
                n = random.randint(0, 1)
                if n == 0:
                    self.speed_y = speed
                    self.speed_x = 0
                else:
                    self.speed_x = -speed
                    self.speed_y = 0
                del n
        if self.rect.x == 270:
            if self.rect.y == 580 - 160:
                n = random.randint(0, 1)
                if n == 0:
                    self.speed_y = -speed
                    self.speed_x = 0
                else:
                    self.speed_x = speed
                    self.speed_y = 0
                del n
        if self.rect.x == 480:
            if self.rect.y == 580 - 160:
                n = random.randint(0, 1)
                if n == 0:
                    self.speed_y = -speed
                    self.speed_x = 0
                else:
                    self.speed_x = -speed
                    self.speed_y = 0
                del n
        if self.rect.y == 420:
            if self.rect.x == 20:
                n = random.randint(0, 1)
                if n == 0:
                    self.speed_y = speed
                    self.speed_x = 0
                else:
                    self.speed_x = speed
                    self.speed_y = 0
                del n
            elif self.rect.x == 160:
                n = random.randint(0, 1)
                if n == 0:
                    self.speed_y = -speed
                    self.speed_x = 0
                else:
                    self.speed_x = -speed
                    self.speed_y = 0
                del n
            elif self.rect.x == 410:
                n = random.randint(0, 1)
                if n == 0:
                    self.speed_y = speed
                    self.speed_x = 0
                else:
                    self.speed_x = speed
                    self.speed_y = 0
                del n
            elif self.rect.x == 530:
                n = random.randint(0, 1)
                if n == 0:
                    self.speed_y = -speed
                    self.speed_x = 0
                else:
                    self.speed_x = -speed
                    self.speed_y = 0
                del n
            elif self.rect.x == 590:
                n = random.randint(0, 1)
                if n == 0:
                    self.speed_y = -speed
                    self.speed_x = 0
                else:
                    self.speed_x = speed
                    self.speed_y = 0
                del n
            elif self.rect.x == 730:
                n = random.randint(0, 1)
                if n == 0:
                    self.speed_y = speed
                    self.speed_x = 0
                else:
                    self.speed_x = -speed
                    self.speed_y = 0
                del n
        if self.rect.y == 275:
            if self.rect.x == 160:
                n = random.randint(0, 1)
                if n == 0:
                    self.speed_y = -speed
                    self.speed_x = 0
                else:
                    self.speed_y = speed
                    self.speed_x = 0
                del n
            elif self.rect.x == 590:
                n = random.randint(0, 1)
                if n == 0:
                    self.speed_y = -speed
                    self.speed_x = 0
                else:
                    self.speed_y = speed
                    self.speed_x = 0
        if self.rect.y == 120:
            if self.rect.x == 390 - self.width:
                n = random.randint(0, 3)
                if n == 0:
                    self.speed_y = -speed
                    self.speed_x = 0
                elif n == 1:
                    self.speed_x = speed
                    self.speed_y = 0
                elif n == 2:
                    self.speed_y = speed
                    self.speed_x = 0
                else:
                    self.speed_x = -speed
                    self.speed_y = 0
                del n
            if self.rect.x == 160:
                n = random.randint(0, 3)
                if n == 0:
                    self.speed_y = -speed
                    self.speed_x = 0
                elif n == 1:
                    self.speed_x = speed
                    self.speed_y = 0
                elif n == 2:
                    self.speed_y = speed
                    self.speed_x = 0
                else:
                    self.speed_x = -speed
                    self.speed_y = 0
                del n
            if self.rect.x == 20:
                n = random.randint(0, 1)
                if n == 0:
                    self.speed_y = -speed
                    self.speed_x = 0
                else:
                    self.speed_x = speed
                    self.speed_y = 0
                del n
            if self.rect.x == 410:
                n = random.randint(0, 3)
                if n == 0:
                    self.speed_y = -speed
                    self.speed_x = 0
                elif n == 1:
                    self.speed_x = speed
                    self.speed_y = 0
                elif n == 2:
                    self.speed_y = speed
                    self.speed_x = 0
                else:
                    self.speed_x = -speed
                    self.speed_y = 0
                del n
            if self.rect.x == 590:
                n = random.randint(0, 3)
                if n == 0:
                    self.speed_y = -speed
                    self.speed_x = 0
                elif n == 1:
                    self.speed_x = speed
                    self.speed_y = 0
                elif n == 2:
                    self.speed_y = speed
                    self.speed_x = 0
                else:
                    self.speed_x = -speed
                    self.speed_y = 0
                del n
            if self.rect.x == 730:
                n = random.randint(0, 1)
                if n == 0:
                    self.speed_y = -speed
                    self.speed_x = 0
                elif n == 1:
                    self.speed_x = -speed
                    self.speed_y = 0
                del n
        if self.rect.y == 210:
            if self.rect.x == 270:
                n = random.randint(0, 1)
                if n == 0:
                    self.speed_y = speed
                    self.speed_x = 0
                else:
                    self.speed_x = speed
                    self.speed_y = 0
                del n
            elif self.rect.x == 340:
                n = random.randint(0, 2)
                if n == 0:
                    self.speed_y = -speed
                    self.speed_x = 0
                elif n == 1:
                    self.speed_x = speed
                    self.speed_y = 0
                else:
                    self.speed_x = -speed
                    self.speed_y = 0
                del n
            elif self.rect.x == 410:
                n = random.randint(0, 2)
                if n == 0:
                    self.speed_y = -speed
                    self.speed_x = 0
                elif n == 1:
                    self.speed_x = speed
                    self.speed_y = 0
                else:
                    self.speed_x = -speed
                    self.speed_y = 0
                del n
            elif self.rect.x == 480:
                n = random.randint(0, 1)
                if n == 0:
                    self.speed_y = speed
                    self.speed_x = 0
                else:
                    self.speed_x = -speed
                    self.speed_y = 0
                del n
            elif self.rect.x == 375:
                n = random.randint(0, 1)
                if n == 0:
                    self.speed_x = speed
                    self.speed_y = 0
                else:
                    self.speed_x = -speed
                    self.speed_y = 0
                del n
        if self.rect.y == 350:
            if self.rect.x == 160:
                n = random.randint(0, 2)
                if n == 0:
                    self.speed_x = speed
                    self.speed_y = 0
                elif n == 1:
                    self.speed_y = speed
                    self.speed_x = 0
                else:
                    self.speed_y = -speed
                    self.speed_x = 0
            if self.rect.x == 270:
                n = random.randint(0, 3)
                if n == 0:
                    self.speed_y = -speed
                    self.speed_x = 0
                elif n == 1:
                    self.speed_x = speed
                    self.speed_y = 0
                elif n == 2:
                    self.speed_y = speed
                    self.speed_x = 0
                else:
                    self.speed_x = -speed
                    self.speed_y = 0
                del n
            if self.rect.x == 480:
                n = random.randint(0, 3)
                if n == 0:
                    self.speed_y = -speed
                    self.speed_x = 0
                elif n == 1:
                    self.speed_x = speed
                    self.speed_y = 0
                elif n == 2:
                    self.speed_y = speed
                    self.speed_x = 0
                else:
                    self.speed_x = -speed
                    self.speed_y = 0
                del n
            if self.rect.x == 590:
                n = random.randint(0, 2)
                if n == 0:
                    self.speed_x = -speed
                    self.speed_y = 0
                elif n == 1:
                    self.speed_y = speed
                    self.speed_x = 0
                else:
                    self.speed_y = -speed
                    self.speed_x = 0
        if self.rect.y == 280:
            if self.rect.x == 340:
                self.speed_x = speed
                self.speed_y = 0
            if self.rect.x == 375:
                self.speed_x = 0
                self.speed_y = -speed
            if self.rect.x == 410:
                self.speed_x = -speed
                self.speed_y = 0

    def process_draw(self):
        speed = 5
        if self.color == "blue":
            if self.speed_x > 0:
                if self.angle != 0:
                    self.img = pg.image.load('images/BGHOST_0.png')
                    self.img = pg.transform.scale(self.img, (self.width, self.height))
                    self.angle = 0
            elif self.speed_x < 0:
                if self.angle != 180:
                    self.img = pg.image.load('images/BGHOST_180.png')
                    self.img = pg.transform.scale(self.img, (self.width, self.height))
                    self.angle = 180
            elif self.speed_y > 0:
                if self.angle != 270:
                    self.img = pg.image.load('images/BGHOST_270.png')
                    self.img = pg.transform.scale(self.img, (self.width, self.height))
                    self.angle = 270
            elif self.speed_y < 0:
                if self.angle != 90:
                    self.img = pg.image.load('images/BGHOST_90.png')
                    self.img = pg.transform.scale(self.img, (self.width, self.height))
                    self.angle = 90
        elif self.color == "red":
            if self.speed_x > 0:
                if self.angle != 0:
                    self.img = pg.image.load('images/RGHOST_0.png')
                    self.img = pg.transform.scale(self.img, (self.width, self.height))
                    self.angle = 0
            elif self.speed_x < 0:
                if self.angle != 180:
                    self.img = pg.image.load('images/RGHOST_180.png')
                    self.img = pg.transform.scale(self.img, (self.width, self.height))
                    self.angle = 180
            elif self.speed_y > 0:
                if self.angle != 270:
                    self.img = pg.image.load('images/RGHOST_270.png')
                    self.img = pg.transform.scale(self.img, (self.width, self.height))
                    self.angle = 270
            elif self.speed_y < 0:
                if self.angle != 90:
                    self.img = pg.image.load('images/RGHOST_90.png')
                    self.img = pg.transform.scale(self.img, (self.width, self.height))
                    self.angle = 90
        elif self.color == "pink":
            if self.speed_x > 0:
                if self.angle != 0:
                    self.img = pg.image.load('images/PGHOST_0.png')
                    self.img = pg.transform.scale(self.img, (self.width, self.height))
                    self.angle = 0
            elif self.speed_x < 0:
                if self.angle != 180:
                    self.img = pg.image.load('images/PGHOST_180.png')
                    self.img = pg.transform.scale(self.img, (self.width, self.height))
                    self.angle = 180
            elif self.speed_y > 0:
                if self.angle != 270:
                    self.img = pg.image.load('images/PGHOST_270.png')
                    self.img = pg.transform.scale(self.img, (self.width, self.height))
                    self.angle = 270
            elif self.speed_y < 0:
                if self.angle != 90:
                    self.img = pg.image.load('images/PGHOST_90.png')
                    self.img = pg.transform.scale(self.img, (self.width, self.height))
                    self.angle = 90
        else:
            if self.speed_x > 0:
                if self.angle != 0:
                    self.img = pg.image.load('images/YGHOST_0.png')
                    self.img = pg.transform.scale(self.img, (self.width, self.height))
                    self.angle = 0
            elif self.speed_x < 0:
                if self.angle != 180:
                    self.img = pg.image.load('images/YGHOST_180.png')
                    self.img = pg.transform.scale(self.img, (self.width, self.height))
                    self.angle = 180
            elif self.speed_y > 0:
                if self.angle != 270:
                    self.img = pg.image.load('images/YGHOST_270.png')
                    self.img = pg.transform.scale(self.img, (self.width, self.height))
                    self.angle = 270
            elif self.speed_y < 0:
                if self.angle != 90:
                    self.img = pg.image.load('images/YGHOST_90.png')
                    self.img = pg.transform.scale(self.img, (self.width, self.height))
                    self.angle = 90
        self.game.screen.blit(self.img, self.rect)
