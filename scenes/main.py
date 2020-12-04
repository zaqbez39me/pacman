import pygame

from objects import Wall, Player, Ghost, Seed, Crossroad, Road, Energizer
from scenes import BaseScene


class MainScene(BaseScene):
    INITIAL_WALLS_COUNT = 83

    def move_to_spawn(self):
        self.player.respawn()
        for ghost in self.ghosts:
            ghost.respawn()

    def generate_seeds(self):
        seeds = []
        for road in self.seeds_roads:
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
        self.crossroads = [Crossroad(46, 48), Crossroad(184, 48), Crossroad(365, 48), Crossroad(435, 48),
                           Crossroad(615, 48), Crossroad(758, 48), Crossroad(46, 150), Crossroad(184, 150),
                           Crossroad(365, 150), Crossroad(435, 150), Crossroad(615, 150), Crossroad(758, 150),
                           Crossroad(296, 238), Crossroad(365, 238), Crossroad(435, 238), Crossroad(508, 238),
                           Crossroad(18, 300), Crossroad(184, 300), Crossroad(615, 300), Crossroad(775, 300),
                           Crossroad(184, 376), Crossroad(296, 376), Crossroad(508, 376), Crossroad(615, 376),
                           Crossroad(46, 446), Crossroad(184, 446), Crossroad(296, 446), Crossroad(365, 446),
                           Crossroad(435, 446), Crossroad(508, 446), Crossroad(615, 446), Crossroad(758, 446),
                           Crossroad(46, 556), Crossroad(365, 556), Crossroad(435, 556), Crossroad(758, 556),
                           Crossroad(400, 238), Crossroad(400, 300)]

        self.crossroads[0].neighbours = [self.crossroads[1], None, None, self.crossroads[6]]
        self.crossroads[1].neighbours = [self.crossroads[2], None, self.crossroads[0], self.crossroads[7]]
        self.crossroads[2].neighbours = [None, None, self.crossroads[1], self.crossroads[8]]
        self.crossroads[3].neighbours = [self.crossroads[4], None, None, self.crossroads[9]]
        self.crossroads[4].neighbours = [self.crossroads[5], None, self.crossroads[3], self.crossroads[10]]
        self.crossroads[5].neighbours = [None, None, self.crossroads[4], self.crossroads[11]]
        self.crossroads[6].neighbours = [self.crossroads[7], self.crossroads[0], None, None]
        self.crossroads[7].neighbours = [self.crossroads[8], self.crossroads[1], self.crossroads[6], self.crossroads[17]]
        self.crossroads[8].neighbours = [self.crossroads[9], self.crossroads[2], self.crossroads[7], self.crossroads[13]]
        self.crossroads[9].neighbours = [self.crossroads[10], self.crossroads[3], self.crossroads[8], self.crossroads[14]]
        self.crossroads[10].neighbours = [self.crossroads[11], self.crossroads[4], self.crossroads[9], self.crossroads[18]]
        self.crossroads[11].neighbours = [None, self.crossroads[5], self.crossroads[10], None]
        self.crossroads[12].neighbours = [self.crossroads[13], None, None, self.crossroads[21]]
        self.crossroads[13].neighbours = [self.crossroads[36], self.crossroads[8], self.crossroads[12], None]
        self.crossroads[14].neighbours = [self.crossroads[15], self.crossroads[9], self.crossroads[36], None]
        self.crossroads[15].neighbours = [None, None, self.crossroads[14], self.crossroads[22]]
        self.crossroads[16].neighbours = [self.crossroads[17], None, None, None]
        self.crossroads[17].neighbours = [None, self.crossroads[7], self.crossroads[16], self.crossroads[20]]
        self.crossroads[18].neighbours = [self.crossroads[19], self.crossroads[10], None, self.crossroads[23]]
        self.crossroads[19].neighbours = [None, None, self.crossroads[18], None]
        self.crossroads[20].neighbours = [self.crossroads[21], self.crossroads[17], None, self.crossroads[25]]
        self.crossroads[21].neighbours = [self.crossroads[22], self.crossroads[12], self.crossroads[20], self.crossroads[26]]
        self.crossroads[22].neighbours = [self.crossroads[23], self.crossroads[15], self.crossroads[21], self.crossroads[29]]
        self.crossroads[23].neighbours = [None, self.crossroads[18], self.crossroads[22], self.crossroads[30]]
        self.crossroads[24].neighbours = [self.crossroads[25], None, None, self.crossroads[32]]
        self.crossroads[25].neighbours = [None, self.crossroads[20], self.crossroads[24], None]
        self.crossroads[26].neighbours = [self.crossroads[27], self.crossroads[21], None, None]
        self.crossroads[27].neighbours = [None, None, self.crossroads[26], self.crossroads[33]]
        self.crossroads[28].neighbours = [self.crossroads[29], None, None, self.crossroads[34]]
        self.crossroads[29].neighbours = [None, self.crossroads[22], self.crossroads[28], None]
        self.crossroads[30].neighbours = [self.crossroads[31], self.crossroads[23], None, None]
        self.crossroads[31].neighbours = [None, None, self.crossroads[30], self.crossroads[35]]
        self.crossroads[32].neighbours = [self.crossroads[33], self.crossroads[24], None, None]
        self.crossroads[33].neighbours = [self.crossroads[34], self.crossroads[27], self.crossroads[32], None]
        self.crossroads[34].neighbours = [self.crossroads[35], self.crossroads[28], self.crossroads[33], None]
        self.crossroads[35].neighbours = [None, self.crossroads[31], self.crossroads[34], None]
        self.crossroads[36].neighbours = [self.crossroads[14], None, self.crossroads[13], self.crossroads[37]]
        self.crossroads[37].neighbours = [None, self.crossroads[36], None, None]

        self.seeds_roads = [Road(self.crossroads[0], self.crossroads[1]), Road(self.crossroads[1], self.crossroads[2]),
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

        self.player = Player(self.game, 'images/pacman_0.png')
        self.ghosts = [Ghost(self.game, 'Y', 200, self.crossroads[37], 1),
                       Ghost(self.game, 'B', 400, self.crossroads[37], 1),
                       Ghost(self.game, 'P', 800, self.crossroads[37], 1),
                       Ghost(self.game, 'R', 1600, self.crossroads[37], 1)]
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

        self.seeds = self.generate_seeds()
        self.energizers = [Energizer(self.game, 46, 94), Energizer(self.game, 758, 94),
                           Energizer(self.game, self.crossroads[24].x, self.crossroads[24].y),
                           Energizer(self.game, self.crossroads[31].x, self.crossroads[31].y)]

        self.objects = self.seeds + self.energizers + self.walls + self.ghosts + [self.player]

    def process_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.player.rect.x += 5
                Dol = True
                for walls in self.walls:
                    if self.player.check_collision(walls.rect):
                        Dol = False
                        break
                if Dol:
                    self.player.move_right()
                self.player.rect.x -= 5
            elif event.key == pygame.K_a:
                self.player.rect.x -= 5
                Aol = True
                for walls in self.walls:
                    if self.player.check_collision(walls.rect):
                        Aol = False
                        break
                if Aol:
                    self.player.move_left()
                self.player.rect.x += 5
            elif event.key == pygame.K_s:
                self.player.rect.y += 5
                Sol = True
                for walls in self.walls:
                    if self.player.check_collision(walls.rect):
                        Sol = False
                        break
                if Sol:
                    self.player.move_down()
                self.player.rect.y -= 5
            elif event.key == pygame.K_w:
                self.player.rect.y -= 5
                Wol = True
                for walls in self.walls:
                    if self.player.check_collision(walls.rect):
                        Wol = False
                        break
                if Wol:
                    self.player.move_up()
                self.player.rect.y += 5
            elif event.key == pygame.K_p:
                self.game.set_scene(self.game.PAUSE_SCENE_INDEX)

    def on_activate(self) -> None:
        self.create_objects()
        self.start_ticks = pygame.time.get_ticks()

    def time_from_activation(self, start_ticks):
        return (pygame.time.get_ticks() - start_ticks) / 1000

    def check_game_over(self) -> None:
        active_seeds = sum(int(x.stay) for x in self.seeds)
        if self.player.lives.lives == 0:
            self.player.write.write(str(self.player.score) + '\n')
            self.player.write.close()
            self.game.set_scene(self.game.GAMEOVER_SCENE_INDEX)
        elif active_seeds == 0:
            self.player.write.write(str(self.player.score) + '\n')
            self.player.write.close()
            self.game.set_scene(self.game.WIN_SCENE_INDEX)

    def ghosts_logic(self):
        if self.time_from_activation(self.start_ticks) > 3:
            if len(self.walls) == MainScene.INITIAL_WALLS_COUNT:
                del self.walls[0]
                self.objects = self.seeds + self.energizers + self.walls + self.ghosts + [self.player]

            for item in self.ghosts:
                item.move(self.player.is_frightened)

    def check_player_collisions(self):
        for item in self.objects:
            self.player.collides_with(item)

    def additional_logic(self) -> None:
        self.check_game_over()
        self.check_player_collisions()
        self.ghosts_logic()
        if self.player.is_dead:
            self.move_to_spawn()
