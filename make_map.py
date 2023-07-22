from constants import *
import pygame
import sprite
import wall
import portal

class Make_Map():
    def __init__(self):
        self.tiles = pygame.sprite.Group()
        self.map_file = "map.txt"
        self.load_map(self.map_file)

    def load_map(self, map_file):
        r, c = 0, 0

        with open(map_file, "r") as file:
            lines = file.readlines()

            for line in lines:
                for letter in line:
                    if letter == ",":
                        continue
                    if letter == "W":
                        self.tiles.add(wall.Wall(c * BLOCK_SIZE, r * BLOCK_SIZE, BLUE))
                    if letter == "p":
                        self.tiles.add(portal.Portal(c * BLOCK_SIZE, r * BLOCK_SIZE, PURPLE))
                    c += 1
                r += 1
                c = 0


    def get_tiles(self):
        return self.tiles
