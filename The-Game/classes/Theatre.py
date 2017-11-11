#Import basic librairies
import pyglet
from pyglet.gl import *
import pygame
#Import personal packages
from constants import constants
from classes import Piece

class Salle_de_theatre(pyglet.window.Window):
    
    def __init__(self):

        print("#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#")
        print("#         PROJECT SUPER RETRO WORLD by [The Missing Part]         #")
        print("#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#")
        print("Hello and welcome to the event test")
        print("Main purpose: check animation and event states")
        print("")

        scene = "GAME_START"

        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.mixer.init()
        pygame.init()

        platform = pyglet.window.get_platform()
        display = platform.get_default_display()
        self.screens = display.get_screens()    
        screen = display.get_default_screen()
        self.window_width = int(screen.width/2)
        self.window_height = int(screen.height/2)
        self.theatre_dim = [self.window_width, self.window_height]
        #print(screen_width, screen_height)
        #print(screen_width/2, screen_height/2)
        #self.screens[0].get_closest_mode(640,480)
        template = pyglet.gl.Config(double_buffer=True)#alpha_size=8)
        config = self.screens[0].get_best_config(template)
        #context = config.create_context(None)

        super().__init__(self.window_width,
                         self.window_height,
                         caption=constants.GAME_TITLE,
                         vsync = False,
                         fullscreen = False,
                         resizable = False,
                         config=config)
                         #context=context)
                         #screen = screens[1])
        
        #self.set_mouse_visible(False)
        #self.set_fullscreen(fullscreen=True, screen = self.screens[0])
        
        self.dt = 0
        self.Piece_de_theatre = Piece.Piece_de_theatre(self, scene)
        

    def on_draw(self):

        pyglet.clock.tick()
        self.clear()
        self.Piece_de_theatre.Scene_de_theatre.batch.draw()

            
    def on_key_press(self, key, modifiers):
        
        self.Piece_de_theatre.key_pressed(key, modifiers)

        if key == pyglet.window.key.F4:
            if self.fullscreen is True:
                self.set_mouse_visible(True)
                self.set_fullscreen(fullscreen=False, screen = self.screens[0])
            else:
                self.set_mouse_visible(False)
                self.set_fullscreen(fullscreen=True, screen = self.screens[0])

        if key == pyglet.window.key.ESCAPE:
            self.set_mouse_visible(True)
            self.set_fullscreen(fullscreen=False, screen = self.screens[0])

            for spr_i in self.Piece_de_theatre.Scene_de_theatre.sprite_list:
                if spr_i.type_fps:
                    spr_i.fps_file.close()
                    
            self.close()
            

    
    def on_key_release(self, key, modifiers):
        self.Piece_de_theatre.key_released(key, modifiers)

        
    def update(self, dt):

        self.Piece_de_theatre.update(dt)
        
