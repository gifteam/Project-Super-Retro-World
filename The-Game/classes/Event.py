#Import personal packages
from constants import constants

#event_info structure:
#[ID, A, B, C, D, E, F, G, H, I]
# ID = event ID from minimap color (RGB color value divide by 100 = binary value)
# A = filename "xxx" ( x = [0-9])
# B = 1 if top_left anchor_y, 0 if bottom left anchor_y 
# C = z
# D = True if animated, False overwise
# E = animated speed if animated
# F = True if collidable, False overwise
# G = -1, 0 or 1 = offset in X mesh
# H = -1, 0 or 1 = offset in Y mesh
# I = 0 (touch activation), 1 (click activation)

class Event(object):

    def __init__(self):
        pass
        
    def get_event(self, my_scene):
        
        event_info = []
        
        if my_scene == "hard":
            pass
            
        if my_scene == "simple":
            event_info.append([1, "005", 1, 99, False, 0, False, 0, 0, 0])
            event_info.append([4, "005", 1, 99, False, 0, False, 0, 0, 0])
            
        return event_info

    def action(self, event_id):
        pass

            

