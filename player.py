from constants import *
import pygame
import sprite
import wall
import portal



class Player(sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.speed = 3
        self.x_speed = self.speed
        self.y_speed = 0

    def update(self, map):
        self.collision(map)
        self.check_keys()
        self.move(map)

    def move(self, map):
        collided_objects = pygame.sprite.spritecollide(self, map, False)

        if collided_objects:
            for co in collided_objects:
                if self.x_speed:
                    self.rect.right = co.rect.left if self.x_speed > 0 else co.rect.left + co.rect.width * 2
                    self.x_speed = 0
                if self.y_speed:
                    self.rect.bottom = co.rect.top if self.y_speed > 0 else co.rect.top + co.rect.height * 2
                    self.y_speed = 0

        else:
            self.rect.left += self.x_speed
            self.rect.top += self.y_speed


    def collision(self, map):
        collided_objects = pygame.sprite.spritecollide(self, map, False)

        if collided_objects:
            return collided_objects
        return False

                #
                #
                # if type(co) == portal.Portal:
                #     self.rect.left = BLOCK_SIZE if self.x_speed > 0 else GAME_WIDTH - (BLOCK_SIZE * 2)









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
