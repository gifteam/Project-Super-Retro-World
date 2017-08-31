#Import librairies
import pygame, png, math, sys
from random import randint

from src.python_src.constants import *

class Gif_sprite(pygame.sprite.Sprite):
    
    def __init__(self, screen, style):
        super(Gif_sprite, self).__init__()
        self.screen = screen
        self.size = (32, 32)
        self.position = (320 - self.size[0]/2, 240 - self.size[1]/2)
        self.rect = pygame.Rect(self.position, self.size)
        self.sheet = pygame.image.load(constants.PATH_DECO + constants.LOADING_STYLE[style] + ".png").convert_alpha()
        self.nb_sprites_x = self.sheet.get_width() / self.size[0]
        self.index = 0

        self.loading_font = pygame.font.SysFont("Impact", 20)
        self.color = (255,255,255)
        self.run = True

    def get_frame(self, ID):
        spr_x = (ID % self.nb_sprites_x) * self.size[0]
        spr_y = int(ID / self.nb_sprites_x) * self.size[1]
        rect = pygame.Rect((spr_x, spr_y, self.size[0], self.size[1]))
        sprite_surface = pygame.Surface(rect.size).convert_alpha()
        sprite_surface.fill((0,0,0,0))
        sprite_surface.blit(self.sheet,(0,0),rect)  
        return sprite_surface

    def update(self):
        while self.run:
            self.screen.fill((0,0,0))
            self.index += 0.015
            if self.index >= self.nb_sprites_x:
                self.index = 0
            self.image = self.get_frame(int(self.index))
            self.screen.blit(self.image, self.position)
            self.image = self.loading_font.render("Loading...", 1, self.color)
            self.screen.blit(self.image, (self.position[0]-20, self.position[1]+32))
            pygame.display.flip()
