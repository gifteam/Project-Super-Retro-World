#Import librairies
import pygame, png, math, sys
from random import randint

from src.python_src.constants import *

class Choose_name_sprite(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Choose_name_sprite, self).__init__()
        self.screen = screen
        #SPRITES PARAM

        #MAIN MUSIC
        self.main_title_music = pygame.mixer.Sound(constants.PATH_SOUND + "game_scene_title_02.wav")
        self.main_title_music.set_volume(1)
        self.main_title_music.play(loops=-1)
        #MENU SOUND EFFECT
        self.cursor_sound = pygame.mixer.Sound(constants.PATH_SOUND + "game_menu_select_01.wav")
        self.select_sound = pygame.mixer.Sound(constants.PATH_SOUND + "game_menu_select_02.wav")
        self.cursor_sound.set_volume(0.5)
        self.select_sound.set_volume(1)
        #FADE SCREEN
        self.fade_surface = pygame.Surface((constants.SCREEN_X,constants.SCREEN_Y))
        self.fade_surface.fill((0,0,0))
        self.fade_surface.set_alpha(2)
        #TEXT
        self.index = 0
        self.position = (320,240)
        self.title_font = pygame.font.SysFont("Impact", 20)
        self.color = (255,255,255)
        self.text = ["New game", "Continue", "Quit"]
        self.k_up = False
        self.k_down = False
        self.k_enter = False

    def go_to_next_scene(self):
        if self.k_enter:
            self.select_sound.play()
            self.main_title_music.fadeout(2000)
            for i in range(300):
                self.screen.blit(self.fade_surface, (0,0))
                pygame.display.flip()
            return self.text[self.index]
        else:
            return ""
    
    def set_all_previous_keys(self):
        self.previous_k_up = self.k_up
        self.previous_k_down = self.k_down
        self.previous_k_left = self.k_left
        self.previous_k_right = self.k_right

    def get_all_new_keys(self):
        keys = pygame.key.get_pressed()
        self.k_up = keys[pygame.K_UP]
        self.k_down = keys[pygame.K_DOWN]
        self.k_left = keys[pygame.K_LEFT]
        self.k_right = keys[pygame.K_RIGHT]
        self.k_enter = keys[pygame.K_RETURN]

    def print_title(self):
        text = self.text[self.index]
        self.image = self.title_font.render(text, 1, self.color)
        self.screen.blit(self.image, (self.position[0], self.position[1]))
  
    def move_cursor(self):
        if self.k_up and not self.previous_k_up:
            self.index = (self.index - 1) % 3
            self.cursor_sound.play()
        elif self.k_down and not self.previous_k_down:
            self.index = (self.index + 1) % 3
            self.cursor_sound.play()
        if self.k_left and not self.previous_k_left:
            self.index = (self.index - 1) % 3
            self.cursor_sound.play()
        if self.k_right and not self.previous_k_right:
            self.index = (self.index - 1) % 3
            self.cursor_sound.play()
            
    def update_screen(self):
        self.image_anim_frame = (self.image_anim_frame + 0.02) % self.image_anim_frame_max
        x = self.image_anim_frame
        for img_id in range(len(self.images_list)):
            img = self.images_load[img_id]
            pos = ((constants.SCREEN_X - img.get_rect().size[0])/2, (constants.SCREEN_Y - img.get_rect().size[1])/2)
            if self.images_list[img_id] == "007" or self.images_list[img_id] == "012":
                pos = (pos[0] + math.cos(x) * 5, pos[1] + math.sin(x) * 10)
            if self.images_list[img_id] == "008" or self.images_list[img_id] == "013":
                pos = (pos[0] - math.cos(x) * 5, pos[1] - math.sin(x) * 10)
            self.screen.blit(img, pos)
        #Add big bubble
        self.image_bubble_index = (self.image_bubble_index + 0.15) % self.image_bubble_nb_sprites
        img = self.get_bubble_frame(int(self.image_bubble_index))
        pos = (268, 139)
        self.screen.blit(img, pos)
        #Add little bubble
        self.image_bubble_2_index = (self.image_bubble_2_index + 0.15) % self.image_bubble_2_nb_sprites
        img = self.get_bubble_2_frame(int(self.image_bubble_2_index))
        pos = (206, 162)
        self.screen.blit(img, pos)
        
    def update(self):
        self.set_all_previous_keys()
        self.get_all_new_keys()
        #self.update_screen()
        #self.move_cursor()
        #self.print_title()
        pygame.display.flip()

