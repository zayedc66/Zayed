import pygame
import sys
#custom object for copys of walls
class move(pygame.sprite.Sprite):
    def __init__(self,startx,starty):
        super().__init__() 
        img = pygame.image.load("Kerbalman.png")
        self.image = pygame.transform.scale(img, (100,120)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startx,starty))
    def moveguy(self,startx,starty,gamestart):
        key_input = pygame.key.get_pressed()
        if gamestart == 1:
            if key_input[pygame.K_a]: 
                self.x = -8
            elif key_input[pygame.K_d]: 
                self.x = 8            
            else:
                self.x = 0           
            self.rect.x+=self.x  