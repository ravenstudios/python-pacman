from constants import *
import pygame
import character


class Player(character.Character):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.speed = 5
        self.x_speed = self.speed
        self.y_speed = 0

    def update(self):
        self.check_keys()
        self.rect.left += self.x_speed
        self.rect.top += self.y_speed

    def check_keys(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_w] or keys[pygame.K_UP]):
            self.x_speed = 0
            self.y_speed = -self.speed

        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
            self.x_speed = self.speed
            self.y_speed = 0

        if (keys[pygame.K_s] or keys[pygame.K_DOWN]):
            self.x_speed = 0
            self.y_speed = self.speed

        if (keys[pygame.K_a] or keys[pygame.K_LEFT]):
            self.x_speed = -self.speed
            self.y_speed = 0
