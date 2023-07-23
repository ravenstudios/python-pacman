from constants import *
import pygame
import player
import make_map

player = player.Player(BLOCK_SIZE , BLOCK_SIZE * 2, YELLOW)
player_group = pygame.sprite.GroupSingle()
map = make_map.Make_Map(player)


player_group.add(player)
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
    map.get_tiles().draw(surface)
    map.get_pills().draw(surface)
    pygame.display.flip()



def update():
    player_group.update(map.get_tiles(), map.get_pills())



if __name__ == "__main__":
    main()
