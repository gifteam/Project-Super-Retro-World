#Import librairies
import pygame, png, math, sys
from random import randint

from src.python_src.constants import *

class Class_AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, image, x, y, size_x, size_y, collidable, z):

        super(Class_AnimatedSprite, self).__init__()
        self.z = z
        self.size_x, self.size_y = size_x, size_y
        self.pos_x, self.pos_y = x, y
        self.collidable = collidable
        position = (self.pos_x, self.pos_y)
        size = (self.size_x, self.size_y)
        self.rect = pygame.Rect(position,size)
        self.sheet = pygame.image.load(constants.PATH_DECO + image + ".png").convert_alpha()
        self.nb_sprites_x = self.sheet.get_width() / size_x
        self.index = 0
        self.appearance_id = 4 #randint(0,self.sheet.get_height()/constants.SPRITE_X)
        self.image = self.get_frame(self.index)

    def get_frame(self, ID):
        self.spr_x = (ID % self.nb_sprites_x) * self.size_x
        self.spr_y = self.appearance_id * self.size_y
        rect = pygame.Rect((self.spr_x, self.spr_y, self.size_x, self.size_y))
        sprite_surface = pygame.Surface(rect.size).convert_alpha()
        sprite_surface.fill((0,0,0,0))
        sprite_surface.blit(self.sheet,(0,0),rect)  
        return sprite_surface
        
    def update(self, center):
        
        self.index += 0.05
        if self.index >= self.nb_sprites_x:
            self.index = 0
        self.image = self.get_frame(int(self.index))
