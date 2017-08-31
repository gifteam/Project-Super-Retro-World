#Import librairies
import pygame, png, math, sys
from random import randint

from src.python_src.constants import *

class Class_FrontgroundSprite(pygame.sprite.Sprite):

    def __init__(self, image, collidable, z):

        super(Class_FrontgroundSprite, self).__init__()
        self.z = z
        self.collidable = collidable
        image_path = constants.PATH_FRONT + image + ".png"
        self.sheet = pygame.image.load(image_path).convert_alpha()
        self.index = 0
        self.id = image
        self.set_param_from_ID()
        self.rect = pygame.Rect(self.position,self.size)
        self.nb_sprites_x = self.sheet.get_width() / self.size_x
        self.image = self.get_frame(int(self.index))

    def set_param_from_ID(self):
        self.position = (0,0)
        self.size_x = 0
        self.size_y = 0
        self.size = (self.size_x,self.size_y)
        if self.id == "001":
            self.position = (0,480-120)
            self.size_x = 160
            self.size_y = 120
            self.size = (self.size_x,self.size_y)

    def get_frame(self, index):
        x = (index % self.nb_sprites_x) * self.size_x
        y = int(index / self.nb_sprites_x) * self.size_y
        rect = pygame.Rect(x, y,self.rect.width,self.rect.height)
        frontground_surface = pygame.Surface(rect.size, pygame.SRCALPHA, 32).convert_alpha()
        frontground_surface.fill((0,0,0,0))
        frontground_surface.blit(self.sheet,(0,0),rect)
        return frontground_surface
        
    def update(self, center):
        self.index += 1
        if self.index > 3:
            self.index = 0
        self.image = self.get_frame(int(self.index))
