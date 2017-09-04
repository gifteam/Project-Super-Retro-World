#Import basic librairies
import pyglet
from pyglet.gl import *
#Import personal packages
from constants import constants

class Ball_sprite(pyglet.sprite.Sprite):

    def __init__(self, x, y, z, my_batch, target):

        self.target = target

        self.z = z
        
        self.sprite_list_collidable = []
        self.ball_z = pyglet.graphics.OrderedGroup(self.z)
        self.path = constants.PATH_CHARA + "006" + ".png"
        
        self.my_image = pyglet.image.load(self.path)
        self.my_image_list = pyglet.image.ImageGrid(self.my_image, 1, 2)
        for img in self.my_image_list:
            self.anti_aliasied_texture(img)
            texture = img.get_texture()
            texture.anchor_x = int(img.width/2)
            texture.anchor_y = int(img.height/2)

        super(Ball_sprite, self).__init__(img=self.my_image_list[0], x=-100, y=-100, batch=my_batch, group=self.ball_z)

        self.activated = False
        self.can_bounce = False
        self.frames = 0
        self.frames_max = 150
        self.init_speed = 0
        self.rect = [0,0,10,10]
        
        self.launching_y_pattern = [int((500 - x)/100) for x in range(0,500,25)]
        self.launching_y_pattern_max = len(self.launching_y_pattern) - 1
        self.launching_y_pattern_index = 0
        self.falling_y_pattern = [int((x)/100) for x in range(50,900,50)]
        self.falling_y_pattern_max = len(self.falling_y_pattern) - 1
        self.falling_y_pattern_index = 0

##        self.clock_z = pyglet.graphics.OrderedGroup(self.z+10)
##        self.clock_path = constants.PATH_EFFECT + "001" + ".png"
##        self.clock_image = pyglet.image.load(self.clock_path)
##        self.anti_aliasied_texture(self.clock_image)
##        self.clock_nb_frames = int(self.clock_image.width/constants.SPRITE_X)
##        self.clock_image_list = pyglet.image.ImageGrid(self.clock_image, 1, self.clock_nb_frames)
##        self.clock_index = 0
##        self.clock_index_max = len(self.clock_image_list)
##        self.clock_sprite = pyglet.sprite.Sprite(img=self.clock_image_list[self.clock_index], x=-100, y=-100, batch=my_batch, group=self.clock_z)        

        self.desactivation()
              
    def update(self):

        if self.activated:
            self.frames += 1

            self.rotation += int((1-(self.frames/self.frames_max))*55)
            if self.speed > 0:
                step = 1
            else:
                step = -1
            for i in range(abs(self.speed)):
                if self.can_x(step):
                    self.x += step
                    self.rect[0] += step
                else:
                    self.speed = int(self.speed*(-0.5))
                    break
                    
            if self.launching_y_pattern_index < self.launching_y_pattern_max:
                step = 1
                for i in range(self.launching_y_pattern[self.launching_y_pattern_index]):
                    if self.can_y(step):
                        self.y += step
                        self.rect[1] += step
                    else:
                        self.launching_y_pattern_index = self.launching_y_pattern_max
                        self.falling_y_pattern_index = 0
                        break       
                self.launching_y_pattern_index += 1
            else: 
                step = -1
                for i in range(self.falling_y_pattern[min(self.falling_y_pattern_max,self.falling_y_pattern_index)]):
                    if self.can_y(step):
                        self.y += step
                        self.rect[1] += step 
                    else:
                        self.launching_y_pattern_index = 0
                        self.falling_y_pattern_index = 0
                        break  
                self.falling_y_pattern_index += 1


            if self.y < - 16:
                self.frames = self.frames_max
            if self.frames == self.frames_max:
                self.desactivation()


    def can_x(self, step):
        for sprite in self.sprite_list_collidable:
            if (sprite.x + sprite.rect[2]) >= (self.rect[0] + step) and (sprite.x) <= (self.rect[0] + self.rect[2] + step):
                if (sprite.y + sprite.rect[3]) >= (self.rect[1]) and (sprite.y) <= (self.rect[1] + self.rect[3]):
                    return False
        return True


    def can_y(self, step):
        for sprite in self.sprite_list_collidable:
            if (sprite.x + sprite.rect[2]) >= (self.rect[0]) and (sprite.x) <= (self.rect[0] + self.rect[2]):
                if (sprite.y + sprite.rect[3]) >= (self.rect[1] + step) and (sprite.y) <= (self.rect[1] + self.rect[3] + step):
                    return False
        return True
    
     
    def activation(self, target, sprite_list_collidable):

        self.sprite_list_collidable = sprite_list_collidable
        self.x = target.x+16
        self.y = target.y+16
        self.rect[0] = self.x + 3
        self.rect[1] = self.y + 3
        self.image = self.my_image_list[0]
        self.init_speed = target.moving_x_pattern[int(target.duration_moving)]
        
        if "LEFT" in target.anim_state:
            self.speed = (-1) * (7 + abs(self.init_speed))
        else:
            self.speed = (7 + abs(self.init_speed))

        self.frames = 0 
        self.launching_y_pattern_index = 0
        self.falling_y_pattern_index = 0

        self.can_bounce = True
        self.activated = True


    def desactivation(self):
        
        self.x = -100
        self.y = -100
        self.rect[0] = self.x + 3
        self.rect[1] = self.y + 3
        self.speed = 0
        self.frames = 0
        self.can_bounce = False
        self.activated = False


    def anti_aliasied_texture(self, img):
        
        texture = img.get_texture()
        glBindTexture(texture.target, texture.id)
        glTexParameteri(texture.target,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        glBindTexture(texture.target,0)
