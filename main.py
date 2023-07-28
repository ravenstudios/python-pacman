from constants import *
import pygame
import player
import make_map
import ghost


map = make_map.Make_Map()
player = player.Player(BLOCK_SIZE * 5 , BLOCK_SIZE * 15, YELLOW, map)
player_group = pygame.sprite.GroupSingle()
player_group.add(player)




ghost_group = pygame.sprite.Group()
blinky = ghost.Ghost(9 * BLOCK_SIZE, 7 * BLOCK_SIZE, RED, map, player)
ghost_group.add(blinky)


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

    map.get_tiles().draw(surface)
    map.get_pills().draw(surface)

    player_group.draw(surface)
    ghost_group.draw(surface)


    # draw_grid(surface)
    pygame.display.flip()



def update():
    player_group.update(map.get_tiles(), map.get_pills())
    ghost_group.update(player)

def draw_grid(surface):
    col = GAME_WIDTH // BLOCK_SIZE
    row = GAME_HEIGHT // BLOCK_SIZE
    font = pygame.font.Font('freesansbold.ttf', 10)


    for r in range(row):
        for c in range(col):
            pygame.draw.line(surface, RED, (0, r * BLOCK_SIZE), (GAME_WIDTH, r * BLOCK_SIZE))
            pygame.draw.line(surface, RED, (c * BLOCK_SIZE, 0), (c * BLOCK_SIZE, GAME_HEIGHT))
            text = font.render(str((r, c)), True, BLACK, BLUE)
            textRect = text.get_rect()
            textRect.center = (r * BLOCK_SIZE + BLOCK_SIZE // 2, c * BLOCK_SIZE + BLOCK_SIZE // 2)
            surface.blit(text, textRect)
if __name__ == "__main__":
    main()
