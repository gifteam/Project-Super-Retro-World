#Constants -----
    #FPS
FRAME_PER_SECONDS = 60
    #screen size
SCREEN_X = 640
SCREEN_Y = 480
    #center immobile screen size
IMMOBILE_SCREEN_X = 640/2
IMMOBILE_SCREEN_Y = 480/2
    #map style
MAP_STYLE = "001"
BACKGROUND_BASE = "005"
BACKGROUND_STYLE = "001"
FRONTGROUND_STYLE = "001"
DIAPO_STYLE = "002"
#---------------
    #scene dictionary style
MAP_STYLE = {}
BASE_BACK_STYLE = {}
BACK_STYLE = {}
TILE_STYLE = {}
LIGHT_SOURCE = {}
#[_, _, _, (_, _, _, _)]
# 0 = None, 1 = orange deco lighted, 2 = player only, 3 = global
# 2, 4, 8, 16 or 32 = light pixel resolution (lower if better)
# 2 to 15 = light range
# (0,0,0,0) = shadow color and alpha
ANIMATEDSET_STYLE = {}
ELEMENT_STYLE = {}
ROBOTSET_STYLE = {}
ENEMYSET_STYLE = {}
LOADING_STYLE = {}
    #Title screen style
TITLE_SCREEN_STYLE = ["title_009", "title_012", "title_013", "title_011", "title_008", "title_010", "title_007", "title_006"]
    #Level 01 style
MAP_STYLE["SLEEPING_FOREST"] = "004"
BASE_BACK_STYLE["SLEEPING_FOREST"] = "forest_018"
BACK_STYLE["SLEEPING_FOREST"] = ["forest_014","forest_015","forest_016","forest_017"]
TILE_STYLE["SLEEPING_FOREST"] = "003"
LIGHT_SOURCE["SLEEPING_FOREST"] = [0, 8, 13, (20, 30, 50, 10)]
ANIMATEDSET_STYLE["SLEEPING_FOREST"] = "001"
ELEMENT_STYLE["SLEEPING_FOREST"] = "001"
ROBOTSET_STYLE["SLEEPING_FOREST"] = "001"
ENEMYSET_STYLE["SLEEPING_FOREST"] = "002"
LOADING_STYLE["SLEEPING_FOREST"] = "002"
    #sprite style
HITBOX_STYLE = "001"
WAKE_UP_STYLE = "001_wake_up"
    #sprite size
SPRITE_X = 32
SPRITE_Y = 32 
    #Number tile per dimension
TILES_X = int(SCREEN_X/SPRITE_X)
TILES_Y = int(SCREEN_Y/SPRITE_Y)
    #Txt box style
TXTBOX_SPEED = 5 #from 0 to 10 max
    #layers info (z value)
#LAYERS NAME   = [background] [  tile  ] [sprites] [ tile ] [player] [tile] [sprites] [ tile ] [frontground] [HUD]
#LAYERS VALUES = [ -998;-101] [-100;-50] [-49;-20] [-19;-1] [   0  ] [1;19] [ 20;49 ] [50;100] [  101;998  ] [999]
#---------------
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
    #game title
GAME_TITLE = "The game"

