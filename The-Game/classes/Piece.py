#Import basic librairies

#Import personal packages
from constants import constants
from classes import Scene

class Piece_de_theatre(object):

    def __init__(self, my_theatre):

        self.theatre = my_theatre
        my_scene = "DESERT"
        self.Scene_de_theatre = Scene.Scene_de_theatre(my_theatre, self, my_scene)
        self.key_list = {}


    def update(self, dt):
        
        self.Scene_de_theatre.update(dt)
        #self.Scene_de_theatre.batch.draw()
        
 
    def key_pressed(self, key, modifiers):

        self.Scene_de_theatre.key_pressed(key, modifiers)
        

    def key_released(self, key, modifiers):

        self.Scene_de_theatre.key_released(key, modifiers)


    def change_scene(self, scene):

        self.Scene_de_theatre = None
        print("new scene")
        self.Scene_de_theatre = Scene.Scene_de_theatre(self.theatre, self, scene)
