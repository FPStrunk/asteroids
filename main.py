import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shots import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock =pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    Asteroid_Field = AsteroidField()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for item in drawable:
            item.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.col_check(shot):
                    asteroid.split()
                    shot.kill()
        for asteroid in asteroids:
            if asteroid.col_check(player):
                print("Game over!")
                sys.exit()
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
