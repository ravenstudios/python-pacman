from constants import *
import pygame
import sprite
import wall
import portal



class Player(sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.speed = 3
        # self.move_vec[0] = self.speed
        # self.move_vec[1] = 0
        self.move_vec = (1, 0)

    def update(self, map):
        self.collision(map)
        self.check_keys()
        self.move(map)

    def move(self, map):
        temp_sprite = pygame.sprite.Sprite()
        temp_vec = self.move_vec * self.speed
        temp_sprite.rect = self.rect.move(temp_vec[0], temp_vec[1])
        # temp_sprite.rect.topl

        collided_objects = pygame.sprite.spritecollide(temp_sprite, map, False)

        if collided_objects:
            for co in collided_objects:
                if self.move_vec[0]:
                    self.rect.right = co.rect.left if self.move_vec[0] > 0 else co.rect.left + co.rect.width * 2

                if self.move_vec[1]:
                    self.rect.bottom = co.rect.top if self.move_vec[1] > 0 else co.rect.top + co.rect.height * 2


        else:
            self.rect.left += self.move_vec[0]
            self.rect.top += self.move_vec[1]


    def collision(self, map):
        collided_objects = pygame.sprite.spritecollide(self, map, False)

        if collided_objects:
            return collided_objects
        return False

                #
                #
                # if type(co) == portal.Portal:
                #     self.rect.left = BLOCK_SIZE if self.move_vec[0] > 0 else GAME_WIDTH - (BLOCK_SIZE * 2)









    def check_keys(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_w] or keys[pygame.K_UP]):
            self.move_vec = (0, -1)

        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
            self.move_vec = (1, 0)

        if (keys[pygame.K_s] or keys[pygame.K_DOWN]):
            self.move_vec = (0, 1)

        if (keys[pygame.K_a] or keys[pygame.K_LEFT]):
            self.move_vec = (-1, 0)
