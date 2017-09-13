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
        self.my_animation = []
        if self.effect_name == "WALK_FOG":
            self.my_animation.append(self.get_animation("RIGHT"))
            self.my_animation.append(self.get_animation("LEFT"))
        else:
            self.my_animation = self.get_animation()
            
        self.previous_target_state = ""
        
        super(Effect_sprite, self).__init__(img=self.my_image_empty, x=0, y=0, batch=my_batch, group=self.effect_z)

        self.run = False
        self.launched = False
        
              
    def update(self, target_state):

        if self.effect_name == "WALK_FOG":
            if target_state[:4] == "WALK":
                self.run = True
                if self.previous_target_state != target_state:
                    if target_state == "WALK_RIGHT":
                        self.image = self.my_animation[0]
                        self.offset_x = -22
                    elif target_state == "WALK_LEFT":
                        self.offset_x = 22
                        self.image = self.my_animation[1]
            else:
                self.image = self.my_image_empty
                self.run = False
                
        if self.run:
            self.x = self.target.x + self.offset_x
            self.y = self.target.y + self.offset_y  

        self.previous_target_state = target_state

            
    def get_empty_image(self):
        
        return pyglet.image.load(constants.PATH_EFFECT + "000" + ".png")
    

    def get_animation(self, side = ""):

        x, y, w, h, loop, self.nb_frame, speed = self.get_anim_sequence(self.effect_name)
        if side == "LEFT":
            y += constants.SPRITE_Y
        effect_complete_image = pyglet.image.load(constants.PATH_EFFECT + "003" + ".png")
        effect_region = effect_complete_image.get_region(x, y, w, h)
        effect_sequence = pyglet.image.ImageGrid(effect_region, 1, self.nb_frame)
        for img in effect_sequence:
            self.anti_aliasied_texture(img)
        effect_animation = pyglet.image.Animation.from_image_sequence(effect_sequence, speed, loop)
        return effect_animation


    def get_anim_sequence(self, state):
        
        if state == "WALK_FOG": #OK
            return 0, 0*constants.SPRITE_Y, 12*constants.SPRITE_X, constants.SPRITE_Y, True, 12, 0.05


    def anti_aliasied_texture(self, img):
        
        texture = img.get_texture()
        glBindTexture(texture.target, texture.id)
        glTexParameteri(texture.target,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        glBindTexture(texture.target,0)
