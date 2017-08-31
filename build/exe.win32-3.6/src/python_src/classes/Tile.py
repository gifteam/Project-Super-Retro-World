#Import librairies
import pygame, png, math, sys
from random import randint

from src.python_src.constants import *

class Class_Tile(pygame.sprite.Sprite):

    def __init__(self,image, size_x, size_y, ID, display_x, display_y, shadow = False):
        
        super(Class_Tile, self).__init__()
        if shadow:
            self.z = -100
        else:
            self.z = self.define_z_from_ID(ID)
        self.sheet = pygame.image.load(constants.PATH_TILE + image + ".png").convert_alpha()
        self.id = ID
        self.tile_x = size_x
        self.tile_y = size_y
        self.origin_left = display_x
        self.nb_tiles_x = self.sheet.get_width() / size_x
        self.pos_x = (ID % self.nb_tiles_x) * size_x
        self.pos_y = int(ID / self.nb_tiles_x) * size_y
        self.rect = pygame.Rect((display_x, display_y, size_x, size_y))
        self.image = self.get_surface()
        if shadow:
            self.collidable = False
        else:
            self.collidable = self.define_collidable()

    def define_z_from_ID(self, ID):
        if (ID >=0 and ID <= 3) or (ID >= 16 and ID <= 19):
            return -75
        elif (ID >=4 and ID <= 15) or (ID >= 20 and ID <= 31):
            return 75
        
    def define_collidable(self):
        if (self.id >=4 and self.id <= 15) or (self.id >=20 and self.id <= 23):
            return True
        else:
            return False
        
    def get_surface(self):
        rect = pygame.Rect((self.pos_x, self.pos_y, self.tile_x, self.tile_y))
        tile_surface = pygame.Surface(rect.size).convert_alpha()
        tile_surface.fill((0,0,0,0))
        tile_surface.blit(self.sheet, (0,0), rect)
        return tile_surface
        
    def update(self, center):
        return
