from random import randint
from typing import Tuple

import pygame

from constants import Color
from objects import BallObject, TextObject, Wall, Player, Ghost, Lives
from scenes import BaseScene


class MainScene(BaseScene):
    INITIAL_WALLS_COUNT = 83

    def create_objects(self) -> None:
        self.player = Player(self.game, 'images/pacman_0.png')
        self.ghosts = [Ghost(self.game, 'images/YGHOST.png'), Ghost(self.game, 'images/BGHOST.png'),
                       Ghost(self.game, 'images/PGHOST.png'), Ghost(self.game, 'images/RGHOST.png')]
        self.walls = [Wall(self.game, 375, 260, 50, 20), Wall(self.game, 460, 510, 270, 20),
                      Wall(self.game, 460, 490, 270, 20), Wall(self.game, 460, 470, 270, 20),
                      Wall(self.game, 70, 510, 270, 20), Wall(self.game, 70, 490, 270, 20),
                      Wall(self.game, 70, 470, 270, 20), Wall(self.game, 570, 400, 20, 70),
                      Wall(self.game, 550, 400, 20, 70), Wall(self.game, 530, 400, 20, 70),
                      Wall(self.game, 250, 400, 20, 70), Wall(self.game, 230, 400, 20, 70),
                      Wall(self.game, 210, 400, 20, 70), Wall(self.game, 730, 400, 50, 20),
                      Wall(self.game, 210, 70, 130, 25), Wall(self.game, 460, 70, 130, 25),
                      Wall(self.game, 210, 95, 130, 25), Wall(self.game, 460, 95, 130, 25),
                      Wall(self.game, 70, 70, 90, 25), Wall(self.game, 640, 70, 90, 25),
                      Wall(self.game, 70, 95, 90, 25), Wall(self.game, 640, 95, 90, 25),
                      Wall(self.game, 340, 260, 35, 20), Wall(self.game, 425, 260, 35, 20),
                      Wall(self.game, 320, 260, 20, 70), Wall(self.game, 460, 260, 20, 70),
                      Wall(self.game, 530, 170, 20, 180), Wall(self.game, 550, 170, 20, 180),
                      Wall(self.game, 570, 170, 20, 180), Wall(self.game, 210, 170, 20, 180),
                      Wall(self.game, 230, 170, 20, 180), Wall(self.game, 250, 170, 20, 180),
                      Wall(self.game, 390, 170, 20, 40), Wall(self.game, 640, 345, 20, 55),
                      Wall(self.game, 660, 345, 20, 55), Wall(self.game, 680, 345, 20, 55),
                      Wall(self.game, 700, 345, 20, 55), Wall(self.game, 720, 345, 20, 55),
                      Wall(self.game, 740, 345, 20, 55), Wall(self.game, 760, 345, 20, 55),
                      Wall(self.game, 20, 345, 20, 55), Wall(self.game, 40, 345, 20, 55),
                      Wall(self.game, 60, 345, 20, 55), Wall(self.game, 80, 345, 20, 55),
                      Wall(self.game, 100, 345, 20, 55), Wall(self.game, 120, 345, 20, 55),
                      Wall(self.game, 140, 345, 20, 55), Wall(self.game, 780, 325, 20, 275),
                      Wall(self.game, 780, 0, 20, 275), Wall(self.game, 0, 580, 800, 20),
                      Wall(self.game, 0, 325, 20, 275), Wall(self.game, 0, 0, 20, 275),
                      Wall(self.game, 0, 0, 800, 20),
                      Wall(self.game, 390, 420, 20, 110), Wall(self.game, 390, 20, 20, 100),
                      Wall(self.game, 20, 170, 140, 20), Wall(self.game, 20, 255, 140, 20),
                      Wall(self.game, 20, 325, 140, 20), Wall(self.game, 320, 330, 160, 20),
                      Wall(self.game, 320, 400, 160, 20), Wall(self.game, 20, 400, 140, 20),
                      Wall(self.game, 640, 400, 140, 20), Wall(self.game, 640, 325, 140, 20),
                      Wall(self.game, 640, 255, 140, 20), Wall(self.game, 640, 170, 140, 20),
                      Wall(self.game, 20, 190, 20, 65), Wall(self.game, 40, 190, 20, 65),
                      Wall(self.game, 60, 190, 20, 65), Wall(self.game, 80, 190, 20, 65),
                      Wall(self.game, 100, 190, 20, 65), Wall(self.game, 120, 190, 20, 65),
                      Wall(self.game, 140, 190, 20, 65), Wall(self.game, 640, 190, 20, 65),
                      Wall(self.game, 660, 190, 20, 65), Wall(self.game, 680, 190, 20, 65),
                      Wall(self.game, 700, 190, 20, 65), Wall(self.game, 720, 190, 20, 65),
                      Wall(self.game, 740, 190, 20, 65), Wall(self.game, 760, 190, 20, 65),
                      Wall(self.game, 270, 170, 70, 20), Wall(self.game, 270, 190, 70, 20),
                      Wall(self.game, 460, 170, 70, 20), Wall(self.game, 460, 190, 70, 20)]
        
        self.objects = self.walls + self.ghosts + [self.player]

    def process_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.player.move_right()
            elif event.key == pygame.K_a:
                self.player.move_left()
            elif event.key == pygame.K_s:
                self.player.move_down()
            elif event.key == pygame.K_w:
                self.player.move_up()
            elif event.key == pygame.K_ESCAPE:
                self.game.set_scene(self.game.PAUSE_SCENE_INDEX)

    def on_activate(self) -> None:
        self.create_objects()
        self.start_ticks = pygame.time.get_ticks()

    def time_from_activation(self):
        return (pygame.time.get_ticks() - self.start_ticks) / 1000

    def check_game_over(self) -> None:
        # if self.collision_count >= MainScene.MAX_COLLISIONS:
        #     self.game.set_scene(self.game.GAMEOVER_SCENE_INDEX)
        pass

    def ghosts_logic(self):
        if self.time_from_activation() > 3:
            if len(self.walls) == MainScene.INITIAL_WALLS_COUNT:
                del self.walls[0]
                self.objects = self.walls + self.ghosts + [self.player]

            for item in self.ghosts:
                item.move()

    def check_player_collisions(self):
        for item in self.objects:
            self.player.collides_with(item)

    def additional_logic(self) -> None:
        self.check_game_over()
        self.check_player_collisions()
        self.ghosts_logic()
