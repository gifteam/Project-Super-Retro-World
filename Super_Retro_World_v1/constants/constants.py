#Constants -----
    #FPS
FRAMES_PER_SECOND = 60
FRAMES_MAX = 60
#ID for Deco and Events ---------
#Trinaire code
# ID [R G B]
#  0  0 0 0 TILE
#  1  0 0 1 START POS
#  2  0 0 2 BLUE FILTER
#  3  0 1 0 DECO
#  4  0 1 1 DECO
#  5  0 1 2 DECO
#  6  0 2 0 GREEN FILTER
#  7  0 2 1 DECO
#  8  0 2 2 DECO
#  9  1 0 0 DECO
# 10  1 0 1 DECO
# 11  1 0 2 DECO
# 12  1 1 0 DECO
# 13  1 1 1 DECO
# 14  1 1 2 DECO
# 15  1 2 0 EVENT
# 16  1 2 1 EVENT
# 17  1 2 2 EVENT
# 18  2 0 0 RED FILTER
# 19  2 0 1 EVENT
# 20  2 0 2 EVENT
# 21  2 1 0 EVENT
# 22  2 1 1 EVENT
# 23  2 1 2 EVENT
# 24  2 2 0 EVENT
# 25  2 2 1 EVENT
# 26  2 2 2 EVENT

#---------------
    #scene dictionary style
MAP_STYLE = {}
BASE_BACK_STYLE = {}
BACK_STYLE = {}
FRONT_STYLE = {}
TILE_STYLE = {}
LIGHT_SOURCE = {}
#[_, _, _, (_, _, _, _)]
# 0 = None, 1 = orange deco lighted, 2 = player only, 3 = global
# 2, 4, 8, 16 or 32 = light pixel resolution (lower if better)
# 2 to 15 = light range
# (0,0,0,0) = shadow color and alpha
ELEMENT_STYLE = {}
PLAYER_STYLE = {}
ENEMYSET_STYLE = {}
LOADING_STYLE = {}
WAKE_UP_STYLE = {}

    #LEVEL SIMPLE
style = "LEVEL_0_0"
MAP_STYLE[style] = "LEVEL_0_0"
BASE_BACK_STYLE[style] = "forest_017"
BACK_STYLE[style] = []
FRONT_STYLE[style] = "001"
TILE_STYLE[style] = "003"
ELEMENT_STYLE[style] = "001"
PLAYER_STYLE[style] = "005"
ENEMYSET_STYLE[style] = "002"
LOADING_STYLE[style] = "002"
WAKE_UP_STYLE[style] = "004"
    #LEVEL MEDIUM
style = "LEVEL_1_0"
MAP_STYLE[style] = "LEVEL_1_0"
BASE_BACK_STYLE[style] = "forest_017"
BACK_STYLE[style] = []
FRONT_STYLE[style] = "001"
TILE_STYLE[style] = "003"
ELEMENT_STYLE[style] = "001"
PLAYER_STYLE[style] = "005"
ENEMYSET_STYLE[style] = "002"
LOADING_STYLE[style] = "002"
WAKE_UP_STYLE[style] = "004"
    #LEVEL HARD
style = "LEVEL_2_0"
MAP_STYLE[style] = "LEVEL_2_0"
BASE_BACK_STYLE[style] = "forest_017"
BACK_STYLE[style] = ["forest_016","forest_015","forest_014"]
FRONT_STYLE[style] = "001"
TILE_STYLE[style] = "003"
ELEMENT_STYLE[style] = "001"
PLAYER_STYLE[style] = "005"
ENEMYSET_STYLE[style] = "002"
LOADING_STYLE[style] = "002"
WAKE_UP_STYLE[style] = "004"
    #sprite style
HITBOX_STYLE = "001"
    #sprite size
SPRITE_X = 32
SPRITE_Y = 32 
    #Number of tiles per dimension
TILES_X = 32
TILES_Y = 32
    #Txt box style
TXTBOX_SPEED = 5 #from 0 to 10 max
    #layers info (z value)
#LAYERS NAME   = [background] [ tile  ] [sprites] [  tile ] [ player] [  tile ] [sprites] [  tile ] [frontground] [  HUD  ]
#LAYERS VALUES = [  0  ; 99 ] [100;199] [200;299] [300;399] [400;499] [500;599] [600;699] [700;799] [  800;899  ] [900;999]
#---------------
#EVENT IDs rules
#   0 -  99 : activation 
# 100 - 199 : coins
# 200 - 299 : ennemies
# 300 - 399 : decoration

    #paths
PATH_BACK = "src\\visual_src\\background\\"
PATH_FRONT = "src\\visual_src\\frontground\\"
PATH_CHARA = "src\\visual_src\character\\"
PATH_DECO = "src\\visual_src\decoration\\"
PATH_HIT = "src\\visual_src\hitbox\\"
PATH_TILE = "src\\visual_src\\tileset\\"
PATH_MAP = "src\maps_src\\"
PATH_SOUND = "src\sound_src\\"
PATH_EFFECT = "src\\visual_src\effect\\"
PATH_HUD = "src\\visual_src\interface\\"
PATH_LABEL = "src\\visual_src\label\\"
PATH_EVENT = "src\\visual_src\event\\"
PATH_TEXTBOX = "src\\visual_src\\textbox\\"
    #game title
GAME_TITLE = "The game"

