#Import basic librairies
import pyglet
from pyglet.gl import *
#Import personal packages
from constants import constants

class Effect_sprite(pyglet.sprite.Sprite):
    

    def __init__(self, z, effect_name, my_batch, target):

        self.target = target

        self.offset_x = -32
        self.offset_y = 0
        self.z = z
        self.effect_z = pyglet.graphics.OrderedGroup(self.z)
        self.effect_name = effect_name

        self.my_image_empty = self.get_empty_image()
        
        self.my_animation = {}

        self.my_animation["WALK_FOG"] = {}
        self.my_animation["WALK_FOG"]["RIGHT"] = self.get_animation("WALK_FOG", "RIGHT")
        self.my_animation["WALK_FOG"]["LEFT"] = self.get_animation("WALK_FOG", "LEFT")

        self.my_animation["JUMP_FOG"] = self.get_animation("JUMP_FOG", "")
            
        self.previous_target_state = ""
        
        super(Effect_sprite, self).__init__(img=self.my_image_empty, x=0, y=0, batch=my_batch, group=self.effect_z)

        self.run = False
        self.launched = False


    def change_effect(self, new_effect_name):

        self.image = self.my_image_empty
        self.run = False
        self.effect_name = new_effect_name
   
              
    def update(self, target_state):

        if self.effect_name == "WALK_FOG":
            self.update_walk_fog(target_state)

        elif self.effect_name == "JUMP_FOG":
            self.update_jump_fog(target_state)


    def update_jump_fog(self, target_state):

        if not self.run:
            self.image = self.my_animation["JUMP_FOG"]
            self.run = True

        self.previous_target_state = target_state       


    def update_walk_fog(self, target_state):
        
        if target_state[:4] == "WALK":
            self.run = True
            if self.previous_target_state != target_state:
                if target_state == "WALK_RIGHT":
                    self.image = self.my_animation["WALK_FOG"]["RIGHT"]
                    self.offset_x = -22
                elif target_state == "WALK_LEFT":
                    self.offset_x = 22
                    self.image = self.my_animation["WALK_FOG"]["LEFT"]
        else:
            self.image = self.my_image_empty
            self.run = False
            
        if self.run:
            self.x = self.target.x + self.offset_x
            self.y = self.target.y + self.offset_y  

        self.previous_target_state = target_state
        
        
    def get_empty_image(self):
        
        return pyglet.image.load(constants.PATH_EFFECT + "000" + ".png")
    

    def get_animation_loaded(self, effect_name, direction):

        return self.anim_effect_list[effect_name][direction]
    

    def get_animation(self, effect_name, side):

        x, y, w, h, my_loop, my_nb_frame, my_speed = self.get_anim_sequence(effect_name)

        if side == "LEFT":
            y += constants.SPRITE_Y
        effect_complete_image = pyglet.image.load(constants.PATH_EFFECT + "003" + ".png")
        effect_region = effect_complete_image.get_region(x, y, w, h)
        effect_sequence = pyglet.image.ImageGrid(effect_region, 1, my_nb_frame)

        for img in effect_sequence:
            self.anti_aliasied_texture(img)
        effect_animation = pyglet.image.Animation.from_image_sequence(effect_sequence, my_speed, my_loop)

        return effect_animation


    def get_anim_sequence(self, state):

        if state == "WALK_FOG": #OK
            return 0, 0*constants.SPRITE_Y, 12*constants.SPRITE_X, constants.SPRITE_Y, True, 12, 0.05

        if state == "JUMP_FOG": #OK
            return 0, 3*constants.SPRITE_Y, 7*constants.SPRITE_X, constants.SPRITE_Y, False, 7, 0.03


    def anti_aliasied_texture(self, img):
        
        texture = img.get_texture()
        glBindTexture(texture.target, texture.id)
        glTexParameteri(texture.target,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        glBindTexture(texture.target,0)
