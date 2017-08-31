#Import personal packages
from constants import constants

#deco_info structure:
#[ID, A, B, C, D, E, F, G, H]
# ID = event ID from minimap color (RGB color value divide by 100 = binary value)
# A = filename "xxx" ( x = [0-9])
# B = 1 if top_left anchor_y, 0 if bottom left anchor_y 
# C = z
# D = True if animated, False overwise
# E = animated speed if animated
# F = True if collidable, False overwise
# G = -1, 0 or 1 = offset in X
# H = -1, 0 or 1 = offset in Y


class Deco(object):

    def __init__(self):
        pass
        

    def get_deco(self, my_scene):
        
        deco_info = []
        
        if my_scene == "DESERT":
            deco_info.append([1, "005", 1, 99, True, 0.05, False, 0, 1])
            deco_info.append([2, "005", 1, 600, True, 0.05, False, 0, 1])
            deco_info.append([3, "011", 0, 200, True, 0.05, False, 0, 0])

        return deco_info
