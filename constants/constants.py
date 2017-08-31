#Constants -----
    #FPS
FRAMES_PER_SECOND = 60
FRAMES_MAX = 180
    #screen size
SCREEN_X = 640# 1280
SCREEN_Y = 480# 960
    #center immobile screen size
IMMOBILE_SCREEN_X = 640/2
IMMOBILE_SCREEN_Y = 480/2
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

    #Level select style
style = "LEVEL_SELECT"
MAP_STYLE[style] = "002"
BASE_BACK_STYLE[style] = "001"
BACK_STYLE[style] = ["select_001"]
FRONT_STYLE[style] = "001"
TILE_STYLE[style] = "003"
LIGHT_SOURCE[style] = [0, 8, 13, (20, 30, 50, 10)]
ELEMENT_STYLE[style] = "001"
PLAYER_STYLE[style] = "003"
ENEMYSET_STYLE[style] = "002"
LOADING_STYLE[style] = "002"
WAKE_UP_STYLE[style] = "004"
    #Level 01 style
style = "DESERT"
MAP_STYLE[style] = "005"
BASE_BACK_STYLE[style] = "forest_017"
BACK_STYLE[style] = ["forest_016","forest_015","forest_014"]
FRONT_STYLE[style] = "001"
TILE_STYLE[style] = "003"
ELEMENT_STYLE[style] = "001"
PLAYER_STYLE[style] = "003"
ENEMYSET_STYLE[style] = "002"
LOADING_STYLE[style] = "002"
WAKE_UP_STYLE[style] = "004"
    #Level 02 style
style = "TEMPLE"
MAP_STYLE[style] = "001"
BASE_BACK_STYLE[style] = "forest_017"
BACK_STYLE[style] = ["forest_016","forest_015","forest_014"]
FRONT_STYLE[style] = "001"
TILE_STYLE[style] = "003"
LIGHT_SOURCE[style] = [0, 8, 13, (20, 30, 50, 10)]
ELEMENT_STYLE[style] = "001"
PLAYER_STYLE[style] = "003"
ENEMYSET_STYLE[style] = "002"
LOADING_STYLE[style] = "002"
WAKE_UP_STYLE[style] = "004"
    #Level 03 style
style = "WATER"
MAP_STYLE[style] = "001"
BASE_BACK_STYLE[style] = "001"
BACK_STYLE[style] = ["forest_017","forest_016","forest_015","forest_014"]
FRONT_STYLE[style] = "001"
TILE_STYLE[style] = "002"
LIGHT_SOURCE[style] = [0, 8, 13, (20, 30, 50, 10)]
ELEMENT_STYLE[style] = "001"
PLAYER_STYLE[style] = "003"
ENEMYSET_STYLE[style] = "002"
LOADING_STYLE[style] = "002"
WAKE_UP_STYLE[style] = "004"
    #sprite style
HITBOX_STYLE = "001"
    #sprite size
SPRITE_X = 32
SPRITE_Y = 32 
    #Number of tiles per dimension
TILES_X = int(SCREEN_X/SPRITE_X)
TILES_Y = int(SCREEN_Y/SPRITE_Y)
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
    #game title
GAME_TITLE = "The game"

