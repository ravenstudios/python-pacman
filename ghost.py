from constants import *
import pygame
from pygame.math import Vector2
import math
import sprite
import wall
import pill



class Ghost(sprite.Sprite):
    def __init__(self, x, y, color, map):
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
        self.smallest_f = []
        self.moveable_locations = []
        self.travled_locatioins = []
    def update(self, player, surface):
        if self.found_player == False:
            self.find_path(player, surface)



    def draw_path(self, surface):
        for trav in self.travled:
            # print(trav)
            x = trav["loc"][0]
            y = trav["loc"][1]
            pygame.draw.rect(surface, WHITE, (x, y, BLOCK_SIZE, BLOCK_SIZE))



    def find_path(self, player, surface):

        self.travled = []
        self.smallest_f = []
        self.path = []

        px, py = player.get_grid_location()
        mx, my = self.rect.x // BLOCK_SIZE, self.rect.y // BLOCK_SIZE

        self.get_neighbor((mx, my), (px, py))
        # print(f"self.moveable_locations len :{self.moveable_locations}")
        # print(self.moveable_locations)
        # print(self.moveable_locations)
        count = 0
        while self.found_player == False:
            # breakpoint()
            print(f"count:{count}")
            count += 1
            current_loc = min(self.moveable_locations, key=lambda  d:d['f'])
            self.travled.append(current_loc)
            if  current_loc["loc"] == (px, py):
                        print("found Player!!!!!")
                        self.found_player = True
                        self.get_path()
                        return

            # print(f"mo len before{len(self.moveable_locations)}")
            self.get_neighbor(current_loc["loc"], (py, px))
            # print(f"mo len after{len(self.moveable_locations)}")
            # self.travled.append(current_loc)
            self.moveable_locations.remove(current_loc)




    def get_neighbor(self, g_loc, p_loc):

        self.travled_locatioins.append(g_loc)
        # print(f"g_loc:{g_loc}")
        wall_locations = self.map.get_map_list()
        temp = []
        mx, my = self.rect.x // BLOCK_SIZE, self.rect.y // BLOCK_SIZE
        dirs = [(g_loc[0], g_loc[1] - 1), (g_loc[0] + 1, g_loc[1]), (g_loc[0], g_loc[1] + 1), (g_loc[0] - 1, g_loc[1])]
        for dir in dirs:
            try:
                if wall_locations[dir[1]][dir[0]] != "#" and dir not in self.travled_locatioins:
                    # print(f"dir({dir[0], dir[1]}) is not a wall::::  {wall_locations[dir[1]][dir[0]]} ")
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
                    # print(f"obj:{obj}")
                    # for ml in self.moveable_locations:
                    #     print(f"dir:{dir}  loc:{obj['loc']}")
                    #     if dir == ml["loc"]:
                    #         if obj["f"] > f:
                    #             print("obj updated")
                    #             ml["g"] = g
                    #             ml["h"] = h
                    #             ml["f"] = f
                    #     continue

                    self.moveable_locations.append(obj)
            except Exception as e:
                print(f"e:{e}")
        # print(temp, "\n\n\n")
        return temp


    def get_path(self):

        print("!!!!!!!!!!!!!PATH!!!!!!!!!!!!!!")
        print(self.travled[-1])
        mx, my = self.rect.x // BLOCK_SIZE, self.rect.y // BLOCK_SIZE
        path_complete = False
        self.travled.reverse()
        result = [self.travled[0]]
        while not path_complete:
            result.append(self.travled[self.travled.index()]result[0]["came_from"])





    def move(self):

        if self.rect.right > self.cols * BLOCK_SIZE and self.move_vec[0] > 0:
            self.rect.left = 0

        elif self.rect.left < self.start_offset and self.move_vec[0] < 0:
            self.rect.left = self.cols * BLOCK_SIZE



        temp_sprite = pygame.sprite.Sprite()
        temp_vec = self.move_vec * self.speed
        temp_sprite.rect = self.rect.move(temp_vec[0], temp_vec[1])

        collided_objects = pygame.sprite.spritecollide(temp_sprite, self.map.get_tiles(), False)


        if collided_objects:
            for co in collided_objects:
                if self.move_vec[0]:
                    self.rect.right = co.rect.left if self.move_vec[0] > 0 else co.rect.left + co.rect.width * 2

                if self.move_vec[1]:
                    self.rect.bottom = co.rect.top if self.move_vec[1] > 0 else co.rect.top + co.rect.height * 2


        else:
            self.rect.left += self.move_vec[0] * self.speed
            self.rect.top += self.move_vec[1] * self.speed


    def collision(self, map):
        collided_objects = pygame.sprite.spritecollide(self, map, False)
        return collided_objects if collided_objects else False
