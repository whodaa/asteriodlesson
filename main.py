import pygame
from constants import *

run_game_loop = True

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    frameclock = pygame.time.Clock() 


    while run_game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, (0,0,0))
        
        
        pygame.display.flip()
        dt = safe_divide(frameclock.tick(60), 1000)

def safe_divide(dividend, divisor):
    if dividend == 0 or divisor == 0:
        return 0
    else:
        return dividend / divisor


if __name__ == "__main__":
    main()