import pygame
import sys
#custom object for copys of walls
class bckgrnd1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        img = pygame.image.load("invade.png")
        self.image = pygame.transform.scale(img, (1000, 700))
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(0,0))