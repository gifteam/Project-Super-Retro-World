import pygame, png, math, sys
from random import randint

from src.python_src.constants import *
from src.python_src.classes import FPSSprite
from src.python_src.classes import BackgroundSprite
from src.python_src.classes import FrontgroundSprite
from src.python_src.classes import Tile
from src.python_src.classes import AnimatedSprite
from src.python_src.classes import ElementSprite

def Function_DisplayMapping(screen, mapping, mapping_edges_top_left, mapping_edges_top_right, mapping_edges_bottom_left, mapping_edges_bottom_right, mapping_deco, mapping_element, style, filter_sprite):

    #get style of the map
    back_style = constants.BACK_STYLE[style]
    tile_style = constants.TILE_STYLE[style]
    anim_style = constants.ANIMATEDSET_STYLE[style]
    element_style = constants.ELEMENT_STYLE[style]
    base_style = constants.BASE_BACK_STYLE[style]

    #set basic background
    background = pygame.Surface((screen.get_width(), screen.get_height()))
    rect = pygame.Rect((0, 0, screen.get_width(), screen.get_height()))
    background.blit(pygame.image.load(constants.PATH_BACK + base_style + ".png").convert(),(0,0),rect)
    screen.blit(background.convert(),(0,0))
    
    FPS = FPSSprite.Class_FPSSprite(False)
    animated_sprites_list = pygame.sprite.Group(FPS)

    for i in range(len(back_style)):
        back = BackgroundSprite.Class_BackgroundSprite(back_style[i], False,0, 0, max(-998,-101-100*i))
        animated_sprites_list.add(back)

    front = FrontgroundSprite.Class_FrontgroundSprite(constants.FRONTGROUND_STYLE, False,999)
    animated_sprites_list.add(front)

    #diapo = BackgroundSprite.Class_BackgroundSprite(constants.DIAPO_STYLE, False,0,0, -250)
    #animated_sprites_list.add(diapo)
    
    #update the screen
    for y in range(len(mapping)):
        for x in range(len(mapping[y])):
            tile_ID = mapping[y][x]
            if tile_ID >= 0:
                #clip the tileset to get the tile
                tile = Tile.Class_Tile(tile_style, constants.SPRITE_X, constants.SPRITE_Y, tile_ID, (x-1)*constants.SPRITE_X, (y-1)*constants.SPRITE_Y, False)
                animated_sprites_list.add(tile)
                #shadow = Tile.Class_Tile(tile_style + "_shadow", constants.SPRITE_X, constants.SPRITE_Y, tile_ID, (x-1)*constants.SPRITE_X+8, (y-1)*constants.SPRITE_Y-8, True)
                #animated_sprites_list.add(shadow)
                
    for y in range(len(mapping_edges_top_left)):
        for x in range(len(mapping_edges_top_left[y])):
            tile_ID = mapping_edges_top_left[y][x]
            if tile_ID >= 0:
                #clip the tileset to get the tile
                tile = Tile.Class_Tile(tile_style, constants.SPRITE_X, constants.SPRITE_Y, tile_ID, (x-1)*constants.SPRITE_X, (y-1)*constants.SPRITE_Y)
                animated_sprites_list.add(tile)

    for y in range(len(mapping_edges_top_right)):
        for x in range(len(mapping_edges_top_right[y])):
            tile_ID = mapping_edges_top_right[y][x]
            if tile_ID >= 0:
                #clip the tileset to get the tile
                tile = Tile.Class_Tile(tile_style, constants.SPRITE_X, constants.SPRITE_Y, tile_ID, (x-1)*constants.SPRITE_X, (y-1)*constants.SPRITE_Y)
                animated_sprites_list.add(tile)

    for y in range(len(mapping_edges_bottom_left)):
        for x in range(len(mapping_edges_bottom_left[y])):
            tile_ID = mapping_edges_bottom_left[y][x]
            if tile_ID >= 0:
                #clip the tileset to get the tile
                tile = Tile.Class_Tile(tile_style, constants.SPRITE_X, constants.SPRITE_Y, tile_ID,(x-1)*constants.SPRITE_X, (y-1)*constants.SPRITE_Y)
                animated_sprites_list.add(tile)

    for y in range(len(mapping_edges_bottom_right)):
        for x in range(len(mapping_edges_bottom_right[y])):
            tile_ID = mapping_edges_bottom_right[y][x]
            if tile_ID >= 0:
                #clip the tileset to get the tile
                tile = Tile.Class_Tile(tile_style, constants.SPRITE_X, constants.SPRITE_Y, tile_ID, (x-1)*constants.SPRITE_X, (y-1)*constants.SPRITE_Y)
                animated_sprites_list.add(tile)

    for i in range(len(mapping_deco)):
        deco = AnimatedSprite.Class_AnimatedSprite(anim_style, mapping_deco[i][0]*constants.SPRITE_X, mapping_deco[i][1]*constants.SPRITE_Y, constants.SPRITE_X, constants.SPRITE_Y,  False, -20)
        animated_sprites_list.add(deco)
        #shadow = AnimatedSprite.Class_AnimatedSprite(anim_style + "_shadow", mapping_deco[i][0]*constants.SPRITE_X+8, mapping_deco[i][1]*constants.SPRITE_Y-8, constants.SPRITE_X, constants.SPRITE_Y,  False, -49)
        #animated_sprites_list.add(shadow)   

    for i in range(len(mapping_element)):
        element = ElementSprite.Class_ElementSprite(element_style, tile_style, mapping_element[i][0]*constants.SPRITE_X, mapping_element[i][1]*constants.SPRITE_Y, mapping_element[i][2], constants.SPRITE_X, constants.SPRITE_Y, False, -20, filter_sprite, 0)
        animated_sprites_list.add(element)
        element_top = ElementSprite.Class_ElementSprite(element_style, tile_style, mapping_element[i][0]*constants.SPRITE_X, mapping_element[i][1]*constants.SPRITE_Y-32, mapping_element[i][2], constants.SPRITE_X, constants.SPRITE_Y,  False, -20, filter_sprite, -1)
        animated_sprites_list.add(element_top)

    return screen, animated_sprites_list, background
