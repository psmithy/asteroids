import pygame
from constants import *
from player import Player

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), PLAYER_RADIUS)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        screen.fill([0, 0, 0])

        for i in drawable:
            i.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

  

