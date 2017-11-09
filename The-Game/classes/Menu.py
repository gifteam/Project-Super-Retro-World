#Import basic librairies
import pyglet
from pyglet import window
from pyglet.gl import *
#Import personal packages
from constants import constants
from classes import Sprite, Player, Event, Deco

class Menu(object):

    def __init__(self, my_scene_name, my_scene, my_batch):

        #global - - - - - - - - - - - - - - 
        self.scene_name = my_scene_name
        self.scene = my_scene
        self.batch = my_batch
        #menu animation - - - - - - - - - - 
        self.menu_sprite = []
        self.enter_menu_timer = 0
        self.menu_enter_complete = False
        self.menu_name = ""
        #menu management - - - - - - - - - 
        self.my_key_pressed = None
        self.menu_state = ""
        self.previous_menu_state = ""
        self.menu_list_position = 0
        self.menu_list_position_max = 0

        
    def init_menu(self, menu_name):

        self.menu_name = menu_name
        if self.menu_name == "GAME_START":
            self.init_menu_GAME_START()
        

    def enter_menu(self):

        if self.menu_name == "GAME_START":
            self.enter_menu_GAME_START()


    def update(self):
        
        if self.menu_enter_complete:
            self.update_menu()
        else:
            self.enter_menu()

        self.update_camera()


    def key_pressed(self, key):

        if not self.menu_enter_complete:
            self.menu_enter_complete = True
            self.skip_entering()

        else:
            self.my_key_pressed = key


    def update_menu(self):
        
        if self.menu_name == "GAME_START":
            self.update_menu_GAME_START()


    def exit_menu(self):
        pass


    def skip_entering(self):

        if self.menu_name == "GAME_START":
            self.skip_entering_GAME_START()
 

    # - - - - - - - - - - - - - - - - - - - -
    #
    # MENU GAME START
    #
    # - - - - - - - - - - - - - - - - - - - - 

    def init_menu_GAME_START(self):

        src_list = []
        
        src_list.append(constants.PATH_LABEL + "000.png")
        src_list.append(constants.PATH_LABEL + "001.png")
        src_list.append(constants.PATH_LABEL + "002.png")
        src_list.append(constants.PATH_LABEL + "003.png")
        src_list.append(constants.PATH_LABEL + "004.png")
        src_list.append(constants.PATH_LABEL + "005.png")
        src_list.append(constants.PATH_LABEL + "006.png")
        src_list.append(constants.PATH_LABEL + "007.png")
        src_list.append(constants.PATH_LABEL + "010.png")
        src_list.append(constants.PATH_LABEL + "011.png")

        sprt_list = []
        for i in range(len(src_list)):
            z_grp = pyglet.graphics.OrderedGroup(len(src_list) - 1 - i)
            img_aa = pyglet.image.load(src_list[i])
            self.anti_aliasied_texture(img_aa)
            x = int((self.scene.my_theatre.theatre_dim[0] - img_aa.width)/2)
            y = int((self.scene.my_theatre.theatre_dim[1] - img_aa.height)/2)

            if i >= 3 and i <= 6:
                y -= 100
                
            elif i == 7:
                x = sprt_list[len(sprt_list)-1].x - 16
                y = sprt_list[len(sprt_list)-1].y + sprt_list[len(sprt_list)-1].image.height - img_aa.height

            elif i == 9:
                x = self.scene.my_theatre.theatre_dim[0] - img_aa.width
                y = 0
                
            sprt_list.append(pyglet.sprite.Sprite(img = img_aa, x=x, y=y, batch=self.batch, group=z_grp))

        self.menu_sprite = []
        self.menu_sprite = sprt_list

        for i in range(len(self.menu_sprite)):
            self.menu_sprite[i].visible = False
        self.menu_sprite[0].visible = True
        self.menu_sprite[1].visible = True
        
        self.enter_menu_timer = 0
        self.menu_enter_complete = False
        self.menu_state = "PRESS ENTER"
        self.menu_list_position = 0
        self.menu_list_position_max = 0
        

    def enter_menu_GAME_START(self):

        self.enter_menu_timer += 1

        if self.enter_menu_timer >= 100 and self.enter_menu_timer < 200:
            if self.enter_menu_timer % 20 == 0 and self.menu_sprite[0].opacity > 5:
                self.menu_sprite[0].opacity -= 50

        if self.enter_menu_timer >= 600 and self.enter_menu_timer < 700:
            if self.enter_menu_timer % 20 == 0 and self.menu_sprite[0].opacity < 255:
                self.menu_sprite[0].opacity += 50

        if self.enter_menu_timer == 700:
            self.menu_sprite[1].visible = False
            self.menu_sprite[2].visible = True                       

        if self.enter_menu_timer >= 700 and self.enter_menu_timer < 800:
            if self.enter_menu_timer % 20 == 0 and self.menu_sprite[0].opacity > 5:
                self.menu_sprite[0].opacity -= 50

        if self.enter_menu_timer >= 900 and self.enter_menu_timer < 1000:
            if self.enter_menu_timer % 20 == 0 and self.menu_sprite[0].opacity < 255:
                self.menu_sprite[0].opacity += 50

        if self.enter_menu_timer == 1000:
            self.menu_sprite[2].visible = False
            self.menu_sprite[3].visible = True
            self.menu_sprite[8].visible = True
            self.menu_sprite[9].visible = True 

        if self.enter_menu_timer >= 1000:
            if self.enter_menu_timer % 20 == 0 and self.menu_sprite[0].opacity > 5:
                self.menu_sprite[0].opacity -= 50

        if self.enter_menu_timer > 1000 and self.menu_sprite[0].opacity == 0:
            self.menu_enter_complete = True
            self.menu_sprite[0].visible = False
            self.menu_sprite[1].visible = False
            self.menu_sprite[2].visible = False
            self.menu_sprite[3].visible = True
            self.menu_sprite[8].visible = True
            self.menu_sprite[9].visible = True 


    def skip_entering_GAME_START(self):
        
        for i in range(len(self.menu_sprite)):
            self.menu_sprite[i].visible = False
        self.menu_sprite[3].visible = True
        self.menu_sprite[8].visible = True 
       

    def update_menu_GAME_START(self):

        if self.my_key_pressed == window.key.RETURN:
            
            if self.menu_state == "PRESS ENTER":
                self.menu_state = "MAIN MENU"
                self.menu_list_position = 0
                self.menu_list_position_max = 3
            
            elif self.menu_state == "MAIN MENU":
                
                if self.menu_list_position == 0:
                    self.menu_state = "CHOOSE LEVEL"
                    self.menu_list_position = 0
                    self.menu_list_position_max = 3
                    
                elif self.menu_list_position == 1:
                    self.menu_state = "CHOOSE OPTION"
                    self.menu_list_position = 0
                    self.menu_list_position_max = 3
                    
                else:
                    self.menu_state = "QUIT GAME"
                    self.scene.my_theatre.close()

            elif self.menu_state == "CHOOSE LEVEL":
                
                if self.menu_list_position == 0:
                    self.scene.new_name = "simple"
                elif self.menu_list_position == 1:
                    self.scene.new_name = "simple"
                else:
                    self.scene.new_name = "hard"

                    
            self.my_key_pressed = None
            return
                    
                
        elif self.my_key_pressed == window.key.UP:

            self.menu_list_position -= 1
            self.menu_list_position = self.menu_list_position % self.menu_list_position_max
            self.menu_sprite[7].y = self.menu_sprite[6].y + self.menu_sprite[6].image.height - self.menu_sprite[7].image.height - self.menu_list_position*32
            self.my_key_pressed = None
            return
            
        elif self.my_key_pressed == window.key.DOWN:

            self.menu_list_position += 1
            self.menu_list_position = self.menu_list_position % self.menu_list_position_max
            self.menu_sprite[7].y = self.menu_sprite[6].y + self.menu_sprite[6].image.height - self.menu_sprite[7].image.height - self.menu_list_position*32
            self.my_key_pressed = None
            return

        elif self.my_key_pressed == window.key.ESCAPE:

            if self.menu_state == "PRESS ENTER":
                return
            
            elif self.menu_state == "MAIN MENU":
                return
                    
            elif self.menu_state == "CHOOSE LEVEL" or self.menu_state == "CHOOSE OPTION":
                self.menu_state = "MAIN MENU"
                self.menu_list_position = 0
                self.menu_list_position_max = 3

            self.my_key_pressed = None
            return

        self.update_menu_GAME_START_sprites()
        
        
    def update_menu_GAME_START_sprites(self):

        if self.menu_state != self.previous_menu_state:

            self.previous_menu_state = self.menu_state
            for i in range(len(self.menu_sprite)):
                self.menu_sprite[i].visible = False

            if self.menu_state == "PRESS ENTER":
                self.menu_sprite[3].visible = True
                self.menu_sprite[8].visible = True
                self.menu_sprite[9].visible = True 

            elif self.menu_state == "MAIN MENU":
                self.menu_sprite[4].visible = True
                self.menu_sprite[7].visible = True
                self.menu_sprite[7].y = self.menu_sprite[6].y + self.menu_sprite[6].image.height - self.menu_sprite[7].image.height - self.menu_list_position*32
                self.menu_sprite[8].visible = True
                self.menu_sprite[9].visible = True 
            
            elif self.menu_state == "CHOOSE LEVEL":
                self.menu_sprite[5].visible = True
                self.menu_sprite[7].visible = True
                self.menu_sprite[7].y = self.menu_sprite[6].y + self.menu_sprite[6].image.height - self.menu_sprite[7].image.height - self.menu_list_position*32
                self.menu_sprite[8].visible = True
                self.menu_sprite[9].visible = True 

            elif self.menu_state == "CHOOSE OPTION":
                self.menu_sprite[6].visible = True
                self.menu_sprite[7].visible = True
                self.menu_sprite[7].y = self.menu_sprite[6].y + self.menu_sprite[6].image.height - self.menu_sprite[7].image.height - self.menu_list_position*32
                self.menu_sprite[8].visible = True
                self.menu_sprite[9].visible = True 
        
    # - - - - - - - - - - - - - - - - - - - - 

    def update_camera(self):

        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        glOrtho(0, self.scene.my_theatre.theatre_dim[0], 0, self.scene.my_theatre.theatre_dim[1], 0, 1);
        

    def anti_aliasied_texture(self, img):
        
        texture = img.get_texture()
        glBindTexture(texture.target, texture.id)
        glTexParameteri(texture.target,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        glBindTexture(texture.target,0)
