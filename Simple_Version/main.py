import random
import sys

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


class Ghost:
    def __init__(self, drawing, size, screen):
        self.size = size
        self.screen = screen
        self.img = pg.image.load(drawing)
        self.width = 50
        self.height = 50
        self.img = pg.transform.scale(self.img, (self.width, self.height))
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(340, 410)
        self.rect.y = 280
        f = random.randint(0, 1)
        if f == 0:
            self.speed_x = 1
        else:
            self.speed_x = -1
        del f
        self.speed_y = 0

    def collides_with(self, obj):
        if self.rect.colliderect(obj):
            self.speed_y *= -1

    def move(self, secs):
        if secs > 3:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            speed = 5
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
                    n = random.randint(0, 2)
                    if n == 0:
                        self.speed_y = -speed
                        self.speed_x = 0
                    elif n == 1:
                        self.speed_x = -speed
                        self.speed_y = 0
                    else:
                        self.speed_y = speed
                        self.speed_x = 0
                    del n
                elif self.rect.x == -50:
                    self.rect.x = 800
                    self.speed_y = 0
                    self.speed_x = -speed
                elif self.rect.x == 850:
                    self.rect.x = -50
                    self.speed_y = 0
                    self.speed_x = speed
                elif self.rect.x == 590:
                    n = random.randint(0, 2)
                    if n == 0:
                        self.speed_y = -speed
                        self.speed_x = 0
                    elif n == 1:
                        self.speed_x = speed
                        self.speed_y = 0
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

    def draw(self):
        self.screen.blit(self.img, self.rect)


class Lives:
    MAX_LIFES = 2

    def __init__(self, size, screen):
        self.screen = screen
        self.lifes = 2
        self.img = pg.image.load('pacman_0.png')
        self.width = 30
        self.height = 30
        self.img = pg.transform.scale(self.img, (self.width, self.height))
        self.rect = self.img.get_rect()

    def draw(self):
        x = 0
        y = 600
        for i in range(self.lifes):
            self.rect.x = x
            self.rect.y = y
            self.screen.blit(self.img, self.rect)
            x += self.width


class Player(Ghost):
    def __init__(self, drawing, size, screen):
        Ghost.__init__(self, drawing, size, screen)
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
        self.img = pg.image.load('pacman_0.png')
        self.img = pg.transform.scale(self.img, (self.width, self.height))

    def move_left(self):
        if self.rect.x > 20:
            self.current_shift_x = -self.pl_speed
            self.current_shift_y = 0
        else:
            self.current_shift_x = 0
        self.img = pg.image.load('pacman_180.png')
        self.img = pg.transform.scale(self.img, (self.width, self.height))

    def move_up(self):
        if self.rect.y > 20:
            self.current_shift_y = -self.pl_speed
            self.current_shift_x = 0
        else:
            self.current_shift_y = 0
        self.img = pg.image.load('pacman_90.png')
        self.img = pg.transform.scale(self.img, (self.width, self.height))

    def move_down(self):
        if self.rect.y < 580 - self.height:
            self.current_shift_y = self.pl_speed
            self.current_shift_x = 0
        else:
            self.current_shift_y = 0
        self.img = pg.image.load('pacman_270.png')
        self.img = pg.transform.scale(self.img, (self.width, self.height))

    def move_stop(self):
        self.current_shift_x = 0
        self.current_shift_y = 0

    def check_collide(self, rect):
        return self.rect.colliderect(rect)

    def collide_walls(self, walls):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        for i in range(len(walls)):
            if self.check_collide(walls[i]):
                self.rect.x = self.prev_posx
                self.rect.y = self.prev_posy
                self.move_stop()
                break

    def draw(self):
        self.prev_posx = self.rect.x
        self.prev_posy = self.rect.y
        self.rect.x = self.rect.x + self.current_shift_x
        self.rect.y = self.rect.y + self.current_shift_y
        self.screen.blit(self.img, self.rect)


