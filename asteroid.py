from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import pygame
from logger import log_event
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        vec1 = self.velocity.rotate(angle) * 1.2
        vec2 = self.velocity.rotate(-angle) * 1.2
        a1 = Asteroid(self.position.x,self.position.y,new_radius)
        a2 = Asteroid(self.position.x,self.position.y,new_radius)
        a1.velocity = vec1
        a2.velocity = vec2