from constants import *
import pygame
import sprite


class Portal(sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