def main():
    pg.init()
    clock = pg.time.Clock()
    game_over = False
    size = width, height = [800, 630]
    screen = pg.display.set_mode(size)
    walls = [Wall(375, 260, 50, 20, size, screen), Wall(460, 510, 270, 20, size, screen),
             Wall(460, 490, 270, 20, size, screen), Wall(460, 470, 270, 20, size, screen),
             Wall(70, 510, 270, 20, size, screen), Wall(70, 490, 270, 20, size, screen),
             Wall(70, 470, 270, 20, size, screen), Wall(570, 400, 20, 70, size, screen),
             Wall(550, 400, 20, 70, size, screen), Wall(530, 400, 20, 70, size, screen),
             Wall(250, 400, 20, 70, size, screen), Wall(230, 400, 20, 70, size, screen),
             Wall(210, 400, 20, 70, size, screen), Wall(730, 400, 50, 20, size, screen),
             Wall(210, 70, 130, 25, size, screen), Wall(460, 70, 130, 25, size, screen),
             Wall(210, 95, 130, 25, size, screen), Wall(460, 95, 130, 25, size, screen),
             Wall(70, 70, 90, 25, size, screen), Wall(640, 70, 90, 25, size, screen),
             Wall(70, 95, 90, 25, size, screen), Wall(640, 95, 90, 25, size, screen),
             Wall(340, 260, 35, 20, size, screen), Wall(425, 260, 35, 20, size, screen),
             Wall(320, 260, 20, 70, size, screen), Wall(460, 260, 20, 70, size, screen),
             Wall(530, 170, 20, 180, size, screen), Wall(550, 170, 20, 180, size, screen),
             Wall(570, 170, 20, 180, size, screen), Wall(210, 170, 20, 180, size, screen),
             Wall(230, 170, 20, 180, size, screen), Wall(250, 170, 20, 180, size, screen),
             Wall(390, 170, 20, 40, size, screen), Wall(640, 345, 20, 55, size, screen),
             Wall(660, 345, 20, 55, size, screen), Wall(680, 345, 20, 55, size, screen),
             Wall(700, 345, 20, 55, size, screen), Wall(720, 345, 20, 55, size, screen),
             Wall(740, 345, 20, 55, size, screen), Wall(760, 345, 20, 55, size, screen),
             Wall(20, 345, 20, 55, size, screen), Wall(40, 345, 20, 55, size, screen),
             Wall(60, 345, 20, 55, size, screen), Wall(80, 345, 20, 55, size, screen),
             Wall(100, 345, 20, 55, size, screen), Wall(120, 345, 20, 55, size, screen),
             Wall(140, 345, 20, 55, size, screen), Wall(780, 325, 20, 275, size, screen),
             Wall(780, 0, 20, 275, size, screen), Wall(0, 580, 800, 20, size, screen),
             Wall(0, 325, 20, 275, size, screen), Wall(0, 0, 20, 275, size, screen), Wall(0, 0, 800, 20, size, screen),
             Wall(390, 420, 20, 110, size, screen), Wall(390, 20, 20, 100, size, screen),
             Wall(20, 170, 140, 20, size, screen), Wall(20, 255, 140, 20, size, screen),
             Wall(20, 325, 140, 20, size, screen), Wall(320, 330, 160, 20, size, screen),
             Wall(320, 400, 160, 20, size, screen), Wall(20, 400, 140, 20, size, screen),
             Wall(640, 400, 140, 20, size, screen), Wall(640, 325, 140, 20, size, screen),
             Wall(640, 255, 140, 20, size, screen), Wall(640, 170, 140, 20, size, screen),
             Wall(20, 190, 20, 65, size, screen), Wall(40, 190, 20, 65, size, screen),
             Wall(60, 190, 20, 65, size, screen), Wall(80, 190, 20, 65, size, screen),
             Wall(100, 190, 20, 65, size, screen), Wall(120, 190, 20, 65, size, screen),
             Wall(140, 190, 20, 65, size, screen), Wall(640, 190, 20, 65, size, screen),
             Wall(660, 190, 20, 65, size, screen), Wall(680, 190, 20, 65, size, screen),
             Wall(700, 190, 20, 65, size, screen), Wall(720, 190, 20, 65, size, screen),
             Wall(740, 190, 20, 65, size, screen), Wall(760, 190, 20, 65, size, screen),
             Wall(270, 170, 70, 20, size, screen), Wall(270, 190, 70, 20, size, screen),
             Wall(460, 170, 70, 20, size, screen), Wall(460, 190, 70, 20, size, screen)]
    start_ticks = pg.time.get_ticks()
    ghosts = [Ghost('YGHOST.png', size, screen), Ghost('BGHOST.png', size, screen), Ghost('PGHOST.png', size, screen),
              Ghost('RGHOST.png', size, screen)]
    player = Player('pacman_0.png', size, screen)
    lives = Lives(size, screen)
    while not game_over:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True
            elif event.type == pg.VIDEORESIZE:
                print(f'Resize window: [{event.w}, {event.h}]')
                screen_size = width, height = event.w, event.h
                screen = pg.display.set_mode(screen_size, pg.RESIZABLE)
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    player.move_right()
                elif event.key == pg.K_a:
                    player.move_left()
                elif event.key == pg.K_s:
                    player.move_down()
                elif event.key == pg.K_w:
                    player.move_up()
        clock.tick(60)
        screen.fill((0, 0, 0))
        seconds = (pg.time.get_ticks() - start_ticks) / 1000
        for i in range(4):
            ghosts[i].move(seconds)
            ghosts[i].draw()
        player.collide_walls(walls)
        player.draw()
        lives.draw()
        seconds = (pg.time.get_ticks() - start_ticks) / 1000
        if seconds > 3 and len(walls) == 83:
            walls = walls[1:]
        for i in range(len(walls)):
            walls[i].draw()
        pg.display.flip()
        pg.time.wait(40)
    print("Вы проиграли")
    pg.time.wait(1000)
    sys.exit()


if __name__ == '__main__':
    main()
