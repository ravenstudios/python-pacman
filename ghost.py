from constants import *
import pygame
from pygame.math import Vector2
import math
import sprite
import wall
import pill



class Ghost(sprite.Sprite):
    def __init__(self, x, y, color, map, player):
        super().__init__(x, y, color)
        self.speed = 5
        self.gn = 0
        # self.move_vec[0] = self.speed
        # self.move_vec[1] = 0
        self.move_vec = (1, 0)
        self.start_offset = 0
        self.score = 0

        self.map = map
        self.cols = map.get_cols()
        self.rows = map.get_rows()

        self.found_player = False
        self.path = []
        self.travled = []


        self.moveable_locations = []
        self.travled_locatioins = []


    def update(self, player):
        # breakpoint()
        print(f"vec:{self.move_vec}")
        if self.found_player == False:
            self.find_path(player)
        self.move(player)




    def find_path(self, player):
        print("find path")
        self.travled = [
            {
                       "g":0,
                       "h":abs(self.rect.x // BLOCK_SIZE - player.rect.x // BLOCK_SIZE) + abs(self.rect.y // BLOCK_SIZE - player.rect.y // BLOCK_SIZE),
                       "f":abs(self.rect.x // BLOCK_SIZE - player.rect.x // BLOCK_SIZE) + abs(self.rect.y // BLOCK_SIZE - player.rect.y // BLOCK_SIZE),
                       "loc": (self.rect.x // BLOCK_SIZE, self.rect.y // BLOCK_SIZE),
                       "came_from": (self.rect.x // BLOCK_SIZE, self.rect.y // BLOCK_SIZE)
                       }
        ]

        # self.path = []
        print(f"travled[0] in findpath:{self.travled[0]}")
        px, py = player.get_grid_location()
        mx, my = self.rect.x // BLOCK_SIZE, self.rect.y // BLOCK_SIZE

        self.get_neighbor((mx, my), (px, py))






        while self.found_player == False:

            current_loc = min(self.moveable_locations, key=lambda  d:d['f'])
            self.travled.append(current_loc)
            if  current_loc["loc"] == (px, py):
                        print("found Player!!!!!")
                        self.found_player = True
                        self.get_path()
                        return

            self.get_neighbor(current_loc["loc"], (py, px))
            self.moveable_locations.remove(current_loc)




    def get_neighbor(self, g_loc, p_loc):

        self.travled_locatioins.append(g_loc)
        wall_locations = self.map.get_map_list()
        temp = []
        mx, my = self.rect.x // BLOCK_SIZE, self.rect.y // BLOCK_SIZE
        dirs = [(g_loc[0], g_loc[1] - 1), (g_loc[0] + 1, g_loc[1]), (g_loc[0], g_loc[1] + 1), (g_loc[0] - 1, g_loc[1])]
        for dir in dirs:
            try:
                if wall_locations[dir[1]][dir[0]] != "#" and dir not in self.travled_locatioins:
                    g = abs(mx - dir[0]) + abs(my - dir[1])
                    h = abs(dir[0] - p_loc[0]) + abs(dir[1] - p_loc[1])
                    f = g + h
                    obj = {
                               "g":g,
                               "h":h,
                               "f":f,
                               "loc": dir,
                               "came_from": g_loc
                               }
                    self.moveable_locations.append(obj)
            except Exception as e:
                print(f"e:{e}")
        # print(temp, "\n\n\n")
        return temp


    def get_path(self):
        print(f"GET PATH!!!!!!!!!!!!!!!!!!!!")
        print(f"len of travled in get path:{len(self.travled)}")
        mx, my = self.rect.x // BLOCK_SIZE, self.rect.y // BLOCK_SIZE

        path_not_complete = True


        current = self.travled[-1]
        came_from = current["came_from"]
        self.path = []
        # print(f"self.travled:{self.travled}")

        while path_not_complete:
            for i in range(len(self.travled)):
                if current["loc"] == (mx, my):
                    print("DONE!!!!!")
                    self.path.append(current["loc"])
                    self.path.reverse()
                    path_not_complete = False
                    # self.found_player = False
                    print(self.path, "\n")
                    return
                if self.travled[i]["loc"] == came_from:
                    self.path.append(current["loc"])
                    current = self.travled[i]
                    came_from = current["came_from"]
                    # print(f"came_from:{came_from}")
                    # print(f"loc:{current['loc']} mx, my:{(mx, my)}")










    def move(self, player):

        if self.path:
            # breakpoint()
            current = self.path[0]
            mx, my = self.rect.x // BLOCK_SIZE, self.rect.y // BLOCK_SIZE
            if mx == current[0] and my == current[1]:
                print("POPPOPOPOPOPOPOPOPO")
                self.path.pop(0)
                if len(self.path) <= 0:
                # self.found_player = False
                    self.find_path(player)

            if mx < current[0]:
                self.move_vec = (1, 0)
            elif my < current[1]:
                self.move_vec = (0, 1)
            elif mx > current[0]:
                self.move_vec = (-1, 0)
            elif my > current[1]:
                self.move_vec = (0, -1)

            self.rect.left += self.move_vec[0] * self.speed
            self.rect.top += self.move_vec[1] * self.speed

        # if self.rect.right > self.cols * BLOCK_SIZE and self.move_vec[0] > 0:
        #     self.rect.left = 0
        #
        # elif self.rect.left < self.start_offset and self.move_vec[0] < 0:
        #     self.rect.left = self.cols * BLOCK_SIZE
        #
        #
        #
        # temp_sprite = pygame.sprite.Sprite()
        # temp_vec = self.move_vec * self.speed
        # temp_sprite.rect = self.rect.move(temp_vec[0], temp_vec[1])
        #
        # collided_objects = pygame.sprite.spritecollide(temp_sprite, self.map.get_tiles(), False)
        #
        #
        # if collided_objects:
        #     for co in collided_objects:
        #         if self.move_vec[0]:
        #             self.rect.right = co.rect.left if self.move_vec[0] > 0 else co.rect.left + co.rect.width * 2
        #
        #         if self.move_vec[1]:
        #             self.rect.bottom = co.rect.top if self.move_vec[1] > 0 else co.rect.top + co.rect.height * 2


        # else:



    def collision(self, map):
        collided_objects = pygame.sprite.spritecollide(self, map, False)
        return collided_objects if collided_objects else False
