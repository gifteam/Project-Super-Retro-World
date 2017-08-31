#Import librairies
import pygame, png, math, sys
from random import randint

from src.python_src.constants import *

class Class_CPUSprite(pygame.sprite.Sprite):

    def __init__(self, image, x, y, z, size_x, size_y, all_sprites_list, brain):

        super(Class_CPUSprite, self).__init__()
        #STATE
        self.state, self.previous_state = "IDLE", ""
        #KEYS and DIRECTIONS
        self.k_left, self.k_right = False, False
        #HITBOX INFO
        self.collidable = False
        self.block_list = all_sprites_list
        self.hitbox_size_x, self.hitbox_size_y = 14, 24
        self.hitbox_delta_x, self.hitbox_delta_y = int((size_x - self.hitbox_size_x)/2), int((size_y - self.hitbox_size_y))
        self.hitbox_show = False
        self.k_hitbox = False
        self.collide_image = pygame.image.load(constants.PATH_HIT + constants.HITBOX_STYLE + ".png").convert()
        position = (x + self.hitbox_delta_x, y + self.hitbox_delta_y)
        self.collide_size = (self.hitbox_size_x, self.hitbox_size_y)
        self.collide_rect = pygame.Rect(position,self.collide_size)
        #SPRITE INFO
        self.pos_x, self.pos_y, self.z = x, y, 0
        self.size_x, self.size_y = size_x, size_y
        self.sheet = pygame.image.load(constants.PATH_CHARA + image + ".png").convert_alpha()
        self.nb_sprites_x = self.sheet.get_width() / self.size_x
        self.index = 0
        self.set_sprite, self.set_sprite_offset = 0, 0
        position, self.size = (self.pos_x, self.pos_y), (self.size_x, self.size_y)
        self.rect = pygame.Rect(position,self.size)
        #SPRITE SHADOW
        shadow_sprite = False
        #MOVEMENTS
        self.speed_x_pattern = [1,0,1,0,1,0,1,1,1,1,2,1,2,2,2,2,2,2]
        self.dir_x_duration = 0
        self.dir_x_max = len(self.speed_x_pattern)-1
        self.speed_x = self.speed_x_pattern[self.dir_x_duration]
        #GRAVITY
        self.speed_y_pattern_gravity = [1,0,1,0,1,1,1,2,2,3,3,4,5]
        self.speed_y_pattern_jump = [9,8,7,6,5,4,3,3,3,2,2,2,2,2,1,2,1,1,1,0,1,1,0,1,0,0]
        self.dir_y_duration = 0
        self.dir_y_max = len(self.speed_y_pattern_gravity)-1
        self.speed_y = self.speed_y_pattern_gravity[self.dir_y_duration]
        self.fall_new = False
        self.fall_old = False
        #JUMP
        self.jump_new = False
        self.jump_old = False
        self.touch_land = False
        #IMAGE
        self.image = self.get_frame(int(self.index))   
        #SOUND EFFECT
        pygame.mixer.music.load(constants.PATH_SOUND + "game_player_jump.wav")
        #BRAIN
        self.brain = brain
        #START!
        self.reset_position()

    def reset_position(self):
        self.move_to_xy(1*32,8*32)

    def move_to_xy(self,x,y):
        self.rect.left = x
        self.rect.top = y
        self.collide_rect.left = x + self.hitbox_delta_x
        self.collide_rect.top = y + self.hitbox_delta_y

    def get_frame(self, ID):
        set_sprite = self.set_sprite + self.set_sprite_offset
        self.spr_x = (ID % self.nb_sprites_x) * self.size_x
        self.spr_y = set_sprite * self.size_y
        rect = pygame.Rect(self.spr_x, self.spr_y, self.size_x,self.size_y)
        sprite_surface = pygame.Surface((32,32)).convert_alpha()
        sprite_surface.fill((0,0,0,0))
        sprite_surface.blit(self.sheet,(0,0),rect)

        if self.hitbox_show:
            sprite_surface.blit(self.collide_image,(self.hitbox_delta_x,self.hitbox_delta_y),self.collide_rect)

        return sprite_surface

    def can_fall(self, step):
        #try to fall below
        self.collide_rect.top += step
        for block in self.block_list:
            if block.collidable:
                if self.collide_rect.colliderect(block.rect) == 1:
                    self.collide_rect.top -= step
                    return False
        self.collide_rect.top -= step
        return True

    def can_jump(self, step):
        #try to jump above
        self.collide_rect.top += step
        for block in self.block_list:
            if block.collidable:
                if self.collide_rect.colliderect(block.rect) == 1:
                    self.collide_rect.top -= step
                    return False
        self.collide_rect.top -= step
        return True

    def update_gravity(self):

        if (self.jump_old and not self.jump_new) or (self.jump_new and not self.jump_old):
            self.dir_y_duration = 0
            
        if self.jump_new:
            step = -1
            self.dir_y_max = len(self.speed_y_pattern_jump)-1
            if self.dir_y_duration == self.dir_y_max - 1:
                self.jump_new = False
                self.dir_y_duration = 0
                return
            self.speed_y = self.speed_y_pattern_jump[self.dir_y_duration]
            if self.can_jump(step):
                self.dir_y_duration += 1
            else:
                self.jump_new = False
                self.dir_y_duration = 0
                return
            for i in range(self.speed_y):    
                if self.can_jump(step):
                    self.rect.top += step
                    self.collide_rect.top += step
        else:
            step = 1
            self.dir_y_max = len(self.speed_y_pattern_gravity)-1
            if self.dir_y_duration > self.dir_y_max:
                self.dir_y_duration = self.dir_y_max
            self.speed_y = self.speed_y_pattern_gravity[self.dir_y_duration]
            self.fall_old = self.fall_new
            if self.can_fall(step):
                self.fall_new = True
                self.touch_land = False
                self.dir_y_duration += 1
            else:
                self.fall_new = False
                self.dir_y_duration = 0
            for i in range(self.speed_y):    
                if self.can_fall(step):
                    self.rect.top += step
                    self.collide_rect.top += step

        if not self.can_fall(1):
            self.touch_land = True
        
    def can_move(self, step):
        #try to move toward step x direction (<- or ->) by 1 pixel
        self.collide_rect.left += step
        for block in self.block_list:
            if block.collidable:
                if self.collide_rect.colliderect(block.rect) == 1:
                    self.collide_rect.left -= step
                    return False
        self.collide_rect.left -= step
        return True

    def update_movement(self):

        if self.k_reset:
            self.reset_position()
        
        step = 0
        if self.state == "LEFT":
            step = -1
        elif self.state == "RIGHT":
            step = 1
        if self.dir_x_duration > self.dir_x_max:
            self.dir_x_duration = self.dir_x_max
        self.speed_x =self.speed_x_pattern[self.dir_x_duration]
        if step != 0:
            for i in range(self.speed_x):    
                if self.can_move(step):
                    self.rect.left += step
                    self.collide_rect.left += step
        
    def update_state(self):
        if self.k_hitbox:
            self.hitbox_show = True  
        else:
            self.hitbox_show = False

        self.jump_old = self.jump_new
        if self.k_jump:
            if not self.jump_old and not self.jump_new and self.touch_land:
                pygame.mixer.music.play()
                self.jump_new = True
                self.touch_land = False
        else:
            self.jump_new = False
            
        if self.k_left and not self.k_right:
            if self.state == "LEFT":
                self.dir_x_duration += 1
            else:
                self.dir_x_duration = 0
            self.state = "LEFT"
        elif self.k_right and not self.k_left:
            if self.state == "RIGHT":
                self.dir_x_duration += 1
            else:
                self.dir_x_duration = 0
            self.state = "RIGHT"
        else:
            self.state = "IDLE"
            self.dir_x_duration = 0

    def update_animation(self):
        if self.state == "IDLE":
            self.set_sprite = 0
        if self.state == "LEFT":
            self.set_sprite = 1
        if self.state == "RIGHT":
            self.set_sprite = 2
            
        if self.set_sprite_offset > 0:
            self.set_sprite_offset_duration -= 1
            if self.set_sprite_offset_duration == 0:
                self.set_sprite_offset = 0
                
        if (self.fall_old and not self.fall_new):
            self.jump_new = False
            self.jump_old = False
            self.touch_land = True
            self.index = 0
            self.set_sprite_offset = 3
            self.set_sprite_offset_duration = 5*4
            
        self.update_animation_index()
        self.image = self.get_frame(int(self.index))

    def update_animation_index(self):
        if self.index < 1 and self.state == "IDLE" and self.set_sprite_offset == 0:
            self.index += 0.005
        else:
            self.index += 0.125*2
        if int(self.index) >= self.nb_sprites_x:
            self.index = 0
            
    def state_change(self):
        if self.previous_state != self.state:
            return True
        else:
            return False

    def get_all_keys(self):
        self.k_left = self.brain.k_left
        self.k_right = self.brain.k_right
        self.k_jump = self.brain.k_jump
        self.k_hitbox = False
        self.k_reset = False
        
    def update(self, center):

        self.get_all_keys()
        self.update_gravity()
        self.update_state()
        self.update_movement()
        self.update_animation()
        #self.shadow_sprite.update_from_origin()
