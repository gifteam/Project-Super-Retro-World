#Import librairies
import pygame, png, math, sys
from random import randint

from src.python_src.constants import *

class Class_EffectSprite(pygame.sprite.Sprite):

    def __init__(self):

        super(Class_EffectSprite, self).__init__()
        self.z = 1
        self.size = (32, 32)
        self.pos_x, self.pos_y = 320, 240
        self.collidable = False
        self.position = (self.pos_x, self.pos_y)
        self.rect = pygame.Rect(self.position, self.size)
        self.sheet = pygame.image.load(constants.PATH_CHARA + "jump_effects" + ".png").convert_alpha()
        self.nb_sprites_x = self.sheet.get_width() / self.size[0]
        self.index = self.nb_sprites_x
        self.type = 1
        self.image = self.get_frame(int(self.index))


    def get_frame(self, ID):
        self.spr_x = (ID % self.nb_sprites_x) * self.size[0]
        if self.type == 1:
            self.spr_y = 0 * self.size[1]
        else:
            self.spr_y = 1 * self.size[1]
        rect = pygame.Rect((self.spr_x, self.spr_y, self.size[0], self.size[1]))
        sprite_surface = pygame.Surface(rect.size).convert_alpha()
        sprite_surface.fill((0,0,0,0))
        sprite_surface.blit(self.sheet,(0,0),rect)  
        return sprite_surface
        
    def update(self, center):
        self.index += 0.5
        if self.index <= self.nb_sprites_x - 1:
            self.image = self.get_frame(int(self.index))
        else:
            self.image.fill((0,0,0,0))
