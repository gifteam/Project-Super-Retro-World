#Import basic librairies
import pyglet
from pyglet.gl import *
import time
import pygame
#Import personal packages
from constants import constants
from classes import Piece

class Salle_de_theatre(pyglet.window.Window):
    
    def __init__(self):

        self.set_the_project_name()
        self.set_the_scene_name()
        self.set_the_pygame_music_mixer()
        self.set_the_window()
   
        self.dt = 0
        self.Piece_de_theatre = Piece.Piece_de_theatre(self, self.scene)

        
    def on_draw(self):

        pyglet.clock.tick()
        self.clear()
        self.Piece_de_theatre.Scene_de_theatre.batch.draw()

        
    def update(self, dt):

        self.Piece_de_theatre.update(dt)

            
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
                    
            self.close()
            
    
    def on_key_release(self, key, modifiers):

        self.Piece_de_theatre.key_released(key, modifiers)


    def set_the_project_name(self):

        print("#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#")
        print("#         PROJECT SUPER RETRO WORLD by [The Missing Part]         #")
        print("#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#")
        print("Hello and welcome to game")
        print("Main purpose: check animation and event states")
        print("")    


    def set_the_scene_name(self):

        self.scene = "GAME_START"


    def set_the_pygame_music_mixer(self):

        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.mixer.init()
        pygame.init()


    def set_the_window(self):

        platform = pyglet.window.get_platform()
        display = platform.get_default_display()
        self.screens = display.get_screens()    
        screen = display.get_default_screen()
        self.window_width = int(screen.width/2)
        self.window_height = int(screen.height/2)

        print("Window dimension:", self.window_width, "x", self.window_height)
        
        self.theatre_dim = [self.window_width, self.window_height]
        template = pyglet.gl.Config(double_buffer=True)
        config = self.screens[0].get_best_config(template)

        super().__init__(self.window_width,
                         self.window_height,
                         caption=constants.GAME_TITLE,
                         vsync = False,
                         fullscreen = False,
                         resizable = False,
                         config=config)

        self.set_mouse_visible(False)
        self.set_fullscreen(fullscreen=False, screen = self.screens[0])
