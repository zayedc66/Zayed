import pygame
import sys
#custom object for copys of walls
class back2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        img = pygame.image.load("kerbalinvaders.png")
        self.image = pygame.transform.scale(img, (507,196))
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(0,0))