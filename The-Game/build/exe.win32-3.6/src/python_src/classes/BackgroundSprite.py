#Import librairies
import pygame, png, math, sys
from random import randint

from src.python_src.constants import *

class Class_BackgroundSprite(pygame.sprite.Sprite):

    def __init__(self, image, collidable, x, y, z):

        super(Class_BackgroundSprite, self).__init__()
        self.z = z
        self.opacity = 255
        self.collidable = collidable
        self.position = (x, y)
        size = (640*2,480)
        image_path = constants.PATH_BACK + image + ".png"
        self.rect = pygame.Rect(self.position,size)
        back = pygame.Surface(size).convert_alpha()
        back.fill((0,0,0,0)) 
        self.sheet = pygame.image.load(image_path).convert_alpha()
        back.blit(self.sheet,(0,0))
        back.blit(self.sheet,(640,0))
        self.image = back
        
    def update(self, center):
        return
