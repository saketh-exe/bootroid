from typing import Any

import pygame



class Score(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # we will be using this later
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.value = 0
        self.font = pygame.font.Font(None, 36)  # None uses default font, 36 is size

    def draw(self, screen):
        # Draw a rectangle at the position with width and height
        rect = pygame.draw.rect(screen, "white", (self.position.x, self.position.y, 100, 50))
        
        # Render text
        text_surface = self.font.render(f"Score: {self.value}", True, "black")
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)
        
    
 
