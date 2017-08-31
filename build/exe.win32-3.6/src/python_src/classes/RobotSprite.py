#Import librairies
import pygame, png, math, sys
from random import randint
from threading import Thread

from src.python_src.constants import *
from src.python_src.classes import Powers
from src.python_src.classes import EffectSprite

class Class_RobotSprite(pygame.sprite.Sprite):

    def __init__(self, x, y, z, size_x, size_y, all_sprites_list, style):

        super(Class_RobotSprite, self).__init__()
        #STATE
        self.state, self.previous_state = "IDLE", ""
        #KEYS and DIRECTIONS
        self.k_left, self.k_right = False, False
        #HITBOX INFO
        self.collidable = False
        self.block_list = all_sprites_list
        self.hitbox_size_x, self.hitbox_size_y = 18, 24
        self.hitbox_delta_x, self.hitbox_delta_y = int((size_x - self.hitbox_size_x)/2), int((size_y - self.hitbox_size_y))
        self.hitbox_show = False
        self.k_hitbox = False
        self.collide_image = pygame.image.load(constants.PATH_HIT + constants.HITBOX_STYLE + ".png").convert()
        position = (x + self.hitbox_delta_x, y + self.hitbox_delta_y)
        self.collide_size = (self.hitbox_size_x, self.hitbox_size_y)
        self.collide_rect = pygame.Rect(position,self.collide_size)
        #SPRITE INFO
        self.init_x, self.init_y = x, y
        self.pos_x, self.pos_y, self.z = x, y, 0
        self.size_x, self.size_y = size_x, size_y
        self.sheet = pygame.image.load(constants.PATH_CHARA + constants.ROBOTSET_STYLE[style] + ".png").convert_alpha()
        self.nb_sprites_x = 8
        self.index = 0
        self.set_sprite, self.set_sprite_offset = 0, [0, 1]
        self.set_sprite_offset_duration = 0
        position, self.size = (self.pos_x, self.pos_y), (self.size_x, self.size_y)
        self.previous_position = position
        self.rect = pygame.Rect(position,self.size)
        self.powers = Powers.Classe_Powers(constants.ROBOTSET_STYLE[style], size_x)
        self.sprite_anim_speed = 0.25
        #SPRITE SHADOW
        shadow_sprite = False
        #MOVEMENTS
        self.speed_x_pattern = [1,0,1,0,1,0,1,1,1,1,2,1,2,2,2,2,2,2]
        self.dir_x_duration = 0
        self.dir_x_max = len(self.speed_x_pattern)-1
        self.speed_x = self.speed_x_pattern[self.dir_x_duration]
        #GRAVITY
        self.speed_y_pattern_gravity = [1,0,1,0,1,1,1,2,2,3,3,4,5]
        self.speed_y_pattern_jump = self.powers.get_y_pattern()
        self.dir_y_duration = 0
        self.dir_y_max = len(self.speed_y_pattern_gravity)-1
        self.speed_y = self.speed_y_pattern_gravity[self.dir_y_duration]
        self.fall_new = False
        self.fall_old = False
        #JUMP
        self.jump_new = False
        self.jump_old = False
        self.touch_land = False
        self.jump_max = 2
        #JUMP EFFECT 
        self.jump_effect_sprite = EffectSprite.Class_EffectSprite()
        #ELEMENT TILE
        self.walk_on_element = False
        #WALLJUMP
        self.wall_left = False
        self.wall_right = False
        self.can_wall_jump = False
        self.wall_jump_max = 2
        self.pushed_left = 0
        self.pushed_right = 0
        self.pushed_duration = 25
        #IMAGE
        self.image = self.get_frame(int(self.index))   
        #UPDATE LIMIT
        self.have_to_update = True
        #CAMERA SETTINGS
        self.camera_step_x = 0
        self.camera_step_y = 0
        self.camera_speed_x = 0
        self.camera_speed_y = 0
        #START!
        self.reset_position()
        
    def reset_position(self):
        #Reset to the initial position
        self.move_to_xy(self.init_x, self.init_y)

    def move_to_xy(self,x,y):
        #Move the sprite to the desire location
        self.rect.left = x
        self.rect.top = y
        self.collide_rect.left = x + self.hitbox_delta_x
        self.collide_rect.top = y + self.hitbox_delta_y

    def get_frame(self, ID):
        #Get the correct frame of the sprite depending on his movements
        self.spr_x = (ID % self.nb_sprites_x) * self.size_x
        sprite_surface = pygame.Surface((self.size_x,self.size_y*self.set_sprite_offset[1])).convert_alpha()
        sprite_surface.fill((0,0,0,0)) 
        set_sprite = self.set_sprite + self.set_sprite_offset[0]
        self.spr_y = set_sprite * self.size_y
        rect = pygame.Rect(self.spr_x, self.spr_y, self.size_x,self.size_y*self.set_sprite_offset[1])
        sprite_surface.blit(self.sheet,(0,0),rect)
            
        if self.hitbox_show:
            sprite_surface.blit(self.collide_image,(self.hitbox_delta_x,self.hitbox_delta_y),self.collide_rect)

        return sprite_surface

    def block_is_around_robot(self, my_block):
        #check if the block is around the player (3x3 block around)
        if abs(my_block.rect.left - self.collide_rect.left) <= 32+16 and abs(my_block.rect.top - self.collide_rect.top) <= 32+16:
            return True
        else:
            return False

    def can_fall(self, step):
        #try to fall below by one pixel
        self.collide_rect.top += step
        self.walk_on_element = False
        for block in self.block_list:
            if block.collidable and self.block_is_around_robot(block):
                if self.collide_rect.colliderect(block.rect) == 1:
                    self.collide_rect.top -= step
                    return False
            if type(block).__name__ == "Class_ElementSprite":
                if not self.walk_on_element:
                    if self.collide_rect.colliderect(block.rect) == 1:
                        if block.activated and block.top_sprite == 0:
                            if self.collide_rect.top + self.collide_rect.height - 1 == block.rect.top:
                                self.collide_rect.top -= step
                                self.walk_on_element = True
                                return False
        self.collide_rect.top -= step
        return True

    def can_jump(self, step):
        #try to jump above by 1 pixel
        self.collide_rect.top += step
        for block in self.block_list:
            if block.collidable and self.block_is_around_robot(block):
                if self.collide_rect.colliderect(block.rect) == 1:
                    self.collide_rect.top -= step
                    return False
        self.collide_rect.top -= step
        return True
    
    def can_move(self, step):
        #try to move toward step x direction (<- or ->) by 1 pixel
        self.collide_rect.left += step
        for block in self.block_list:
            if block.collidable and self.block_is_around_robot(block):
                if self.collide_rect.colliderect(block.rect) == 1:
                    self.collide_rect.left -= step
                    if step > 0:
                        self.wall_right = True
                    else:
                        self.wall_left = True
                    return False
        self.collide_rect.left -= step
        self.wall_left = False
        self.wall_right = False
        return True
    
    def update_gravity(self):
        #Simulate the gravity
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

        if self.touch_land:
            self.jump_max = 2

        if not self.k_jump:
            if self.jump_max == 1:
                self.jump_max = 0
            if self.wall_jump_max == 1:
                self.wall_jump_max = 2

        if self.wall_left and self.k_left:
            self.can_wall_jump = True
        elif self.wall_right and self.k_right:
            self.can_wall_jump = True
        else:
            self.can_wall_jump = False
    
        if self.k_jump:
            if self.can_wall_jump: # and self.wall_jump_max == 2:
                self.jump_old = False
                self.jump_new = True
                self.fall_old = False
                self.fall_new = False
                self.touch_land = False
                if self.wall_left:
                    self.pushed_right = self.pushed_duration
                    self.pushed_left = 0
                elif self.wall_right:
                    self.pushed_left = self.pushed_duration
                    self.pushed_right = 0
                #self.wall_jump_max = 1
            if not self.jump_old and not self.jump_new and self.touch_land:
                self.jump_old = False
                self.jump_new = True
                self.fall_old = False
                self.fall_new = False
                self.touch_land = False
                self.jump_max = 1
            if (self.jump_max == 0 or (self.fall_new and self.jump_max == 2)) and not self.can_wall_jump:
                self.jump_old = False
                self.jump_new = True
                self.fall_old = False
                self.fall_new = False
                self.touch_land = False
                self.jump_max = -1                
        else:
            self.jump_new = False

        if self.walk_on_element and self.k_down:
            self.rect.top += 1
            self.collide_rect.top += 1
  
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

        if self.jump_new and not self.jump_old:
            self.jump_effect_sprite.type = self.jump_max
            self.jump_effect_sprite.rect.top = self.rect.top
            self.jump_effect_sprite.rect.left = self.rect.left
            self.jump_effect_sprite.index = 0
  
        if self.set_sprite_offset[0] > 0:
            self.set_sprite_offset_duration -= 1
            if self.set_sprite_offset_duration == 0:
                self.set_sprite_offset = [0, 1]

        if (self.jump_new and not self.jump_old):
            self.powers.play_jump_start_sound()
            self.nb_sprites_x = self.powers.get_nb_sprites_animation()
            self.set_sprite_offset = self.powers.get_jump_animation()
            self.index = 0
            self.set_sprite_offset_duration = 100
            
        if (self.fall_new and not self.fall_old):
            self.nb_sprites_x = 13
            self.index = 0
            self.set_sprite_offset = [9, 1]
            self.set_sprite_offset_duration = 100

        if self.jump_new or self.fall_new:
           self.set_sprite_offset_duration = 100
           
        if (self.fall_old and not self.fall_new):
            self.nb_sprites_x = 8
            self.jump_new = False
            self.jump_old = False
            self.touch_land = True
            self.index = 0
            self.set_sprite_offset = [3, 1]
            self.set_sprite_offset_duration = 6*4 -1

        if self.state == "IDLE":
            self.set_sprite = 0
        if self.state == "LEFT":
            self.set_sprite = 1
            if self.set_sprite_offset[1] == 3:
                self.set_sprite += 2
        if self.state == "RIGHT":
            self.set_sprite = 2
            if self.set_sprite_offset[1] == 3:
                self.set_sprite += 4

        if self.state_change():
            self.index = 0
                
        self.update_animation_index()
        self.image = self.get_frame(int(self.index))

    def update_animation_index(self):
        if self.index < 1 and self.state == "IDLE" and self.set_sprite_offset[0] == 0:
            self.index = 0.005
        else:
            self.index += self.sprite_anim_speed

        if self.index >= self.nb_sprites_x:
            self.index = 0
            
    def state_change(self):
        if self.previous_state != self.state:
            self.previous_state = self.state
            return True
        else:
            return False

    def get_all_keys(self):
        keys = pygame.key.get_pressed()
        self.k_hitbox = False #keys[pygame.K_LSHIFT]
        self.k_left = keys[pygame.K_a]
        self.k_right = keys[pygame.K_d]
        self.k_down = keys[pygame.K_s]
        self.k_jump = keys[pygame.K_SPACE]
        self.k_reset = keys[pygame.K_F5]

        if self.pushed_left > 0:
            self.k_left = True
            self.k_right = False
            self.pushed_left -= 1
        if self.pushed_right > 0:
            self.k_right = True
            self.k_left = False
            self.pushed_right -= 1
        
    def update(self, center):
        if self.have_to_update:
            self.have_to_update = False
            self.get_all_keys()
            self.update_gravity()
            self.update_state()
            self.update_movement()
            self.update_animation()
            #self.shadow_sprite.update_from_origin()
