#Import basic librairies
import pyglet
#Import personal packages
from constants import constants

class New_sprite(pyglet.sprite.Sprite):

    def __init__(self, img, x, y, z, l, w, my_batch, my_group, spr_type, collidable, my_scene):

        super(New_sprite, self).__init__(img=img, x=x, y=y, batch=my_batch, group=my_group)

        #global info - - - - - - - - - - - - - - - - -      
        self.type_event = False
        self.type_base = False
        self.type_back = False
        self.type_front = False
        self.type_fps = False
        self.type_tile = False
        self.type_deco = False
        self.type_event = False
        self.type_textbox = False
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
        elif spr_type[:4] == "tile":
            self.type_tile = True
        elif spr_type[:4] == "deco":
            self.type_deco = True
        elif spr_type == "textbox":
            self.type_textbox = True
            self.activation_textbox = False
            
        self.z = z
        self.x_origin = x
        self.my_scene = my_scene
        #collisions - - - - - - - - - - - - - - - - -
        self.sprite_list = []
        self.player_sprite = None
        self.collidable = collidable
        self.rect = [x, y, l, w]
        #load - - - - - - - - - - - - - - - - - - - -
        self.my_image_origin = self.image
        self.my_image_empty = pyglet.image.load(constants.PATH_EFFECT + "000" + ".png")
        #hud - - - - - - - - - - - - - - - - - - - - -
        number_sheet = constants.PATH_HUD + "008" + ".png"
        number_sheet_image = pyglet.image.load(number_sheet)
        self.number_list = pyglet.image.ImageGrid(number_sheet_image, 1, 10)
        self.fps_refresh = 0
        self.fps_refresh_rate = 10
        # - - - - - - - - - - - - - - - - - - - - - - 

    def get_rect(self):
        return self.rect

    def update_base_front(self):

        if self.my_scene != "LEVEL_SELECT":
            self.x = int(self.player_sprite.x - constants.SCREEN_X/2)
            self.y = 0


    def update_back(self):

        if self.my_scene != "LEVEL_SELECT":
            self.x = int(self.x_origin + self.player_sprite.x - constants.SCREEN_X/2 - self.player_sprite.x*self.z/10)
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
            self.x = int(self.player_sprite.x - constants.SCREEN_X/2) + ID * 7 + 10
            self.y = 480 - 20
            

    def update(self, sprite_list, dt, target_load):

        self.player_sprite = target_load

        #determine if the sprite must be drawn or not
        if self.type_tile or self.type_deco:
            
            self.visible = True
            if (self.rect[0] + self.rect[2] < self.player_sprite.x - constants.SCREEN_X/2) or (
                self.rect[0] > self.player_sprite.x + constants.SCREEN_X/2):
                self.visible = False

            return
        

        if self.type_tile:
            pass
        
        elif self.type_event:
            pass

        elif self.type_base or self.type_front:
            self.update_base_front()
            
        elif self.type_back:
            self.update_back()
        
        elif self.type_fps:
            self.update_fps()

        elif self.type_textbox:
            if self.activation_textbox:
                self.opacity = 255
            else:
                self.opacity = 0
