from random import randint
from typing import Tuple

import pygame

from constants import Color
from objects import BallObject, TextObject, Wall, Player, Ghost, Seed, Crossroad, Road
from scenes import BaseScene


class MainScene(BaseScene):
    INITIAL_WALLS_COUNT = 83

    def generate_seeds(self):
        seeds = []
        for road in self.roads:
            seeds.append(Seed(self.game, road.lx, road.ly))
            seeds.append(Seed(self.game, road.rx, road.ry))

            if road.len_x() > 0:
                for x in range(road.lx + road.step, road.rx - Seed.DIAMETER, road.step):
                    seeds.append(Seed(self.game, x, road.ly))
            elif road.len_y() > 0:
                for y in range(road.ly + road.step, road.ry - Seed.DIAMETER, road.step):
                    seeds.append(Seed(self.game, road.lx, y))

        return seeds

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

        self.crossroads = [Crossroad(46, 48), Crossroad(184, 48), Crossroad(365, 48), Crossroad(435, 48),
                           Crossroad(615, 48), Crossroad(758, 48), Crossroad(46, 150), Crossroad(184, 150),
                           Crossroad(365, 150), Crossroad(435, 150), Crossroad(615, 150), Crossroad(758, 150),
                           Crossroad(296, 238), Crossroad(365, 238), Crossroad(435, 238), Crossroad(508, 238),
                           Crossroad(18, 300), Crossroad(184, 300), Crossroad(615, 300), Crossroad(775, 300),
                           Crossroad(184, 376), Crossroad(296, 376), Crossroad(508, 376), Crossroad(615, 376),
                           Crossroad(46, 446), Crossroad(184, 446), Crossroad(296, 446), Crossroad(365, 446),
                           Crossroad(435, 446), Crossroad(508, 446), Crossroad(615, 446), Crossroad(758, 446),
                           Crossroad(46, 556), Crossroad(365, 556), Crossroad(435, 556), Crossroad(758, 556)]
        self.roads = [Road(self.crossroads[0], self.crossroads[1]), Road(self.crossroads[1], self.crossroads[2]),
                      Road(self.crossroads[3], self.crossroads[4]), Road(self.crossroads[4], self.crossroads[5]),
                      Road(self.crossroads[6], self.crossroads[7]), Road(self.crossroads[7], self.crossroads[8]),
                      Road(self.crossroads[9], self.crossroads[10]), Road(self.crossroads[10], self.crossroads[11]),
                      Road(self.crossroads[12], self.crossroads[13]), Road(self.crossroads[13], self.crossroads[14]),
                      Road(self.crossroads[14], self.crossroads[15]), Road(self.crossroads[16], self.crossroads[17]),
                      Road(self.crossroads[18], self.crossroads[19]), Road(self.crossroads[20], self.crossroads[21]),
                      Road(self.crossroads[21], self.crossroads[22]), Road(self.crossroads[22], self.crossroads[23]),
                      Road(self.crossroads[24], self.crossroads[25]), Road(self.crossroads[26], self.crossroads[27]),
                      Road(self.crossroads[28], self.crossroads[29]), Road(self.crossroads[30], self.crossroads[31]),
                      Road(self.crossroads[32], self.crossroads[33]), Road(self.crossroads[34], self.crossroads[35]),
                      Road(self.crossroads[0], self.crossroads[6]), Road(self.crossroads[24], self.crossroads[32]),
                      Road(self.crossroads[1], self.crossroads[7]), Road(self.crossroads[7], self.crossroads[17]),
                      Road(self.crossroads[17], self.crossroads[20]), Road(self.crossroads[20], self.crossroads[25]),
                      Road(self.crossroads[12], self.crossroads[21]), Road(self.crossroads[21], self.crossroads[26]),
                      Road(self.crossroads[2], self.crossroads[8]), Road(self.crossroads[8], self.crossroads[13]),
                      Road(self.crossroads[27], self.crossroads[33]), Road(self.crossroads[3], self.crossroads[9]),
                      Road(self.crossroads[9], self.crossroads[14]), Road(self.crossroads[28], self.crossroads[34]),
                      Road(self.crossroads[8], self.crossroads[9]), Road(self.crossroads[33], self.crossroads[34]),
                      Road(self.crossroads[22], self.crossroads[29]), Road(self.crossroads[23], self.crossroads[30]),
                      Road(self.crossroads[18], self.crossroads[23]), Road(self.crossroads[18], self.crossroads[10]),
                      Road(self.crossroads[10], self.crossroads[4]), Road(self.crossroads[15], self.crossroads[22]),
                      Road(self.crossroads[5], self.crossroads[11]), Road(self.crossroads[31], self.crossroads[35])]

        self.seeds = self.generate_seeds()
        self.objects = self.seeds + self.walls + self.ghosts + [self.player]

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
            elif event.key == pygame.K_p:
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
                self.objects = self.seeds + self.walls + self.ghosts + [self.player]

            for item in self.ghosts:
                item.move()

    def check_player_collisions(self):
        for item in self.objects:
            self.player.collides_with(item)

    def additional_logic(self) -> None:
        self.check_game_over()
        self.check_player_collisions()
        self.ghosts_logic()
