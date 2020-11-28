import pygame as pg
from objects.ghost import Ghost
from objects.wall import Wall
from objects.lives import Lives
from objects.seed import Seed
from objects.text import TextObject


class Player(Ghost):
    def respawn(self):
        self.rect.y = 530
        self.rect.x = 375
        self.is_dead = False

    def find_highest_score(self):
        for line in self.read:
            if self.highest_score < int(line):
                self.highest_score = int(line)
        self.read.close()
        self.Text_HScore.update_text(str(self.highest_score))
        temp = len(str(self.highest_score))
        self.HS_posx += (4 - temp) * 10
        self.Text_HScore.move_center(self.HS_posx, self.HS_posy)

    def __init__(self, game, drawing, color):
        Ghost.__init__(self, game, drawing, color)
        self.score = 0
        self.img = pg.image.load(drawing)
        self.width = 50
        self.height = 50
        self.img = pg.transform.scale(self.img, (self.width, self.height))
        self.rect = self.img.get_rect()
        self.speed_x = 0
        self.speed_y = 0
        self.respawn()
        self.pl_speed = 5
        self.current_shift_y = 0
        self.current_shift_x = 0
        self.prev_pos_x = self.rect.x
        self.prev_pos_y = self.rect.y
        self.lives = Lives(self.game)
        self.Text_Score = TextObject(self.game)
        self.Text_Score.move_center(400, 615)
        self.Text_HScore = TextObject(self.game)
        self.HS_posx = 758
        self.HS_posy = 615
        self.Text_HScore.move_center(self.HS_posx, self.HS_posy)
        self.read = open("high_scores/high_scores.txt", "r")
        self.write = open("high_scores/high_scores.txt", "a")
        self.highest_score = 0
        self.find_highest_score()

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
        if isinstance(obj, Player):
            return
        elif isinstance(obj, Wall):
            if self.check_collision(obj):
                self.rect.x = self.prev_pos_x
                self.rect.y = self.prev_pos_y
                self.move_stop()
        elif isinstance(obj, Ghost):
            if self.check_collision(obj.rect):
                self.is_dead = True
                self.lives.lives -= 1
        elif isinstance(obj, Seed) and obj.stay == True:
            if self.check_collision(obj.rect):
                self.score += 10
                print(self.score)
                obj.stay = False
                del obj.rect
    def check_tunnel(self):
        if self.rect.x == -50 and self.current_shift_x == -5:
            self.rect.x = 800
        elif self.rect.x == 800 and self.current_shift_x == 5:
            self.rect.x = -50
        self.rect.x = self.rect.x + self.current_shift_x
        self.rect.y = self.rect.y + self.current_shift_y
    def process_draw(self):
        self.Text_Score.update_text(str(self.score))
        self.Text_Score.process_draw()
        self.Text_HScore.process_draw()
        self.prev_pos_x = self.rect.x
        self.prev_pos_y = self.rect.y
        self.check_tunnel()
        self.game.screen.blit(self.img, self.rect)
        self.lives.process_draw()
