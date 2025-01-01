import pygame
from constants import *

def main():
    # initialize pygame
    pygame.init()
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # make the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    # time passed since last drawn frame
    dt = 0

    while True:
        # if quit event occurs exit the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #fill screen with black color represented as r, g, b, a set
        screen.fill([0, 0, 0, 0])
        # refresh screen
        pygame.display.flip()
        # poll time since last drawn frame, divide to conv msec to sec
        dt = clock.tick() / 1000


if __name__ == "__main__":
    main()
