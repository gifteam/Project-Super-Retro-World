#Import basic librairies
import pyglet
from pyglet import window
from pyglet.gl import *
#Import personal packages
from constants import constants
from classes import Event, Ball, Effect

class Player_sprite(pyglet.sprite.Sprite):

    def __init__(self, x, y, z, my_batch, my_group, spr_type, collidable, my_scene, my_event_list, my_event):

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
        #ball - - - - - - - - - - - - - - - - - - - -
        self.want_to_ball = False
        self.ball = Ball.Ball_sprite(x, y, z-1, my_batch, self)
        #run + jump effect - - - - - - - - - - - - - -
        self.fog_sprite = Effect.Effect_sprite(z-1, "WALK_FOG", my_batch, self)
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

        self.all_anim_sequences["WALK_RIGHT"] = self.get_new_sequence("WALK_RIGHT")
        self.all_anim_sequences["WALK_LEFT"] = self.get_new_sequence("WALK_LEFT")
        self.all_anim_sequences["IDLE_RIGHT"] = self.get_new_sequence("IDLE_RIGHT")
        self.all_anim_sequences["IDLE_LEFT"] = self.get_new_sequence("IDLE_LEFT")
        self.all_anim_sequences["IDLE_RIGHT"] = self.get_new_sequence("IDLE_RIGHT")

        self.all_anim_sequences["BREAK_RIGHT_01"] = self.get_new_sequence("BREAK_RIGHT_01")
        self.all_anim_sequences["BREAK_LEFT_01"] = self.get_new_sequence("BREAK_LEFT_01")
        self.all_anim_sequences["BREAK_RIGHT_02"] = self.get_new_sequence("BREAK_RIGHT_02")
        self.all_anim_sequences["BREAK_LEFT_02"] = self.get_new_sequence("BREAK_LEFT_02")

        self.all_anim_sequences["TO_THE_RIGHT"] = self.get_new_sequence("TO_THE_RIGHT")
        self.all_anim_sequences["TO_THE_LEFT"] = self.get_new_sequence("TO_THE_LEFT")
        
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
        
        if state == "WALK_RIGHT": #OK
            return constants.PLAYER_STYLE[self.my_scene], 0, 0*constants.SPRITE_Y, 12*constants.SPRITE_X, constants.SPRITE_Y, True, 12, 0.05
        if state == "WALK_LEFT": #OK
            return constants.PLAYER_STYLE[self.my_scene], 0, 1*constants.SPRITE_Y, 12*constants.SPRITE_X, constants.SPRITE_Y, True, 12, 0.05
        if state == "IDLE_RIGHT": #OK
            return constants.PLAYER_STYLE[self.my_scene], 0, 2*constants.SPRITE_Y, 1*constants.SPRITE_X, constants.SPRITE_Y, False, 1, 1
        if state == "IDLE_LEFT": #OK
            return constants.PLAYER_STYLE[self.my_scene], 0, 3*constants.SPRITE_Y, 1*constants.SPRITE_X, constants.SPRITE_Y, False, 1, 1
        
        if state == "BREAK_RIGHT_01": #OK
            return constants.PLAYER_STYLE[self.my_scene], 0, 4*constants.SPRITE_Y, 4*constants.SPRITE_X, constants.SPRITE_Y, False, 4, 0.04
        if state == "BREAK_LEFT_01": #OK
            return constants.PLAYER_STYLE[self.my_scene], 0, 5*constants.SPRITE_Y, 4*constants.SPRITE_X, constants.SPRITE_Y, False, 4, 0.04
        if state == "BREAK_RIGHT_02": #OK
            return constants.PLAYER_STYLE[self.my_scene], 4*constants.SPRITE_X, 4*constants.SPRITE_Y, 3*constants.SPRITE_X, constants.SPRITE_Y, False, 3, 0.04
        if state == "BREAK_LEFT_02": #OK
            return constants.PLAYER_STYLE[self.my_scene], 4*constants.SPRITE_X, 5*constants.SPRITE_Y, 3*constants.SPRITE_X, constants.SPRITE_Y, False, 3, 0.04

        if state == "TO_THE_RIGHT": #OK
            return constants.PLAYER_STYLE[self.my_scene], 0, 6*constants.SPRITE_Y, 3*constants.SPRITE_X, constants.SPRITE_Y, False, 3, 0.04
        if state == "TO_THE_LEFT": #OK
            return constants.PLAYER_STYLE[self.my_scene], 0, 7*constants.SPRITE_Y, 3*constants.SPRITE_X, constants.SPRITE_Y, False, 3, 0.04    

        
    def update(self, sprite_list, dt):

        self.dt = dt
        self.update_player()
        #print(self._frame_index)


    def update_player(self):

        self.update_player_gravity()
        self.update_player_movement()
        self.update_event()
        self.update_death()
        self.update_ball()
        self.update_anim_sequence()
        self.update_effects()


    def update_effects(self):

        self.fog_sprite.update(self.anim_state)

        
    def update_ball(self):
        
        if self.want_to_ball:
            
            if not self.ball.activated:
                self.ball.activation(self, self.sprite_list_collidable)

        self.ball.update()

            
    def update_death(self):

        if self.y < 0 - constants.SPRITE_Y:
            self.reset_position()
            #self.my_event.action(-1)
            
         
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
            print(self.anim_state)

            
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
                    self.anim_state = "IDLE_" + self.new_direction
            return

                
        if self.anim_state[:4] != "IDLE" and self.anim_state[:5] != "BREAK":
            if self.anim_state == "WALK_LEFT":
                self.anim_state = "BREAK_LEFT_01"          
            elif self.anim_state == "WALK_RIGHT":
                self.anim_state = "BREAK_RIGHT_01"
            return
        
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
            step = -1
            for i in range(self.moving_x_pattern[int(self.duration_moving)]):
                if self.can_move(step):
                    self.x += step
                    self.rect[0] += step
                    self.new_direction = "LEFT"
            
        if (self.moving_right and not self.moving_left) or self.anim_state[:11] == "BREAK_RIGHT":
            step = 1
            for i in range(self.moving_x_pattern[int(self.duration_moving)]):
                if self.can_move(step):
                    self.x += step
                    self.rect[0] += step
                    self.new_direction = "RIGHT"


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
        
        if key == window.key.Q:
            self.moving_left = True
        if key == window.key.D:
            self.moving_right = True
        if key == window.key.F5:
            self.reset_position()
        if key == window.key.SPACE:
            self.want_to_jump = True
        if key == window.key.NUM_0:
            self.want_to_ball = True
        if key == window.key.ENTER or key == window.key.RETURN:
            self.want_to_action = True

            
    def key_released(self, key, modifiers):
        
        if key == window.key.Q:
            self.moving_left = False
        if key == window.key.D:
            self.moving_right = False
        if key == window.key.SPACE:
            self.want_to_jump = False
        if key == window.key.NUM_0:
            self.want_to_ball = False
        if key == window.key.ENTER or key == window.key.RETURN:
            self.want_to_action = False


    def anti_aliasied_texture(self, img):
        
        texture = img.get_texture()
        glBindTexture(texture.target, texture.id)
        glTexParameteri(texture.target,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        glBindTexture(texture.target,0)
