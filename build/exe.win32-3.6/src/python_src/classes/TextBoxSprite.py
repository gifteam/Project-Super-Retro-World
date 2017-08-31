import pygame, math
from src.python_src.constants import *

class TextBox_sprite(pygame.sprite.Sprite):
    
    def __init__(self, txt, target):
        super(TextBox_sprite, self).__init__()
        self.z = 999
        self.target = target
        self.size = ((len(txt)+2)*8, 13*3 - 6)
        self.collidable = False
        self.txt = txt
        self.index = 0
        self.index_max = len(self.txt)
        self.txt_speed = constants.TXTBOX_SPEED
        self.last_char_frame = 0
        self.font = pygame.font.SysFont("Consolas", 15)
        self.font_color = (255,255,255)
        self.back_color = (0,0,0)
        self.image = self.get_frame(int(self.index))
        self.run = True
        self.k_return_pressed = False
        self.txt_box_can_close = False
        
    def get_frame(self, index):
        self.position = (int(320 - (self.size[0] - constants.SPRITE_X)/2) , self.target.rect.top - 48)
        self.rect = pygame.Rect(self.position, self.size)
        if self.index <= self.index_max:
            self.txt_render = self.get_txt_to_render(index)
        surf = pygame.Surface(self.size)
        surf.fill((0,0,0,255))
        surf.blit(self.font.render(self.txt_render, 1, self.font_color), (8,10))
        return surf

    def clean_txt_box(self):
        surf = pygame.Surface((0,0))
        return surf

    def get_all_keys(self):
        keys = pygame.key.get_pressed()
        self.k_return_pressed = keys[pygame.K_RETURN]

    def get_txt_to_render(self, index):
        txt = ""
        for i in range(index):
            txt += self.txt[i]
        return txt

    def update(self, center):
        if self.run:
            self.get_all_keys()
            self.index = min(self.index + self.txt_speed / 25, self.index_max)
            self.image = self.get_frame(int(self.index))
            if self.index == self.index_max:
                self.last_char_frame += self.txt_speed / 25
                if self.last_char_frame >= 4:
                    self.last_char_frame = 0
                    self.index -= 1
            if not self.k_return_pressed and self.index >= self.index_max-1 and not self.txt_box_can_close:
                self.txt_box_can_close = True
            if self.k_return_pressed:
                if self.index < self.index_max:
                    self.index = self.index_max
                elif self.txt_box_can_close:
                    self.image = self.clean_txt_box()
                    self.run = False







        
