#Import basic librairies

#Import personal packages
from constants import constants

class Event(object):

    def __init__(self, my_theatre, my_piece, my_scene):
        
        self.my_theatre = my_theatre
        self.my_piece = my_piece
        self.my_scene = my_scene
        self.my_player = None
        self.my_sprite_list = []
        

    def action(self, event_id):

        if event_id == -1:
            print("DEAD")
            self.my_scene.new_name = "LEVEL_SELECT"
        
        if self.my_scene.name == "LEVEL_SELECT":
            self.LEVEL_SELECT_action(event_id)
            
        if self.my_scene.name == "DESERT":
            self.DESERT_action(event_id)

        if self.my_scene.name == "TEMPLE":
            self.TEMPLE_action(event_id)

        if self.my_scene.name == "WATER":
            self.WATER_action(event_id)

            
    def LEVEL_SELECT_action(self, event_id):
        
        if event_id == 0:
            self.my_scene.new_name = "DESERT"
            
        elif event_id == 1:
            self.my_scene.new_name = "TEMPLE"
            
        elif event_id == 2:
            self.my_scene.new_name = "WATER"

    def DESERT_action(self, event_id):
        
        if event_id == 0:
            self.my_scene.new_name = "LEVEL_SELECT"
            

    def TEMPLE_action(self, event_id):
        
        if event_id == 0:
            self.my_scene.new_name = "LEVEL_SELECT"
            

    def WATER_action(self, event_id):
        
        if event_id == 0:
            self.my_scene.new_name = "LEVEL_SELECT"
