from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS,ASTEROID_DEATH_DISPLAY_TIME
from circleshape import CircleShape
import pygame
from logger import log_event
import random



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.is_moving = True
        self.death_time = None  # tracks when asteroid was killed
    
    def draw(self, screen,color="white"):
        if self.is_moving:
            pygame.draw.circle(screen,color,self.position,self.radius,LINE_WIDTH)
        else:
            pygame.draw.circle(screen,"red",self.position,self.radius,LINE_WIDTH)

    def update(self, dt):
        if self.is_moving:
            self.position += self.velocity * dt
        elif self.death_time is not None:
            # asteroid is dead, check if enough time has passed
            self.death_time -= dt
            if self.death_time <= 0:
                self.kill()
    
    def split(self):
        olf_velocity = self.velocity
        self.velocity = pygame.Vector2(0, 0)
        self.is_moving = False
        self.death_time = ASTEROID_DEATH_DISPLAY_TIME  # keep on screen for a few seconds
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        vec1 = olf_velocity.rotate(angle) * 1.2
        vec2 = olf_velocity.rotate(-angle) * 1.2
        a1 = Asteroid(self.position.x,self.position.y,new_radius)
        a2 = Asteroid(self.position.x,self.position.y,new_radius)
        a1.velocity = vec1
        a2.velocity = vec2