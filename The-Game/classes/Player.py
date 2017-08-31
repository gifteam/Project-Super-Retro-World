#Import basic librairies
import pyglet
from pyglet import window
from pyglet.gl import *
#Import personal packages
from constants import constants
from classes import Event

class Player_sprite(pyglet.sprite.Sprite):

    def __init__(self, anim_state, x, y, z, my_batch, my_group, spr_type, collidable, my_scene, my_event_list, my_event):

        #game - - - - - - - - - - - - - - - - - - - -
        self.dt = 0
        self.my_scene = my_scene
        self.type = spr_type
        self.event_list = my_event_list
        self.my_event = my_event
        self.check_event = True
        #scene - - - - - - - - - - - - - - - - - - - -
        self.scene_start = 0
        self.scene_start_step_1 = 80
        self.scene_start_step_2 = 140
        self.scene_start_step_3 = 220
        #animation - - - - - - - - - - - - - - - - - -
        self.anim_state = anim_state
        self.old_anim_state = anim_state
        self.create_all_anim_sequences()
        super(Player_sprite, self).__init__(img=self.all_anim_sequences[self.anim_state], x=x, y=y, batch=my_batch, group=my_group)
        #player sprite movement param - - - - - - - -
        self.origin_x = x
        self.origin_y = y
        self.moving_left = False
        self.moving_right = False
        self.moving_x_pattern = [0,0,0,1,1,2,3,4,5,6]
        self.duration_moving = 0
        self.duration_moving_max = len(self.moving_x_pattern) - 1
        self.new_direction = ""
        self.old_direction = ""
        #collisions - - - - - - - - - - - - - - - - -
        self.sprite_list = []
        self.sprite_list_collidable = []
        self.collidable = collidable
        self.rect = [0,0,18,24]
        #jump - - - - - - - - - - - - - - - - - - - -
        self.jump_y_pattern = [int((1000 - x)/100) for x in range(0,1000,50)]
        self.duration_jump = 0
        self.duration_jump_max = len(self.jump_y_pattern) - 1
        self.new_jump = False
        self.old_jump = False
        self.want_to_jump = False
        #fall - - - - - - - - - - - - - - - - - - - -
        self.falling_y_pattern = [int((x)/100) for x in range(50,900,50)]
        self.duration_falling = 0
        self.duration_falling_max = len(self.falling_y_pattern) - 1
        self.new_fall = False
        self.old_fall = False
        #keys - - - - - - - - - - - - - - - - - - - -
        self.moving_left = False
        self.moving_left_old = False
        self.moving_right = False
        self.moving_right_old = False
        self.want_to_jump = False
        self.want_to_action = False
        # - - - - - - - - - - - - - - - - - - - - - -
        self.reset_position()


    def create_all_anim_sequences(self):
        
        self.all_anim_sequences = {}
        self.all_anim_sequences["IDLE_LEFT"] = self.get_new_sequence("IDLE_LEFT")
        self.all_anim_sequences["IDLE_RIGHT"] = self.get_new_sequence("IDLE_RIGHT")
        self.all_anim_sequences["JUMP_LEFT"] = self.get_new_sequence("JUMP_LEFT")
        self.all_anim_sequences["JUMP_RIGHT"] = self.get_new_sequence("JUMP_RIGHT")
        self.all_anim_sequences["FALL_LEFT"] = self.get_new_sequence("FALL_LEFT")
        self.all_anim_sequences["FALL_RIGHT"] = self.get_new_sequence("FALL_RIGHT")
        self.all_anim_sequences["WALK_LEFT"] = self.get_new_sequence("WALK_LEFT")
        self.all_anim_sequences["WALK_RIGHT"] = self.get_new_sequence("WALK_RIGHT")
        self.all_anim_sequences["SLEEP"] = self.get_new_sequence("SLEEP")
        self.all_anim_sequences["FORM"] = self.get_new_sequence("FORM")
        self.all_anim_sequences["WAKE_UP"] = self.get_new_sequence("WAKE_UP")
        self.all_anim_sequences["DEATH"] = self.get_new_sequence("DEATH")

    def get_new_sequence(self, sequence):
        
        filename, x, y, w, h, loop, nb_frame, speed = self.get_anim_sequence(sequence)
        player_complete_image = pyglet.image.load(constants.PATH_CHARA + filename + ".png")
        player_region = player_complete_image.get_region(x, y, w, h)
        player_sequence = pyglet.image.ImageGrid(player_region, 1, nb_frame)
        for img in player_sequence:
            self.anti_aliasied_texture(img)
        player_animation = pyglet.image.Animation.from_image_sequence(player_sequence, speed, loop)
        return player_animation

    
    def get_anim_sequence(self, state):
        
        if state == "IDLE_LEFT":
            return constants.PLAYER_STYLE[self.my_scene], 0, 13*constants.SPRITE_Y, 8*constants.SPRITE_X, constants.SPRITE_Y, True, 8, 0.12
        if state == "IDLE_RIGHT":
            return constants.PLAYER_STYLE[self.my_scene], 0, 11*constants.SPRITE_Y, 8*constants.SPRITE_X, constants.SPRITE_Y, True, 8, 0.12
        if state == "WALK_LEFT":
            return constants.PLAYER_STYLE[self.my_scene], 0, 10*constants.SPRITE_Y, 8*constants.SPRITE_X, constants.SPRITE_Y, True, 8, 0.06
        if state == "WALK_RIGHT":
            return constants.PLAYER_STYLE[self.my_scene], 0, 9*constants.SPRITE_Y, 8*constants.SPRITE_X, constants.SPRITE_Y, True, 8, 0.06
        if state == "JUMP_LEFT":
            return constants.PLAYER_STYLE[self.my_scene], 0, 5*constants.SPRITE_Y, 8*constants.SPRITE_X, constants.SPRITE_Y, True, 8, 0.06
        if state == "JUMP_RIGHT":
            return constants.PLAYER_STYLE[self.my_scene], 0, 5*constants.SPRITE_Y, 8*constants.SPRITE_X, constants.SPRITE_Y, True, 8, 0.06
        if state == "FALL_LEFT":
            return constants.PLAYER_STYLE[self.my_scene], 0, 1*constants.SPRITE_Y, 8*constants.SPRITE_X, constants.SPRITE_Y, True, 8, 0.06
        if state == "FALL_RIGHT":
            return constants.PLAYER_STYLE[self.my_scene], 0, 0*constants.SPRITE_Y, 8*constants.SPRITE_X, constants.SPRITE_Y, True, 8, 0.06
        if state == "SLEEP":
            return constants.PLAYER_STYLE[self.my_scene], 0, 12*constants.SPRITE_Y, constants.SPRITE_X, constants.SPRITE_Y, False, 1, 5
        if state == "WAKE_UP":
            return constants.PLAYER_STYLE[self.my_scene], 0, 12*constants.SPRITE_Y, 2*constants.SPRITE_X, constants.SPRITE_Y, True, 2, 0.2
        if state == "FORM":
            return constants.WAKE_UP_STYLE[self.my_scene], 0, 0*constants.SPRITE_Y, 40*constants.SPRITE_X, constants.SPRITE_Y * 2, False, 40, 0.03
        if state == "DEATH":
            return constants.PLAYER_STYLE[self.my_scene], 2*constants.SPRITE_X, 12*constants.SPRITE_Y, 1*constants.SPRITE_X, constants.SPRITE_Y, False, 1, 1


    def update(self, sprite_list, dt):

        self.dt = dt
        self.update_player()


    def update_player(self):

        self.update_player_gravity()
        self.update_player_movement()
        self.update_event()
        self.update_death()
        self.update_anim_sequence()


    def update_death(self):

        if self.y < 0 - constants.SPRITE_Y:
            self.my_event.action(-1)
            
         
    def update_event(self):

        self.check_event = not self.check_event

        if self.check_event:
            for event in self.event_list:
                if event[5]:
                    if (event[1] + event[3]) > (self.rect[1]) and (event[1]) < (self.rect[1] + self.rect[3]):
                        if (event[0] + event[2]) > (self.rect[0]) and (event[0]) < (self.rect[0] + self.rect[2]):
                            if self.want_to_action:    
                                self.my_event.action(event[4]) 

          
    def update_anim_sequence(self):
    
        if self.anim_state != self.old_anim_state:
            self.image = self.all_anim_sequences[self.anim_state]
            self.old_anim_state = self.anim_state

            
    def update_player_gravity(self):
        
        step = -1
        if self.can_fall(step) and not self.new_jump:
            self.new_fall = True
        else:
            self.new_fall = False
        
        if not self.new_fall and not self.old_fall:
            self.duration_falling = 0
            self.old_fall = self.new_fall

        if self.new_fall:
            if self.duration_falling < self.duration_falling_max:
                self.duration_falling += 1

            for i in range(self.falling_y_pattern[self.duration_falling]):
                if self.can_fall(step):
                    self.y += step
                    self.rect[1] += step
                else:
                    self.new_fall = False

                    
    def update_player_jump(self):
        
        step = 1
        if not self.can_fall(-1) and self.want_to_jump:
                self.duration_jump = 0
                self.new_jump = True
                self.want_to_jump = False
        
        if self.new_jump:        
            for i in range(self.jump_y_pattern[self.duration_jump]):
                if self.can_fall(step):
                    self.y += step
                    self.rect[1] += step
                else:
                    self.new_jump = False
                
            if self.duration_jump < self.duration_jump_max:
                self.duration_jump += 1
            else:
                self.new_jump = False
            
        self.old_jump = self.new_jump
            

    def update_player_animation(self):

        if self.new_fall:
            self.anim_state = "FALL_RIGHT"
            if self.moving_left:
                self.anim_state = "FALL_LEFT"
            return
            
        if self.new_jump:
            self.anim_state = "JUMP_RIGHT"
            if self.moving_left:
                self.anim_state = "JUMP_LEFT"
            return
        
        if self.moving_left and not self.moving_right:
            self.anim_state = "WALK_LEFT"
            return
            
        if self.moving_right and not self.moving_left:
            self.anim_state = "WALK_RIGHT"
            return
        
        if (self.moving_left_old and not self.moving_left) or self.new_direction == "left":
            self.anim_state = "IDLE_LEFT"
            return
        
        if (self.moving_right_old and not self.moving_right) or self.new_direction == "" or self.new_direction == "right":
            self.anim_state = "IDLE_RIGHT"
            return
        
        return
                
    def update_player_movement(self):

        if self.anim_state == "DEATH":
            return

        if self.scene_start < self.scene_start_step_1:
            self.anim_state = "SLEEP"
            self.scene_start +=1
            return
        elif self.scene_start < self.scene_start_step_2:
            self.anim_state = "WAKE_UP"
            self.scene_start +=1
            return
        elif self.scene_start < self.scene_start_step_3:
            self.anim_state = "FORM"
            self.scene_start +=1
            return
        elif self.scene_start < self.scene_start_step_3+1:
            self.anim_state = "IDLE_RIGHT"
            self.scene_start +=1
            

        self.update_player_animation()


        self.moving_left_old = self.moving_left
        self.moving_right_old = self.moving_right

        
        self.update_player_jump()

        if (not self.moving_left and not self.moving_right) or (self.moving_left and self.moving_right):
            self.duration_moving = 0
            self.new_direction = ""
            
        if self.new_direction != self.old_direction:
            self.duration_moving = 0
            self.old_direction = self.new_direction

        if self.duration_moving < self.duration_moving_max:
            self.duration_moving += 1
        else:
            self.duration_moving -= 1
        
        if self.moving_left and not self.moving_right:
            step = -1
            for i in range(self.moving_x_pattern[self.duration_moving]):
                if self.can_move(step):
                    self.x += step
                    self.rect[0] += step
                    self.new_direction = "left"
            
        if self.moving_right and not self.moving_left:
            step = 1
            for i in range(self.moving_x_pattern[self.duration_moving]):
                if self.can_move(step):
                    self.x += step
                    self.rect[0] += step
                    self.new_direction = "right"


    def can_move(self, step):
        for sprite in self.sprite_list_collidable:
            if (sprite.x + sprite.rect[2]) >= (self.rect[0] + step) and (sprite.x) <= (self.rect[0] + self.rect[2] + step):
                if (sprite.y + sprite.rect[3]) >= (self.rect[1]) and (sprite.y) <= (self.rect[1] + self.rect[3]):
                    return False
        return True
    
        
    def can_fall(self, step):
        for sprite in self.sprite_list_collidable:
            if (sprite.x + sprite.rect[2]) >= (self.rect[0]) and (sprite.x) <= (self.rect[0] + self.rect[2]):
                if (sprite.y + sprite.rect[3]) >= (self.rect[1] + step) and (sprite.y) <= (self.rect[1] + self.rect[3] + step):
                    return False
        return True

    
    def reset_position(self):
        
        self.move_to(self.origin_x, self.origin_y)

        
    def move_to(self, x, y):
        
        self.x, self.y = x, y
        self.rect[0] = self.x + abs(self.rect[2] - 32)/2
        self.rect[1] = self.y


    def key_pressed(self, key, modifiers):
        
        if key == window.key.LEFT:
            self.moving_left = True
        if key == window.key.RIGHT:
            self.moving_right = True
        if key == window.key.F5:
            self.reset_position()
        if key == window.key.SPACE:
            self.want_to_jump = True
        if key == window.key.ENTER or key == window.key.RETURN:
            self.want_to_action = True
            
    def key_released(self, key, modifiers):
        
        if key == window.key.LEFT:
            self.moving_left = False
        if key == window.key.RIGHT:
            self.moving_right = False
        if key == window.key.SPACE:
            self.want_to_jump = False
        if key == window.key.ENTER or key == window.key.RETURN:
            self.want_to_action = False


    def anti_aliasied_texture(self, img):
        
        texture = img.get_texture()
        glBindTexture(texture.target, texture.id)
        glTexParameteri(texture.target,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        glBindTexture(texture.target,0)
