import random

import pygame as pg

class Ghost:
    speed = [pg.math.Vector2(1, 0), pg.math.Vector2(0, -1), pg.math.Vector2(-1, 0), pg.math.Vector2(0, 1)]

    def respawn(self):
        self.crossroad = self.start_crossroad
        self.direction = self.start_direction

    def reload_image(self):
        filename = f'images/{self.color}GHOST_{self.direction * 90}.png'
        return pg.transform.scale(pg.image.load(filename), (self.width, self.height))

    def get_img_rect_coords(self):
        return self.x - self.width // 2, self.y - self.height // 2

    def __init__(self, game, color, kill_cost, start_crossroad, start_direction):
        self.color = color
        self.game = game
        self.direction = self.start_direction = start_direction
        self.crossroad = self.start_crossroad = start_crossroad
        self.x = self.crossroad.x
        self.y = self.crossroad.y
        self.width = 50
        self.height = 50
        self.img = self.reload_image()
        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = self.get_img_rect_coords()
        self.kill_cost = kill_cost

    def process_logic(self):
        pass

    def move(self, player_is_frightened):
        speed_factor = 5 if player_is_frightened else 2
        self.x += self.speed[self.direction].x * speed_factor
        self.y += self.speed[self.direction].y * speed_factor

        vec1 = pg.math.Vector2(self.x - self.crossroad.x, self.y - self.crossroad.y)
        vec2 = pg.math.Vector2(self.x - self.crossroad.neighbours[self.direction].x,
                               self.y - self.crossroad.neighbours[self.direction].y)

        if vec1.dot(vec2) > 0:
            self.crossroad = self.crossroad.neighbours[self.direction]
            self.x = self.crossroad.x
            self.y = self.crossroad.y
            self.direction = random.choice(list(i for i in range(4) if self.crossroad.neighbours[i] is not None))
            self.img = self.reload_image()

        self.rect.x, self.rect.y = self.get_img_rect_coords()

    def process_draw(self):
        self.game.screen.blit(self.img, self.rect)
