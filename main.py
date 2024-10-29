import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initializing the pygame function to variable "screen"
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Creating a Clock object to handle FPS functionality
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Infinite game loop that kills the program when the user has closed the window.
    i = 0
    while i == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()

        # Restricts the game to draw a maximum of 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()