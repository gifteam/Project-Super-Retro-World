#Globals imports
import pygame
from src.python_src.constants import *

class Classe_Powers(object):
    
    def __init__(self, image, size_x):
        #POWER 000 : NORMAL
        self.speed_y_pattern_jump = [9,8,7,6,5,4,3,3,3,2,2,2,2,2,1,2,1,1,1,0,1,1,0,1,0,0] #67 pix high
        self.size_x = size_x
        self.sound_jump = pygame.mixer.Sound(constants.PATH_SOUND + "game_player_jump.wav")
        self.sound_jump.set_volume(0.5)
        
        #POWER 001 : SUPER JUMP
        self.super_jump = False
        self.speed_y_pattern_super_jump = [16,12,10,9,9,8,9,8,6,6,5,5,4,4,3,3,3,3,3,2,2,2,2,2,2,2,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0] #? pix high
        self.sound_super_jump_start = pygame.mixer.Sound(constants.PATH_SOUND + "game_player_power_001_super_jump_001.wav")
        self.sound_super_jump_start.set_volume(0.5)
        self.sound_super_jump_end = pygame.mixer.Sound(constants.PATH_SOUND + "game_player_power_001_super_jump_002.wav")
        self.sound_super_jump_end.set_volume(0.5)

        #POWER 002 : LIGHT

    def get_y_pattern(self):
        if self.super_jump:
            return self.speed_y_pattern_super_jump
        else:
            return self.speed_y_pattern_jump

    def get_jump_animation(self):
        if self.super_jump:
            return [12, 3]
        else:
            return [6, 1]
            
    def get_nb_sprites_animation(self):
        if self.super_jump:
            return 13
        else:
            return 8

    def play_jump_start_sound(self):
        if self.super_jump:
            self.sound_super_jump_start.play()
        else:
            self.sound_jump.play()

    def play_jump_end_sound(self):
        if self.super_jump:
            self.sound_super_jump_end.play()

    def get_set_sprites(self):
        if self.super_jump:
            return 3
        else:
            return 1
