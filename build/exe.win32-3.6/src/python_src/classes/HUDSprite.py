#Import librairies
import pygame, png, math, sys
from random import randint

from src.python_src.constants import *

class Class_HUDSprite(pygame.sprite.Sprite):

    def __init__(self):
        super(Class_HUDSprite, self).__init__()
        self.z = 998
        self.collidable = False
        self.index = 0
        self.can_index_change = True
        self.arrow_have_to_rotate = False
        self.rect = pygame.Rect((0,0),(50,50))
        self.image = pygame.Surface((640,480)).convert_alpha()
        self.back_img = pygame.image.load(constants.PATH_HUD + "001" + ".png").convert_alpha()
        self.arrow_img = pygame.image.load(constants.PATH_HUD + "002" + ".png").convert_alpha()

        self.image.fill((0,0,0,0))
        self.image.blit(self.back_img,(0,32))
        self.image.blit(self.arrow_img,(0,32))

        self.color_list = ["", "BLUE", "GREEN", "RED"]
        self.update_color()

    def update_color(self):
        self.color = self.color_list[self.index]
            
    def get_all_keys(self):
        keys = pygame.key.get_pressed()
        self.k_color_none = keys[pygame.K_KP0]
        self.k_color_red = keys[pygame.K_KP1]
        self.k_color_green = keys[pygame.K_KP2]
        self.k_color_blue = keys[pygame.K_KP3]

    def set_frame(self):
        if self.arrow_have_to_rotate:
            angle = 90
            self.arrow_img = self.set_angle(self.arrow_img,angle)
            self.arrow_have_to_rotate = False
            if self.color == "RED":
                self.image.fill((255,0,0,50))
            elif self.color == "GREEN":
                self.image.fill((0,255,0,50))
            elif self.color == "BLUE":
                self.image.fill((0,0,255,50))
            else:
                self.image.fill((0,0,0,0))
            self.image.blit(self.back_img,(0,32))
            self.image.blit(self.arrow_img,(0,32))                 

    def set_angle(self, image, angle):
        loc = image.get_rect().center
        rot_sprite = pygame.transform.rotate(image, angle)
        rot_sprite.get_rect().center = loc
        return rot_sprite

    def update_index(self):
        
        if not self.k_color_none and not self.k_color_red and not self.k_color_green and not self.k_color_blue:
            self.can_index_change = True

        if self.can_index_change:
            if self.k_color_none:
                self.index = 0
            if self.k_color_red:
                self.index = 1
            if self.k_color_green:
                self.index = 2
            if self.k_color_blue:
                self.index = 3
            if self.k_color_none or self.k_color_red or self.k_color_green or self.k_color_blue:
                self.can_index_change = False
                self.arrow_have_to_rotate = True 
        
        if self.k_color_none and not self.k_color_red and not self.k_color_green and not self.k_color_blue and self.index != 0:
            self.index = 0
            self.arrow_have_to_rotate = True
        if self.k_color_red and not self.k_color_none and not self.k_color_green and not self.k_color_blue and self.index != 1:
            self.index = 1
            self.arrow_have_to_rotate = True
        if self.k_color_green and not self.k_color_red and not self.k_color_none and not self.k_color_blue and self.index != 2:
            self.index = 2
            self.arrow_have_to_rotate = True
        if self.k_color_blue and not self.k_color_red and not self.k_color_green and not self.k_color_none and self.index != 3:
            self.index = 3
            self.arrow_have_to_rotate = True
        
    def update(self, center):
        self.get_all_keys()
        self.update_index()
        self.update_color()
        self.set_frame()

        
