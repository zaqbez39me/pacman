import pygame
import random
import sys
import math
from math import pi
pygame.init()
pg = pygame
black = 0, 0, 0
aqua = 0, 255, 255
blue = 0, 0, 255
fuchsia = 255, 0, 255
gray = 128, 128, 128
clock = pygame.time.Clock()
myfont = pygame.font.SysFont("comicsansms", 30)
size = width, height = [800, 630]
screen = pygame.display.set_mode(size)


def logic(obj):
    speed = 5
    global size
    if obj.rect.y < 20:
        obj.rect.y += 20 - obj.rect.y
        obj.speed_y = 0
        n = random.randint(0, 1)
        if n == 0:
            obj.speed_x = speed
        else:
            obj.speed_x = -speed
        del n
    if obj.rect.y > 580 - obj.height:
        obj.rect.y -= (obj.rect.y + obj.height) - 580
        obj.speed_y = 0
        n = random.randint(0, 1)
        if n == 0:
            obj.speed_x = speed
        else:
            obj.speed_x = -speed
        del n
    if (obj.rect.x > 780 - obj.width) and (obj.rect.y < 275 or obj.rect.y > 325):
        obj.rect.x -= (obj.rect.x + obj.width) - 780
        obj.speed_x = 0
        n = random.randint(0, 1)
        if n == 0:
            obj.speed_y = speed
        else:
            obj.speed_y = -speed
        del n
    if obj.rect.x < 20 and obj.rect.y != 275:
        obj.rect.x += 20 - obj.rect.x
        obj.speed_x = 0
        n = random.randint(0, 1)
        if n == 0:
            obj.speed_y = speed
        else:
            obj.speed_y = -speed
        del n
    if obj.rect.x == 410:
        if obj.rect.y == 20:
            n = random.randint(0, 1)
            if n == 0:
                obj.speed_y = speed
                obj.speed_x = 0
            else:
                obj.speed_x = speed
            del n
        elif obj.rect.y == 120:
            n = random.randint(0, 2)
            if n == 0:
                obj.speed_y = -speed
                obj.speed_x = 0
            elif n == 1:
                obj.speed_x = speed
                obj.speed_y = 0
            else:
                obj.speed_x = -speed
                obj.speed_y = 0
            del n
        elif obj.rect.y == 580 - obj.height:
            n = random.randint(0, 2)
            if n == 0:
                obj.speed_y = -speed
                obj.speed_x = 0
            elif n == 1:
                obj.speed_x = speed
                obj.speed_y = 0
            else:
                obj.speed_x = -speed
                obj.speed_y = 0
            del n
        elif obj.rect.y == 580 - 160:
            n = random.randint(0, 1)
            if n == 0:
                obj.speed_y = speed
                obj.speed_x = 0
            else:
                obj.speed_x = speed
                obj.speed_y = 0
            del n
    if obj.rect.x == 390 - obj.width:
        if obj.rect.y == 580 - obj.height:
            n = random.randint(0, 2)
            if n == 0:
                obj.speed_y = -speed
                obj.speed_x = 0
            elif n == 1:
                obj.speed_x = speed
                obj.speed_y = 0
            else:
                obj.speed_x = -speed
                obj.speed_y = 0
            del n
        elif obj.rect.y == 20:
            n = random.randint(0, 1)
            if n == 0:
                obj.speed_y = speed
                obj.speed_x = 0
            else:
                obj.speed_x = -speed
            del n
        elif obj.rect.y == 580 - 160:
            n = random.randint(0, 1)
            if n == 0:
                obj.speed_y = speed
                obj.speed_x = 0
            else:
                obj.speed_x = -speed
                obj.speed_y = 0
            del n
    if obj.rect.x == 270:
        if obj.rect.y == 580 - 160:
            n = random.randint(0, 1)
            if n == 0:
                obj.speed_y = -speed
                obj.speed_x = 0
            else:
                obj.speed_x = speed
                obj.speed_y = 0
            del n
    if obj.rect.x == 480:
        if obj.rect.y == 580 - 160:
            n = random.randint(0, 1)
            if n == 0:
                obj.speed_y = -speed
                obj.speed_x = 0
            else:
                obj.speed_x = -speed
                obj.speed_y = 0
            del n
    if obj.rect.y == 420:
        if obj.rect.x == 20:
            n = random.randint(0, 1)
            if n == 0:
                obj.speed_y = speed
                obj.speed_x = 0
            else:
                obj.speed_x = speed
                obj.speed_y = 0
            del n
        elif obj.rect.x == 160:
            n = random.randint(0, 1)
            if n == 0:
                obj.speed_y = -speed
                obj.speed_x = 0
            else:
                obj.speed_x = -speed
                obj.speed_y = 0
            del n
        elif obj.rect.x == 410:
            n = random.randint(0, 1)
            if n == 0:
                obj.speed_y = speed
                obj.speed_x = 0
            else:
                obj.speed_x = speed
                obj.speed_y = 0
            del n
        elif obj.rect.x == 530:
            n = random.randint(0, 1)
            if n == 0:
                obj.speed_y = -speed
                obj.speed_x = 0
            else:
                obj.speed_x = -speed
                obj.speed_y = 0
            del n
        elif obj.rect.x == 590:
            n = random.randint(0, 1)
            if n == 0:
                obj.speed_y = -speed
                obj.speed_x = 0
            else:
                obj.speed_x = speed
                obj.speed_y = 0
            del n
        elif obj.rect.x == 730:
            n = random.randint(0, 1)
            if n == 0:
                obj.speed_y = speed
                obj.speed_x = 0
            else:
                obj.speed_x = -speed
                obj.speed_y = 0
            del n
    if obj.rect.y == 275:
        if obj.rect.x == 160:
            n = random.randint(0, 2)
            if n == 0:
                obj.speed_y = -speed
                obj.speed_x = 0
            elif n == 1:
                obj.speed_x = -speed
                obj.speed_y = 0
            else:
                obj.speed_y = speed
                obj.speed_x = 0
            del n
        elif obj.rect.x == -50:
            obj.rect.x = 800
            obj.speed_y = 0
            obj.speed_x = -speed
        elif obj.rect.x == 850:
            obj.rect.x = -50
            obj.speed_y = 0
            obj.speed_x = speed
        elif obj.rect.x == 590:
            n = random.randint(0, 2)
            if n == 0:
                obj.speed_y = -speed
                obj.speed_x = 0
            elif n == 1:
                obj.speed_x = speed
                obj.speed_y = 0
            else:
                obj.speed_y = speed
                obj.speed_x = 0
    if obj.rect.y == 120:
        if obj.rect.x == 390 - obj.width:
            n = random.randint(0, 3)
            if n == 0:
                obj.speed_y = -speed
                obj.speed_x = 0
            elif n == 1:
                obj.speed_x = speed
                obj.speed_y = 0
            elif n == 2:
                obj.speed_y = speed
                obj.speed_x = 0
            else:
                obj.speed_x = -speed
                obj.speed_y = 0
            del n
        if obj.rect.x == 160:
            n = random.randint(0, 3)
            if n == 0:
                obj.speed_y = -speed
                obj.speed_x = 0
            elif n == 1:
                obj.speed_x = speed
                obj.speed_y = 0
            elif n == 2:
                obj.speed_y = speed
                obj.speed_x = 0
            else:
                obj.speed_x = -speed
                obj.speed_y = 0
            del n
        if obj.rect.x == 20:
            n = random.randint(0, 1)
            if n == 0:
                obj.speed_y = -speed
                obj.speed_x = 0
            else:
                obj.speed_x = speed
                obj.speed_y = 0
            del n
        if obj.rect.x == 410:
            n = random.randint(0, 3)
            if n == 0:
                obj.speed_y = -speed
                obj.speed_x = 0
            elif n == 1:
                obj.speed_x = speed
                obj.speed_y = 0
            elif n == 2:
                obj.speed_y = speed
                obj.speed_x = 0
            else:
                obj.speed_x = -speed
                obj.speed_y = 0
            del n
        if obj.rect.x == 590:
            n = random.randint(0, 3)
            if n == 0:
                obj.speed_y = -speed
                obj.speed_x = 0
            elif n == 1:
                obj.speed_x = speed
                obj.speed_y = 0
            elif n == 2:
                obj.speed_y = speed
                obj.speed_x = 0
            else:
                obj.speed_x = -speed
                obj.speed_y = 0
            del n
        if obj.rect.x == 730:
            n = random.randint(0, 1)
            if n == 0:
                obj.speed_y = -speed
                obj.speed_x = 0
            elif n == 1:
                obj.speed_x = -speed
                obj.speed_y = 0
            del n
    if obj.rect.y == 210:
        if obj.rect.x == 270:
            n = random.randint(0, 1)
            if n == 0:
                obj.speed_y = speed
                obj.speed_x = 0
            else:
                obj.speed_x = speed
                obj.speed_y = 0
            del n
        elif obj.rect.x == 340:
            n = random.randint(0, 2)
            if n == 0:
                obj.speed_y = -speed
                obj.speed_x = 0
            elif n == 1:
                obj.speed_x = speed
                obj.speed_y = 0
            else:
                obj.speed_x = -speed
                obj.speed_y = 0
            del n
        elif obj.rect.x == 410:
            n = random.randint(0, 2)
            if n == 0:
                obj.speed_y = -speed
                obj.speed_x = 0
            elif n == 1:
                obj.speed_x = speed
                obj.speed_y = 0
            else:
                obj.speed_x = -speed
                obj.speed_y = 0
            del n
        elif obj.rect.x == 480:
            n = random.randint(0, 1)
            if n == 0:
                obj.speed_y = speed
                obj.speed_x = 0
            else:
                obj.speed_x = -speed
                obj.speed_y = 0
            del n
        elif obj.rect.x == 375:
            n = random.randint(0, 1)
            if n == 0:
                obj.speed_x = speed
                obj.speed_y = 0
            else:
                obj.speed_x = -speed
                obj.speed_y = 0
            del n
    if obj.rect.y == 350:
        if obj.rect.x == 160:
            n = random.randint(0, 2)
            if n == 0:
                obj.speed_x = speed
                obj.speed_y = 0
            elif n == 1:
                obj.speed_y = speed
                obj.speed_x = 0
            else:
                obj.speed_y = -speed
                obj.speed_x = 0
        if obj.rect.x == 270:
            n = random.randint(0, 3)
            if n == 0:
                obj.speed_y = -speed
                obj.speed_x = 0
            elif n == 1:
                obj.speed_x = speed
                obj.speed_y = 0
            elif n == 2:
                obj.speed_y = speed
                obj.speed_x = 0
            else:
                obj.speed_x = -speed
                obj.speed_y = 0
            del n
        if obj.rect.x == 480:
            n = random.randint(0, 3)
            if n == 0:
                obj.speed_y = -speed
                obj.speed_x = 0
            elif n == 1:
                obj.speed_x = speed
                obj.speed_y = 0
            elif n == 2:
                obj.speed_y = speed
                obj.speed_x = 0
            else:
                obj.speed_x = -speed
                obj.speed_y = 0
            del n
        if obj.rect.x == 590:
            n = random.randint(0, 2)
            if n == 0:
                obj.speed_x = -speed
                obj.speed_y = 0
            elif n == 1:
                obj.speed_y = speed
                obj.speed_x = 0
            else:
                obj.speed_y = -speed
                obj.speed_x = 0
    if obj.rect.y == 280:
        if obj.rect.x == 340:
             obj.speed_x = speed
             obj.speed_y = 0
        if obj.rect.x == 375:
            obj.speed_x = 0
            obj.speed_y = -speed
        if obj.rect.x == 410:
            obj.speed_x = -speed
            obj.speed_y = 0


