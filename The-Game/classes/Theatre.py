#Import basic librairies
import pyglet
from pyglet.gl import *
#Import personal packages
from constants import constants
from classes import Piece

class Salle_de_theatre(pyglet.window.Window):
    
    def __init__(self):

        platform = pyglet.window.get_platform()
        display = platform.get_default_display()
        self.screens = display.get_screens()
        #self.screens[0].get_closest_mode(640,480))
        #template = pyglet.gl.Config(double_buffer=True)#alpha_size=8)
        #config = self.screens[0].get_best_config(template)
        #context = config.create_context(None)

        super().__init__(constants.SCREEN_X,
                         constants.SCREEN_Y,
                         caption=constants.GAME_TITLE,
                         vsync = True,
                         fullscreen = False,
                         resizable = True)
                         #config=config,
                         #context=context)
                         #screen = screens[1])
        
        self.my_fullscreen = False
        self.aspect = [self.width/640.0,self.height/480.0]
        self.dt = 0
        self.Piece_de_theatre = Piece.Piece_de_theatre(self)

        #gl.glEnable(gl.GL_BLEND)
        #gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
        

    def on_draw(self):
        
        self.clear()
        self.Piece_de_theatre.Scene_de_theatre.batch.draw()

            
    def on_key_press(self, key, modifiers):
        self.Piece_de_theatre.key_pressed(key, modifiers)

        if key == pyglet.window.key.F4:
            if self.fullscreen is True:
                self.set_mouse_visible(True)
                self.set_fullscreen(fullscreen=False, width = 640, height = 480)
            else:
                self.set_mouse_visible(False)
                self.set_fullscreen(fullscreen=True, width = 640, height = 480)

        if key == pyglet.window.key.ESCAPE:
            self.set_fullscreen(fullscreen=False, width = 640, height = 480)
            self.close()

    
    def on_key_release(self, key, modifiers):
        self.Piece_de_theatre.key_released(key, modifiers)

        
    def update(self, dt):

        self.Piece_de_theatre.update(dt)


    def change_fullscreen_mode(self):
        
        self.set_fullscreen(self.my_fullscreen)
        
