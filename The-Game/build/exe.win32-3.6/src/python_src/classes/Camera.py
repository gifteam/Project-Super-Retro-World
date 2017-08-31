import pygame, math
from src.python_src.constants import *
from src.python_src.classes import Lighting

class Camera_object(object):
    
    def __init__(self, target, mapping_light_scr, map_size, style):
        self.target = target
        self.camera_x = 0
        self.camera_y = 0
        self.light_effect_activated = False
        if constants.LIGHT_SOURCE[style][0] == 0:
            self.light_effect_activated = False
        if constants.LIGHT_SOURCE[style][0] == 1:
            self.light_effect_activated = True
        if constants.LIGHT_SOURCE[style][0] == 2:
            self.light_effect_activated = True
        self.light_effect = Lighting.Lighting_object(mapping_light_scr, map_size, self.camera_x, self.camera_y, style)
        
    def draw_all_sprites_list(self, my_list, screen):
        self.camera_x = self.target.rect.left - constants.SCREEN_X/2
        self.camera_y = 0
        self.robot_y = self.target.rect.top
        #go through all sprites       
        for sprite in my_list:
            #draw only those around the camera target
            if self.is_in_screen(sprite) and not self.is_front_or_background(sprite):
                screen.blit(sprite.image, (sprite.rect.left - self.camera_x, sprite.rect.top - self.camera_y))    
            if self.is_background(sprite): 
                screen.blit(sprite.image, (sprite.rect.left - self.target.rect.left/(abs(sprite.z)/10), sprite.rect.top))
            elif self.is_frontground(sprite):
                screen.blit(sprite.image,sprite.rect)
        #Draw lights sources
        if self.light_effect.light_effect_activated:
            self.light_effect.move_light_effect(screen, self.camera_x, self.robot_y)

    def is_in_screen(self, sprite):
        if (abs(sprite.rect.left - self.target.rect.left) <= constants.SCREEN_X/2 + constants.SPRITE_X):
            if (abs(sprite.rect.top - self.target.rect.top) <= constants.SCREEN_Y * 2):
                return True
        else:
            return False

    def is_frontground(self, sprite):
        if sprite.z >= 101:
            return True
        else:
            return False

    def is_background(self, sprite):
        if sprite.z <= -101:
            return True
        else:
            return False

    def is_front_or_background(self, sprite):
        if sprite.z >= 101 or sprite.z <= -101:
            return True
        else:
            return False
        
    def clear_all_sprites_list(self, background, screen):
        #clear everything on the screen (640 x 480)
        screen.blit(background.convert(),(0,0))

    def is_robot(self, sprite):
        if sprite.z == 0:
            return True
        else:
            return False