def Otrisovka(rect, secs):
    if secs > 3:
        rect.rect.x += rect.speed_x
        rect.rect.y += rect.speed_y
        logic(rect)
    rect.draw()


def Otrisovka_Player(rect, walls):
    rect.rect.x += rect.speed_x
    rect.rect.y += rect.speed_y
    for i in range(len(walls)):
        if rect.check_collide(walls[i]):
            rect.rect.x = rect.prev_posx
            rect.rect.y = rect.prev_posy
            rect.movestop()
            break
    rect.draw()


class Wall:
    def __init__(self, x, y, width, height):
        self.img = pg.image.load('klipartz.com.png')
        if height >= 40:
            self.img = pygame.transform.rotate(self.img, 90)
            self.img = pygame.transform.scale(self.img, (width, height))
        else:
            self.img = pygame.transform.scale(self.img, (width, height))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen
        self.current_shift = 0
        self.width = width
        self.height = height

    def draw(self):
        self.drawer = screen.blit(self.img, self.rect)

    def collides_with(self, b):
        return self.rect.colliderect(b.rect)


class Ghost:
    def __init__(self, drawing):
        self.img = pg.image.load(drawing)
        self.width = 50
        self.height = 50
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(340, 410)
        self.rect.y = 280
        f = random.randint(0,1)
        if f == 0:
            self.speed_x = 1
        else:
            self.speed_x = -1
        del f
        self.speed_y = 0

    def collides_with(self, obj):
        if self.rect.colliderect(obj):
            self.speed_y *= -1

    def draw(self):
        self.drawer = screen.blit(self.img, self.rect)


