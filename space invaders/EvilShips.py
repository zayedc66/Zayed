import pygame
import sys
#custom object for copys of walls
class BadShips(pygame.sprite.Sprite):
    #move_space=2
    def __init__(self,ship_x,ship_y,row):
        super().__init__() 
        img = pygame.image.load("shipKSP.png")
        self.image = pygame.transform.scale(img, (60,30)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(ship_x,ship_y))
        self.row=row
    def update(self,move_space,current_y,stage):
        self.rect.x+=(move_space+stage)
        if self.rect.y <= (15+current_y+(40*(self.row-1))):
            self.rect.y+=1