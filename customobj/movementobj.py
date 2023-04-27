import pygame 
import sys
#custom object for copys of walls 
class Move_Object(pygame.sprite.Sprite):
    def _init_(self, startx, startY ,width, height, load_path):
        super()._init_()
        img_load = pygame. image.load(load_path)
        self.image = pygame.transform.scale(img_load, (width, height)).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startx, startY))
    
    def key_press(self,speed):
        key_input = pygame.key.get_pressed()
        self.movex = (key_input [pygame.K_LEFT] * -speed) + (key_input[pygame.K_RIGHT] * speed)
        self.movey = (key_input [pygame.K_UP] * -speed) + (key_input[pygame.K_DOWN] * speed)
        #x-location + x-speed = new x-location
        self.rect.x += self.movex
        #y-location + y-speed = new y-location
        self.rect.y += self.movey
