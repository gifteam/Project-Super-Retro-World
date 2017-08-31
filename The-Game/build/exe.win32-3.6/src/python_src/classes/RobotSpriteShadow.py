#Import librairies
import pygame, png, math, sys
from random import randint

from src.python_src.constants import *

class Class_RobotSpriteShadow(pygame.sprite.Sprite):

    def __init__(self, image, x, y, z, sprite_origin):

        super(Class_RobotSpriteShadow, self).__init__()
        #ORIGINAL
        self.sprite_origin = sprite_origin
        #INFORMATION
        self.index = 0
        self.collidable = False
        self.pos_x, self.pos_y, self.z = x, y, z
        self.index = 0
        self.set_sprite = 0
        self.set_sprite_offset = 0
        position = (self.pos_x, self.pos_y)
        self.size = (self.sprite_origin.size_x, self.sprite_origin.size_y)
        self.rect = pygame.Rect(position,self.size)
        #IMAGE
        self.sheet = pygame.image.load(constants.PATH_CHARA + image + ".png").convert_alpha()
        self.image = self.get_frame(int(self.index))   
        #START!

    def get_frame(self, ID):
        self.spr_x = (ID % self.sprite_origin.nb_sprites_x) * self.sprite_origin.size_x
        sprite_surface = pygame.Surface((self.sprite_origin.size_x,self.sprite_origin.size_y*self.sprite_origin.set_sprite_offset[1])).convert_alpha()
        sprite_surface.fill((0,0,0,0))
        set_sprite = self.sprite_origin.set_sprite + self.sprite_origin.set_sprite_offset[0]
        self.spr_y = set_sprite * self.sprite_origin.size_y
        rect = pygame.Rect(self.spr_x, self.spr_y, self.sprite_origin.size_x,self.sprite_origin.size_y*self.sprite_origin.set_sprite_offset[1])
        sprite_surface.blit(self.sheet,(0,0),rect)
            
        return sprite_surface

        
    def update(self, center):
        return
    
    def update_from_origin(self):
        self.image = self.get_frame(int(self.sprite_origin.index))
        self.rect.top = self.sprite_origin.rect.top - 8
        self.rect.left = self.sprite_origin.rect.left + 8
