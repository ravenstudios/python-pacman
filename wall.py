from constants import *
import pygame
import sprite


class Wall(sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        