class Lives:
    MAX_LIFES = 2
    def __init__(self):
        self.lifes = 2
        self.img = pg.image.load('pacman_0.png')
        self.width = 30
        self.height = 30
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.rect = self.img.get_rect()
    def draw(self):
        x = 0
        y = 600
        for i in range(self.lifes):
            self.rect.x = x
            self.rect.y = y
            self.drawer = screen.blit(self.img, self.rect)
            x += self.width


class Player(Ghost):
    def __init__(self, drawing):
        Ghost.__init__(self, drawing)
        self.img = pg.image.load(drawing)
        self.width = 50
        self.height = 50
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
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

    def moveright(self):
        if self.rect.x < 780 - self.width:
            self.current_shift_x = self.pl_speed
            self.current_shift_y = 0
        else:
            self.current_shift_x = 0

    def moveleft(self):
        if self.rect.x > 20:
            self.current_shift_x = -self.pl_speed
            self.current_shift_y = 0
        else:
            self.current_shift_x = 0

    def moveup(self):
        if self.rect.y > 20:
            self.current_shift_y = -self.pl_speed
            self.current_shift_x = 0
        else:
            self.current_shift_y = 0

    def movedown(self):
        if self.rect.y < 580 - self.height:
            self.current_shift_y = self.pl_speed
            self.current_shift_x = 0
        else:
            self.current_shift_y = 0

    def movestop(self):
        self.current_shift_x = 0
        self.current_shift_y = 0

    def check_collide(self, rect):
        return self.rect.colliderect(rect)

    def draw(self):
        self.prev_posx = self.rect.x
        self.prev_posy = self.rect.y
        self.rect.x = self.rect.x + self.current_shift_x
        self.rect.y = self.rect.y + self.current_shift_y
        self.drawer = screen.blit(self.img, self.rect)


