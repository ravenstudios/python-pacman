from constants import *
import pygame
import sprite
import wall
import portal



class Player(sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.speed = 5

        # self.move_vec[0] = self.speed
        # self.move_vec[1] = 0
        self.move_vec = (1, 0)
        self.start_offset = 0
        self.cols = 33



    def update(self, map):
        self.collision(map)
        self.check_keys(map)
        self.move(map)

    def move(self, map):

        if self.rect.right > self.cols * BLOCK_SIZE and self.move_vec[0] > 0:
            self.rect.left = 0

        elif self.rect.left < self.start_offset and self.move_vec[0] < 0:
            self.rect.left = self.cols * BLOCK_SIZE



        temp_sprite = pygame.sprite.Sprite()
        temp_vec = self.move_vec * self.speed
        temp_sprite.rect = self.rect.move(temp_vec[0], temp_vec[1])

        collided_objects = pygame.sprite.spritecollide(temp_sprite, map, False)

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








    def check_keys(self, map):
        keys = pygame.key.get_pressed()
        temp_sprite = pygame.sprite.Sprite()

        if (keys[pygame.K_w] or keys[pygame.K_UP]):
            temp_vec = (0, -1) * self.speed
            temp_sprite.rect = self.rect.move(temp_vec[0], temp_vec[1])
            if not pygame.sprite.spritecollide(temp_sprite, map, False):
                self.move_vec = (0, -1)

        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
            temp_vec = (1, 0) * self.speed
            temp_sprite.rect = self.rect.move(temp_vec[0], temp_vec[1])
            if not pygame.sprite.spritecollide(temp_sprite, map, False):
                self.move_vec = (1, 0)

        if (keys[pygame.K_s] or keys[pygame.K_DOWN]):
            temp_vec = (0, 1) * self.speed
            temp_sprite.rect = self.rect.move(temp_vec[0], temp_vec[1])
            if not pygame.sprite.spritecollide(temp_sprite, map, False):
                self.move_vec = (0, 1)

        if (keys[pygame.K_a] or keys[pygame.K_LEFT]):
            temp_vec = (-1, 0) * self.speed
            temp_sprite.rect = self.rect.move(temp_vec[0], temp_vec[1])
            if not pygame.sprite.spritecollide(temp_sprite, map, False):
                self.move_vec = (-1, 0)
