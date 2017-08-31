#Import basic librairies
import pyglet
#Import personal packages
from constants import constants

class New_sprite(pyglet.sprite.Sprite):

    def __init__(self, img, x, y, z, my_batch, my_group, spr_type, collidable, my_scene):

        super(New_sprite, self).__init__(img=img, x=x, y=y, batch=my_batch, group=my_group)

        #global info - - - - - - - - - - - - - - - - -
        self.type_event = False
        self.type_base = False
        self.type_back = False
        self.type_front = False
        self.type_fps = False
        self.type_tile = False
        self.type = spr_type
        if spr_type[:5] == "event":
            self.type_event = True
        elif spr_type == "base":
            self.type_base = True
        elif spr_type == "back":
            self.type_back = True
        elif spr_type == "front":
            self.type_front = True
        elif spr_type[:3] == "fps":
            self.type_fps = True
        elif spr_type[:3] == "tile":
            self.type_tile = True
        self.z = z
        self.x_origin = x
        self.my_scene = my_scene
        #collisions - - - - - - - - - - - - - - - - -
        self.sprite_list = []
        self.collidable = collidable
        self.rect = [0,0,32,32]
        #hud - - - - - - - - - - - - - - - - - - - - -
        number_sheet = constants.PATH_HUD + "008" + ".png"
        number_sheet_image = pyglet.image.load(number_sheet)
        self.number_list = pyglet.image.ImageGrid(number_sheet_image, 1, 10)
        self.fps_refresh = 0
        self.fps_refresh_rate = 10
        # - - - - - - - - - - - - - - - - - - - - - - 

    def update_base_front(self):

        if self.my_scene != "LEVEL_SELECT":
            self.x = int(self.sprite_list[0].x - constants.SCREEN_X/2)
            self.y = 0


    def update_back(self):

        if self.my_scene != "LEVEL_SELECT":
            self.x = int(self.x_origin + self.sprite_list[0].x - constants.SCREEN_X/2 - self.sprite_list[0].x*self.z/10)
            self.y = 0


    def update_fps(self):

        ID = int(self.type[len(self.type)-1])
        
        if self.fps_refresh >= self.fps_refresh_rate:
            self.fps_refresh = 0
            fps = str(int(pyglet.clock.get_fps()))
            fps = "0" * (4-len(fps)) + fps
            if len(fps) > 4:
                fps = "9999"
            num = int(fps[ID])
            
            self.image = self.number_list[num]
        else:
            self.fps_refresh += 1

        if self.my_scene != "LEVEL_SELECT": 
            self.x = int(self.sprite_list[0].x - constants.SCREEN_X/2) + ID * 7 + 10
            self.y = 480 - 20
            

    def update(self, sprite_list, dt):

        self.sprite_list = sprite_list
        
        if self.type_event:
            pass
        elif self.type_base or self.type_front:
            self.update_base_front()
        elif self.type_back:
            self.update_back()
        elif self.type_tile:
            pass
        elif self.type_fps:
            self.update_fps()
