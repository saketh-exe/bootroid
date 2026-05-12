from constants import SCREEN_WIDTH,SCREEN_HEIGHT
import pygame
from logger import log_state ,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from score import Score
from shot import Shot
import sys
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    field = AsteroidField()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    score = Score(SCREEN_WIDTH//2,10)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        score.draw(screen)
        for elem in drawable:
            elem.draw(screen)
        for asteroid in asteroids:
            if asteroid.collides_with(player) and asteroid.is_moving:
                log_event("player_hit")
                print("Game over!")
                print(f"score is {score.value}")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot) and asteroid.is_moving:
                    score.value += 1
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()



        pygame.display.flip()
        delta = clock.tick(60)
        dt = delta/1000
        
if __name__ == "__main__":
    main()

