#Import librairies
import pygame, png, math, sys
from random import randint

class Class_FPSSprite(pygame.sprite.Sprite):

    def __init__(self, collidable):

        super(Class_FPSSprite, self).__init__()
        self.z = 999
        self.collidable = collidable
        self.FPS_font = pygame.font.SysFont("impact", 15)
        self.clock = pygame.time.Clock() 
        self.color = (255,255,0)
        self.clock.tick()
        self.image = self.FPS_font.render("FPS = " + str(int(self.clock.get_fps())), 1, self.color)
        self.rect = pygame.Rect((0,0),(128,32))
        
    def update(self, center):
        
        self.clock.tick()
        self.image = self.FPS_font.render("FPS = " + str(int(self.clock.get_fps())), 1, self.color)
