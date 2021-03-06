#Import basic librairies
import pyglet
from pyglet import window
import time
from pyglet.gl import *
#Import personal packages
from constants import constants
from classes import Event, Effect

class Player_sprite(pyglet.sprite.Sprite):

    def __init__(self, x, y, z, my_batch, my_group, spr_type, collidable, my_scene, my_event_list):

        #debug - - - - - - - - - - - - - - - - - - -
        self.print_dt = 0 # Nb of frame to print dt time (duration) for each procedure
        #game - - - - - - - - - - - - - - - - - - - -
        self.dt = 0
        self.my_scene = my_scene
        self.type = spr_type
        self.my_batch = my_batch
        self.type_fps = False
        #colorfilter - - - - - - - - - - - - - - - - -
        self.go_colorfilter_new = False
        self.go_colorfilter_red = False
        self.go_colorfilter_green = False
        self.go_colorfilter_blue = False
        #animation - - - - - - - - - - - - - - - - - -
        self.anim_state = "IDLE_RIGHT"
        self.old_anim_state = self.anim_state
        self.create_all_anim_sequences()
        super(Player_sprite, self).__init__(img=self.all_anim_sequences[self.anim_state], x=x, y=y, batch=my_batch, group=my_group)
        #player sprite movement param - - - - - - - -
        self.origin_x = x
        self.origin_y = y
        self.moving_left = False
        self.moving_right = False
        self.moving_x_pattern = [0,0,0,1,1,2,3,4,5]
        self.duration_moving = 0
        self.duration_moving_max = len(self.moving_x_pattern) - 1
        self.new_direction = "RIGHT"
        self.old_direction = "RIGHT"
        #collisions - - - - - - - - - - - - - - - - -
        self.sprite_list = []
        self.sprite_list_collidable = []
        self.collidable = collidable
        self.rect = [0,0,18,24]
        #run + jump effect - - - - - - - - - - - - - -
        self.fog_sprite = Effect.Effect_sprite(z-1, "WALK_FOG", my_batch, self)
        #jump - - - - - - - - - - - - - - - - - - - -
        self.jump_y_pattern = [0,0,0] + [int((1000 - x)/100) for x in range(0,1000,50)]
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

        self.all_anim_sequences["WALK_RIGHT"] = self.get_new_sequence("WALK_RIGHT")
        self.all_anim_sequences["WALK_LEFT"] = self.get_new_sequence("WALK_LEFT")

        self.all_anim_sequences["IDLE_RIGHT"] = self.get_new_sequence("IDLE_RIGHT")
        self.all_anim_sequences["IDLE_LEFT"] = self.get_new_sequence("IDLE_LEFT")
        self.all_anim_sequences["IDLE_EDGE_RIGHT"] = self.get_new_sequence("IDLE_EDGE_RIGHT")
        self.all_anim_sequences["IDLE_EDGE_LEFT"] = self.get_new_sequence("IDLE_EDGE_LEFT")

        self.all_anim_sequences["BREAK_RIGHT_01"] = self.get_new_sequence("BREAK_RIGHT_01")
        self.all_anim_sequences["BREAK_LEFT_01"] = self.get_new_sequence("BREAK_LEFT_01")
        self.all_anim_sequences["BREAK_RIGHT_02"] = self.get_new_sequence("BREAK_RIGHT_02")
        self.all_anim_sequences["BREAK_LEFT_02"] = self.get_new_sequence("BREAK_LEFT_02")

        self.all_anim_sequences["TO_THE_RIGHT"] = self.get_new_sequence("TO_THE_RIGHT")
        self.all_anim_sequences["TO_THE_LEFT"] = self.get_new_sequence("TO_THE_LEFT")

        self.all_anim_sequences["JUMP_RIGHT"] = self.get_new_sequence("JUMP_RIGHT")
        self.all_anim_sequences["JUMP_LEFT"] = self.get_new_sequence("JUMP_LEFT")
        self.all_anim_sequences["JUMP_COMPLETE_RIGHT"] = self.get_new_sequence("JUMP_COMPLETE_RIGHT")
        self.all_anim_sequences["JUMP_COMPLETE_LEFT"] = self.get_new_sequence("JUMP_COMPLETE_LEFT")

        self.all_anim_sequences["FALL_RIGHT"] = self.get_new_sequence("FALL_RIGHT")
        self.all_anim_sequences["FALL_LEFT"] = self.get_new_sequence("FALL_LEFT")
        self.all_anim_sequences["FALL_COMPLETE_RIGHT"] = self.get_new_sequence("FALL_COMPLETE_RIGHT")
        self.all_anim_sequences["FALL_COMPLETE_LEFT"] = self.get_new_sequence("FALL_COMPLETE_LEFT")
                                           
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
        
        if state == "WALK_RIGHT": 
            return constants.PLAYER_STYLE[self.my_scene], 0, 0*constants.SPRITE_Y, 12*constants.SPRITE_X, constants.SPRITE_Y, True, 12, 0.05
        if state == "WALK_LEFT": 
            return constants.PLAYER_STYLE[self.my_scene], 0, 1*constants.SPRITE_Y, 12*constants.SPRITE_X, constants.SPRITE_Y, True, 12, 0.05


        if state == "IDLE_RIGHT": 
            return constants.PLAYER_STYLE[self.my_scene], 0, 2*constants.SPRITE_Y, 1*constants.SPRITE_X, constants.SPRITE_Y, False, 1, 1
        if state == "IDLE_LEFT": 
            return constants.PLAYER_STYLE[self.my_scene], 0, 3*constants.SPRITE_Y, 1*constants.SPRITE_X, constants.SPRITE_Y, False, 1, 1
        if state == "IDLE_EDGE_RIGHT": 
            return constants.PLAYER_STYLE[self.my_scene], 0, 12*constants.SPRITE_Y, 2*constants.SPRITE_X, constants.SPRITE_Y, True, 2, 0.5
        if state == "IDLE_EDGE_LEFT": 
            return constants.PLAYER_STYLE[self.my_scene], 0, 13*constants.SPRITE_Y, 2*constants.SPRITE_X, constants.SPRITE_Y, True, 2, 0.5

        
        if state == "BREAK_RIGHT_01": 
            return constants.PLAYER_STYLE[self.my_scene], 0, 4*constants.SPRITE_Y, 4*constants.SPRITE_X, constants.SPRITE_Y, False, 4, 0.04
        if state == "BREAK_LEFT_01": 
            return constants.PLAYER_STYLE[self.my_scene], 0, 5*constants.SPRITE_Y, 4*constants.SPRITE_X, constants.SPRITE_Y, False, 4, 0.04
        if state == "BREAK_RIGHT_02": 
            return constants.PLAYER_STYLE[self.my_scene], 4*constants.SPRITE_X, 4*constants.SPRITE_Y, 3*constants.SPRITE_X, constants.SPRITE_Y, False, 3, 0.04
        if state == "BREAK_LEFT_02": 
            return constants.PLAYER_STYLE[self.my_scene], 4*constants.SPRITE_X, 5*constants.SPRITE_Y, 3*constants.SPRITE_X, constants.SPRITE_Y, False, 3, 0.04


        if state == "TO_THE_RIGHT": 
            return constants.PLAYER_STYLE[self.my_scene], 0, 6*constants.SPRITE_Y, 3*constants.SPRITE_X, constants.SPRITE_Y, False, 3, 0.04
        if state == "TO_THE_LEFT": 
            return constants.PLAYER_STYLE[self.my_scene], 0, 7*constants.SPRITE_Y, 3*constants.SPRITE_X, constants.SPRITE_Y, False, 3, 0.04    


        if state == "JUMP_RIGHT": 
            return constants.PLAYER_STYLE[self.my_scene], constants.SPRITE_X, 8*constants.SPRITE_Y, 1*constants.SPRITE_X, constants.SPRITE_Y, False, 1, 1
        if state == "JUMP_LEFT": 
            return constants.PLAYER_STYLE[self.my_scene], constants.SPRITE_X, 9*constants.SPRITE_Y, 1*constants.SPRITE_X, constants.SPRITE_Y, False, 1, 1


        if state == "JUMP_COMPLETE_RIGHT": 
            return constants.PLAYER_STYLE[self.my_scene], 0, 8*constants.SPRITE_Y, 2*constants.SPRITE_X, constants.SPRITE_Y, False, 2, 0.05
        if state == "JUMP_COMPLETE_LEFT": 
            return constants.PLAYER_STYLE[self.my_scene], 0, 9*constants.SPRITE_Y, 2*constants.SPRITE_X, constants.SPRITE_Y, False, 2, 0.05


        if state == "FALL_RIGHT": 
            return constants.PLAYER_STYLE[self.my_scene], constants.SPRITE_X*2, 10*constants.SPRITE_Y, 1*constants.SPRITE_X, constants.SPRITE_Y, False, 1, 1
        if state == "FALL_LEFT": 
            return constants.PLAYER_STYLE[self.my_scene], constants.SPRITE_X*2, 11*constants.SPRITE_Y, 1*constants.SPRITE_X, constants.SPRITE_Y, False, 1, 1


        if state == "FALL_COMPLETE_RIGHT": 
            return constants.PLAYER_STYLE[self.my_scene], 0, 10*constants.SPRITE_Y, 3*constants.SPRITE_X, constants.SPRITE_Y, False, 3, 0.1
        if state == "FALL_COMPLETE_LEFT": 
            return constants.PLAYER_STYLE[self.my_scene], 0, 11*constants.SPRITE_Y, 3*constants.SPRITE_X, constants.SPRITE_Y, False, 3, 0.1


    def update(self, sprite_list, dt, himself):
            
        self.dt = dt
        self.update_player()


    def update_player(self):

        self.update_player_gravity()
        self.update_player_movement()
        self.update_death()
        self.update_anim_sequence()
        self.update_effects()

        self.print_dt -= 1

    def update_effects(self):

        self.fog_sprite.update(self.anim_state)

            
    def update_death(self):

        if self.y < 0 - constants.SPRITE_Y:
            self.reset_position()
            
          
    def update_anim_sequence(self):
    
        if self.anim_state != self.old_anim_state:
            self.image = self.all_anim_sequences[self.anim_state]
            self.old_anim_state = self.anim_state
            
            
    def update_player_gravity(self):
        
        step = -1

        self.old_fall = self.new_fall
        
        if self.can_fall(step) and not self.new_jump:
            self.new_fall = True
        else:
            self.new_fall = False
        
        if not self.new_fall and not self.old_fall:
            self.duration_falling = 0

        if self.new_fall:
            if self.duration_falling < self.duration_falling_max:
                self.duration_falling += 1

            step = self.falling_y_pattern[self.duration_falling]
            test = True

            while test:
                if step < 0:
                    test = False
                    self.new_fall = False
                elif not self.can_fall(-1):
                    test = False
                    self.new_fall = False
                elif self.can_fall(step*(-1)):
                    self.y -= step
                    self.rect[1] -= step
                    test = False
                else:
                    step -= 1

                    
    def update_player_jump(self):
        
        step = 1
        if not self.can_fall(-1) and self.want_to_jump:
                self.duration_jump = 0
                self.new_jump = True
                self.want_to_jump = False
        
        if self.new_jump:

            step = self.jump_y_pattern[self.duration_jump]
            test = True
            
            while test:
                if step < 0:
                    test = False
                    self.new_jump = False
                elif not self.can_fall(1):
                    test = False
                    self.new_jump = False
                elif self.can_fall(step):
                    self.y += step
                    self.rect[1] += step
                    test = False
                else:
                    step -= 1
                
            if self.duration_jump < self.duration_jump_max:
                self.duration_jump += 1
            else:
                self.new_jump = False
            
        self.old_jump = self.new_jump

            
    def update_player_animation(self):

        # When you walk
        # Switch to jump animation (complete one) 
        if self.new_jump and not ("JUMP" in self.anim_state):
            self.go_to_complete_jump_anim()
            return
        
        # When you jump (complete version)
        # Switch to basic jump anim (after complete one)
        if self.new_jump and self._frame_index == 1 and self.anim_state[:13] == "JUMP_COMPLETE":
            self.go_to_jump_anim()
            return

        # When you jump (simple version)
        # Change direction
        if self.new_jump and self.anim_state[:13] != "JUMP_COMPLETE":
            self.go_to_change_jump_dir()

        # When you jump
        # Stop here (self.new_jump == True)
        if self.anim_state[:5] == "JUMP_" and self.new_jump:
            return

        # When you jump
        # Switch to fall animation (self.new_jump == False)
        # Also stop here (self.new_fall == True)
        if self.new_fall:
            if not ("FALL" in self.anim_state) or ("FALL_COMPLETE" in self.anim_state) and self._frame_index < 2: 
                self.anim_state = "FALL_COMPLETE_" + self.new_direction
            elif self._frame_index == 2 and self.anim_state[:13] == "FALL_COMPLETE":
                self.anim_state = "FALL_" + self.new_direction
            return
        elif self.old_fall:
            self.anim_state = "IDLE_" + self.new_direction
            return

        
        if self.fog_sprite.effect_name != "WALK_FOG":
            self.fog_sprite.change_effect("WALK_FOG")


        if self.anim_state[:7] == "TO_THE_":
            if self._frame_index == 2:
                self.anim_state = "WALK_" + self.new_direction
            return
  
        if "RIGHT" in self.anim_state and self.moving_left and not self.moving_right:
            self.anim_state = "TO_THE_LEFT"
            return
        elif "LEFT" in self.anim_state and self.moving_right and not self.moving_left:
            self.anim_state = "TO_THE_RIGHT"
            return


        if self.moving_left and not self.moving_right:
            self.anim_state = "WALK_LEFT"
            return
        elif self.moving_right and not self.moving_left:
            self.anim_state = "WALK_RIGHT"
            return

        if self.anim_state[:5] == "BREAK":
            if self.duration_moving == 0:
                if self.anim_state[len(self.anim_state)-1] == "1":
                    self.anim_state = "BREAK_" + self.new_direction + "_02"
                    self._frame_index = 0
                elif self._frame_index == 2:
                    self.anim_state = "IDLE_EDGE_" + self.new_direction
            return
      
        if self.anim_state[:4] != "IDLE" and self.anim_state[:5] != "BREAK":
            if self.anim_state == "WALK_LEFT":
                self.anim_state = "BREAK_LEFT_01"          
            elif self.anim_state == "WALK_RIGHT":
                self.anim_state = "BREAK_RIGHT_01"
            return

                
    def update_player_movement(self):

        if self.anim_state == "DEATH":
            return

        self.update_player_animation()
        self.moving_left_old = self.moving_left
        self.moving_right_old = self.moving_right

        self.update_player_jump()

        if ((not self.moving_left and not self.moving_right) or (self.moving_left and self.moving_right)) and(
            self.anim_state[:5] != "BREAK"):
            self.duration_moving = 0
            
        if self.new_direction != self.old_direction:
            self.duration_moving = 0
            self.old_direction = self.new_direction

        if self.duration_moving < self.duration_moving_max and self.anim_state[:5] != "BREAK":
            self.duration_moving += 1
        elif self.duration_moving > 0:
            self.duration_moving -= 0.5
        
        if (self.moving_left and not self.moving_right) or self.anim_state[:10] == "BREAK_LEFT":

            step = self.moving_x_pattern[int(self.duration_moving)]
            test = True
            
            while test:
                if step < 0:
                    test = False
                if self.can_move(step*(-1)):
                    self.x -= step
                    self.rect[0] -= step
                    self.new_direction = "LEFT"
                    test = False
                else:
                    step -= 1
                

        if (self.moving_right and not self.moving_left) or self.anim_state[:11] == "BREAK_RIGHT":

            step = self.moving_x_pattern[int(self.duration_moving)]
            test = True
            
            while test:
                if step < 0:
                    test = False
                if self.can_move(step):
                    self.x += step
                    self.rect[0] += step
                    self.new_direction = "RIGHT"
                    test = False
                else:
                    step -= 1
                    

    def can_move(self, step):
        for sprite in self.sprite_list_collidable:
            if sprite.collidable:
                if (sprite.x + sprite.rect[2]) >= (self.rect[0] + step) and (sprite.x) <= (self.rect[0] + self.rect[2] + step):
                    if (sprite.y + sprite.rect[3]) >= (self.rect[1]) and (sprite.y) <= (self.rect[1] + self.rect[3]):
                        return False
        return True
    
        
    def can_fall(self, step):
        for sprite in self.sprite_list_collidable:
            if sprite.collidable:
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
        
        if key == window.key.Q:
            self.moving_left = True
        if key == window.key.D:
            self.moving_right = True
        if key == window.key.F5:
            self.reset_position()
            
        if key == window.key.SPACE:
            self.want_to_jump = True
            
        if key == window.key.NUM_1:
            self.go_colorfilter_new = True
            self.go_colorfilter_red = not self.go_colorfilter_red
            self.go_colorfilter_green = False
            self.go_colorfilter_blue = False
        if key == window.key.NUM_2:
            self.go_colorfilter_new = True
            self.go_colorfilter_red = False
            self.go_colorfilter_green = not self.go_colorfilter_green
            self.go_colorfilter_blue = False
        if key == window.key.NUM_3:
            self.go_colorfilter_new = True
            self.go_colorfilter_red = False
            self.go_colorfilter_green = False
            self.go_colorfilter_blue = not self.go_colorfilter_blue
            
        if key == window.key.ENTER or key == window.key.RETURN:
            self.want_to_action = True

            
    def key_released(self, key, modifiers):
        
        if key == window.key.Q:
            self.moving_left = False
        if key == window.key.D:
            self.moving_right = False
        if key == window.key.SPACE:
            self.want_to_jump = False
        if key == window.key.ENTER or key == window.key.RETURN:
            self.want_to_action = False


    def go_to_complete_jump_anim(self):
        if self.new_direction == "RIGHT":
            self.anim_state = "JUMP_COMPLETE_RIGHT"
        else:
            self.anim_state = "JUMP_COMPLETE_LEFT"
        self.fog_sprite.change_effect("JUMP_FOG")


    def go_to_jump_anim(self):
        if self.new_direction == "RIGHT":
            self.anim_state = "JUMP_RIGHT"
        else:
            self.anim_state = "JUMP_LEFT"


    def go_to_change_jump_dir(self):
        if self.new_direction == "RIGHT":
            self.anim_state = "JUMP_RIGHT"
        else:
            self.anim_state = "JUMP_LEFT"

            
    def anti_aliasied_texture(self, img):
        
        texture = img.get_texture()
        glBindTexture(texture.target, texture.id)
        glTexParameteri(texture.target,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        glBindTexture(texture.target,0)
