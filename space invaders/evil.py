from typing import Any
import pygame
import sys
#custom object for copys of walls
class enemyshot(pygame.sprite.Sprite):
    def __init__(self,bad_x,bad_y):
        super().__init__() 
        img = pygame.image.load("Bullet.png")
        self.image = pygame.transform.scale(img, (10,30)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(bad_x,bad_y))
        
    def update(self):
        self.rect.y+=15
        if self.rect.y >700:
            self.kill()
    