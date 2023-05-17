import pygame
import sys
#custom object for copys of walls
class BouncePhysics(pygame.sprite.Sprite):
    def __init__(self,wallx,wally,w_width,w_height):
        super().__init__() 
        img = pygame.image.load("Bounce wall.png")
        self.image = pygame.transform.scale(img, (w_width,w_height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(wallx,wally))