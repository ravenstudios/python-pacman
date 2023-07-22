from constants import *
import pygame
import player

player_group = pygame.sprite.GroupSingle()
player_group.add(player.Player(50, 50, YELLOW))
clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()


def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_r:
                    board.reset()
                if event.key == pygame.K_q:
                    running = False
        draw()
        update()

    pygame.quit()



def draw():
    surface.fill((0, 0, 0))#background
    player_group.draw(surface)
    pygame.display.flip()



def update():
    player_group.update()



if __name__ == "__main__":
    main()