from constants import *
import pygame
import sprite
import wall
import pill

class Make_Map():
    def __init__(self):
        self.tiles = pygame.sprite.Group()
        self.pills = pygame.sprite.Group()
        self.map_file = "map.txt"
        self.rows = 0
        self.cols = 0
        self.map_list = []
        self.load_map(self.map_file)


    def load_map(self, map_file):
        r, c = 0, 0

        with open(map_file, "r") as file:
            lines = file.readlines()

            for line in lines:
                line_list = []
                for letter in line:
                    if letter != "\n":
                        line_list.append(letter)
                    if letter == ",":
                        continue
                    if letter == "#":
                        self.tiles.add(wall.Wall(c * BLOCK_SIZE, r * BLOCK_SIZE, BLUE))
                    if letter == ".":
                        self.pills.add(pill.Small_Pill(c * BLOCK_SIZE, r * BLOCK_SIZE, WHITE))
                    if letter == "o":
                        self.pills.add(pill.Big_Pill(c * BLOCK_SIZE, r * BLOCK_SIZE, WHITE))

                    c += 1
                    self.cols += 1
                self.map_list.append(line_list)
                r += 1
                self.rows += 1
                c = 0

        # for i in range(len(self.map_list)):
        #     for j in range(len(self.map_list[i])):
        #         print(f"map[{i}][{j}] {self.map_list[i][j]}")

    def get_map_list(self):
        return self.map_list


    def get_rows(self):
        return self.rows


    def get_cols(self):
        return self.cols / self.rows


    def get_tiles(self):
        return self.tiles


    def get_pills(self):
        return self.pills
