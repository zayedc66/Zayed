from typing import Any
import pygame
import sys
#custom object for copys of walls
class bullet(pygame.sprite.Sprite):
    def __init__(self,bulletx,bullety):
        super().__init__() 
        img = pygame.image.load("Bullet.png")
        self.image = pygame.transform.scale(img, (10,30)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(bulletx,bullety))
        
    def update(self):
        self.rect.y-=15
        if self.rect.y <0:
            self.kill()