def main():
    score = int(0)
    game_over = False
    global size
    global screen
    lt = list()
    walls = [Wall(375, 260, 50, 20), Wall(460, 510, 270, 20), Wall(460, 490, 270, 20), Wall(460, 470, 270, 20), Wall(70, 510, 270, 20), Wall(70, 490, 270, 20), Wall(70, 470, 270, 20), Wall(570, 400, 20, 70), Wall(550, 400, 20, 70), Wall(530, 400, 20, 70), Wall(250, 400, 20, 70), Wall(230, 400, 20, 70), Wall(210, 400, 20, 70), Wall(730, 400, 50, 20), Wall(210, 70, 130, 25), Wall(460, 70, 130, 25), Wall(210, 95, 130, 25), Wall(460, 95, 130, 25), Wall(70, 70, 90, 25), Wall(640, 70, 90, 25), Wall(70, 95, 90, 25), Wall(640, 95, 90, 25), Wall(340, 260, 35, 20), Wall(425, 260, 35, 20), Wall(320, 260, 20, 70), Wall(460, 260, 20, 70), Wall(530, 170, 20, 180), Wall(550, 170, 20, 180), Wall(570, 170, 20, 180), Wall(210, 170, 20, 180), Wall(230, 170, 20, 180), Wall(250, 170, 20, 180), Wall(390, 170, 20, 40), Wall(640, 345, 20, 55), Wall(660, 345, 20, 55), Wall(680, 345, 20, 55), Wall(700, 345, 20, 55), Wall(720, 345, 20, 55), Wall(740, 345, 20, 55), Wall(760, 345, 20, 55), Wall(20, 345, 20, 55), Wall(40, 345, 20, 55), Wall(60, 345, 20, 55), Wall(80, 345, 20, 55), Wall(100, 345, 20, 55), Wall(120, 345, 20, 55), Wall(140, 345, 20, 55), Wall(780, 325, 20, 275), Wall(780, 0, 20, 275), Wall(0, 580, 800, 20), Wall(0, 325, 20, 275), Wall(0, 0, 20, 275), Wall(0, 0, 800, 20), Wall(390, 420, 20, 110), Wall(390, 20, 20, 100), Wall(20, 170, 140, 20), Wall(20, 255, 140, 20), Wall(20, 325, 140, 20), Wall(320, 330, 160, 20), Wall(320, 400, 160, 20), Wall(20, 400, 140, 20) , Wall(640, 400, 140, 20), Wall(640, 325, 140, 20), Wall(640, 255, 140, 20), Wall(640, 170, 140, 20), Wall(20, 190, 20, 65), Wall(40, 190, 20, 65), Wall(60, 190, 20, 65), Wall(80, 190, 20, 65), Wall(100, 190, 20, 65), Wall(120, 190, 20, 65), Wall(140, 190, 20, 65), Wall(640, 190, 20, 65), Wall(660, 190, 20, 65), Wall(680, 190, 20, 65), Wall(700, 190, 20, 65), Wall(720, 190, 20, 65), Wall(740, 190, 20, 65), Wall(760, 190, 20, 65), Wall(270, 170, 70, 20), Wall(270, 190, 70, 20), Wall(460, 170, 70, 20), Wall(460, 190, 70, 20)]
    start_ticks = pygame.time.get_ticks()
    Ghosts = [Ghost('YGHOST.png'), Ghost('BGHOST.png'), Ghost('PGHOST.png'), Ghost('RGHOST.png')]
    Player1 = Player('pacman_0.png')
    Life = Lives()
    motion = "STOP"
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pg.VIDEORESIZE:
                print(f'Resize window: [{event.w}, {event.h}]')
                screen_size = width, height = event.w, event.h
                screen = pg.display.set_mode(screen_size, pg.RESIZABLE)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    Player1.rect.x += 5
                    for i in range(len(walls)):
                        motion = "RIGHT"
                elif event.key == pygame.K_a:
                        motion = "LEFT"
                elif event.key == pygame.K_s:
                        motion = "DOWN"
                elif event.key == pygame.K_w:
                        motion = "UP"
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_d, pygame.K_a, pygame.K_s, pygame.K_w]:
                    motion = "STOP"
        if motion == 'RIGHT':
            Player1.moveright()
            Player1.img = pg.image.load('pacman_0.png')
            Player1.img = pygame.transform.scale(Player1.img, (Player1.width, Player1.height))
        elif motion == 'LEFT':
            Player1.moveleft()
            Player1.img = pg.image.load('pacman_180.png')
            Player1.img = pygame.transform.scale(Player1.img, (Player1.width, Player1.height))
        elif motion == 'UP':
            Player1.moveup()
            Player1.img = pg.image.load('pacman_90.png')
            Player1.img = pygame.transform.scale(Player1.img, (Player1.width, Player1.height))
        elif motion == 'DOWN':
            Player1.movedown()
            Player1.img = pg.image.load('pacman_270.png')
            Player1.img = pygame.transform.scale(Player1.img, (Player1.width, Player1.height))
        clock.tick(60)
        screen.fill(black)
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        for i in range(4):
            Otrisovka(Ghosts[i], seconds)
        Otrisovka_Player(Player1, walls)
        Life.draw()
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        if seconds < 3:
            walls[0].draw()
        if seconds > 3:
            if len(walls) == 83:
                walls = walls[1:]
            else:
                pass

        for i in range(len(walls)):
            walls[i].draw()
        pygame.display.flip()
        pygame.time.wait(40)
    print("Вы проиграли")
    pygame.time.wait(1000)
    sys.exit()


if __name__ == '__main__':
    main()