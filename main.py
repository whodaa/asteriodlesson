import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

run_game_loop = True
#updateable = pygame.sprite.Group()
#drawable = pygame.sprite.Group()
#asteroids = pygame.sprite.Group()

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()


    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    frameclock = pygame.time.Clock() 
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()

    

    while run_game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, (0,0,0))

        # update and draw per tick
        for upd in updateable:
            upd.update(dt)

        for ast in asteroids:
            if player.check_collision(ast):
                print("Game over!")
                exit()
            for sh in shots:
                if ast.check_collision(sh):
                    ast.split()
                    sh.kill()
        
        for drw in drawable:
            drw.draw(screen)
        
        
        pygame.display.flip()
        dt = safe_divide(frameclock.tick(60), 1000)

def safe_divide(dividend, divisor):
    if dividend == 0 or divisor == 0:
        return 0
    else:
        return dividend / divisor


if __name__ == "__main__":
    main()