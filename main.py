import pygame
import constants
from player import Player


def main():
    dt = 0
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for updating in updatable:
            updating.update(dt)

        for drawing in drawable:
            drawing.draw(screen)

        # player.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
