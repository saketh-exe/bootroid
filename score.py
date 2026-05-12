from typing import Any

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT



class Score(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # we will be using this later
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.value = 0
        self.font = pygame.font.Font(None, 22)  # None uses default font, 36 is size

    def draw(self, screen):
        # Rectangle dimensions
        rect_width, rect_height = 100, 50
        # Center the rectangle on screen
        rect_x = (SCREEN_WIDTH - rect_width) // 2
        rect_y = (SCREEN_HEIGHT - rect_height) // 2
        
        rect = pygame.draw.rect(screen, "white", (rect_x, 0, rect_width, rect_height))
        
        # Render text centered on the rectangle
        text_surface = self.font.render(f"Score: {self.value}", True, "black")
        text_rect = text_surface.get_rect(center=(rect_x + rect_width // 2, 0 + rect_height // 2))
        screen.blit(text_surface, text_rect)
        
    
 
