#Import personal packages
from constants import constants

class Event_action(object):

    def __init__(self):
        pass

    def action(self, scene, event_id, event_sprite, textbox_sprite, player_sprite):

        textbox_sprite.activation_textbox = False

        if scene == "simple":
            self.action_level_simple(event_id, event_sprite, textbox_sprite, player_sprite)


    def action_level_simple(self, event_id, event_sprite, textbox_sprite, player_sprite):
        
        if event_id == 1 and not player_sprite.new_jump:
            player_sprite.want_to_jump = True
            
        if event_id == 4:
            textbox_sprite.x = 240
            textbox_sprite.y = 300
            textbox_sprite.activation_textbox = True
