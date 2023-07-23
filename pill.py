from constants import *
import pygame


class Small_Pill(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((BLOCK_SIZE // 4, BLOCK_SIZE // 4))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = x + BLOCK_SIZE // 2, y + BLOCK_SIZE // 2

class Big_Pill(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
