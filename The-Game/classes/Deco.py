#Import personal packages
from constants import constants

#deco_info structure:
#[0, 1, 2, 3, 4, 5, 6, 7, 8]
# 0 = event ID from minimap color (RGB color value divide by 100 = trinary value)
#     possible values = 1 3 4 5 7 8 9 10 11 12 13 14
# 1 = filename "xxx" ( x = [0-9])
# 2 = 1 if top_left anchor_y, 0 if bottom left anchor_y 
# 3 = z
# 4 = True if animated, False overwise
# 5 = animated speed if animated
# 6 = True if collidable, False overwise
# 7 = -1, 0 or 1 = offset in X
# 8 = -1, 0 or 1 = offset in Y


class Deco(object):

    def __init__(self):
        pass
        

    def get_deco(self, my_scene):
        
        deco_info = []
            
        if my_scene == "LEVEL_0_0":
            deco_info.append([4, "012", 0, 200, True, 0.1, False, 0, 0])
            deco_info.append([5, "001", 0, 200, True, 0.5, False, 0, 0])

        if my_scene == "hard":
            pass
            #deco_info.append([3, "012", 0, 200, True, 0.1, False, 0, 0])

        return deco_info
