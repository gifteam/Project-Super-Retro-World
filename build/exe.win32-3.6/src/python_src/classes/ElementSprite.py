#Import librairies
import pygame, png, math, sys
from random import randint

from src.python_src.constants import *

class Class_ElementSprite(pygame.sprite.Sprite):

    def __init__(self, style, tile_style, x, y, el_type, size_x, size_y, collidable, z, filter_sprite, top_sprite):

        super(Class_ElementSprite, self).__init__()
        self.z = z
        self.size_x, self.size_y = size_x, size_y
        self.pos_x, self.pos_y = x, y
        self.collidable = collidable
        self.collidable_origin = collidable
        position = (self.pos_x, self.pos_y)
        size = (self.size_x, self.size_y)
        self.rect = pygame.Rect(position,size)
        self.sheet = pygame.image.load(constants.PATH_TILE + tile_style + "_element_" + style + ".png").convert_alpha()
        self.nb_sprites_x = self.sheet.get_width() / size_x
        self.offset = 0
        self.index = 0
        self.top_sprite = top_sprite
        self.filter = filter_sprite
        self.el_type = el_type
        if el_type[0] == 255:
            self.index = 0
            self.color = "RED"
        if el_type[1] == 255:
            self.index = 1
            self.color = "GREEN"
        if el_type[2] == 255:
            self.index = 2
            self.color = "BLUE"
        self.activation()
        if self.activated:
            self.spr_x = (self.index % self.nb_sprites_x) * self.size_x
        else:
            self.spr_x = (self.nb_sprites_x - 1) * self.size_x
        self.spr_y = self.size_y + self.top_sprite*self.size_y
        rect = pygame.Rect((self.spr_x, self.spr_y, self.size_x, self.size_y))
        self.image = pygame.Surface(rect.size).convert_alpha()
        self.set_frame(self.index)

    def set_frame(self, ID):
        if self.activated:
            self.spr_x = (ID % self.nb_sprites_x) * self.size_x
        else:
            self.spr_x = (self.nb_sprites_x - 1) * self.size_x
        self.spr_y = self.size_y + self.top_sprite*self.size_y
        rect = pygame.Rect((self.spr_x, self.spr_y, self.size_x, self.size_y))
        self.image.fill((0,0,0,0))
        self.image.blit(self.sheet,(0,0),rect)

    def desactivation(self):
        self.activated = False
        self.collidable = False

    def activation(self):
        self.activated = True
        self.collidable = self.collidable_origin
  
    def update(self, center):
        if self.filter.color != self.color:
            if self.activated:
                self.desactivation()
                self.set_frame(self.index)
        elif not self.activated:
            self.activation()
            self.set_frame(self.index)
        
