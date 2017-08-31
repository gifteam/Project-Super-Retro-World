import pygame, png, math, sys
from random import randint
from threading import Thread

from src.python_src.constants import *
from src.python_src.classes import Gif

def this_bloc_is(r, g, b):
    result = ""
    if r == 255 and g == 255 and b == 255:
        result = "EMPTY"
    elif r == 0 and g == 0 and b == 0:
        result = "FLOOR"
    elif r == 255 and g == 0 and b == 0:
        result = "ELEMENT"
    elif r == 0 and g == 255 and b == 0:
        result = "ELEMENT"
    elif r == 0 and g == 0 and b == 255:
        result = "ELEMENT"
    return result

def Function_CalculateMapping(screen, style):

    #tileset datas
    map_size = pygame.image.load(constants.PATH_MAP + constants.MAP_STYLE[style] + ".png")
    map_size = (map_size.get_width(), map_size.get_height())
    mapset = png.Reader(filename=constants.PATH_MAP + constants.MAP_STYLE[style] + ".png")
    map_x, map_y, map_pix, map_data = mapset.read_flat()
    pix_byte = 4 if map_data['alpha'] else 3

    #create a nice little loading gif
    loading_gif = Gif.Gif_sprite(screen, style)
    loading_gif_thread = Thread(name = 'loading_gif', target = loading_gif.update, args = ())
    loading_gif_thread.start()

    #construct the basic mapping from the map
    mapping = [[-1 for x in range(map_x+2)] for y in range(map_y+2)]
    mapping_edges_top_left = [[-1 for x in range(map_x+2)] for y in range(map_y+2)]
    mapping_edges_top_right = [[-1 for x in range(map_x+2)] for y in range(map_y+2)]
    mapping_edges_bottom_left = [[-1 for x in range(map_x+2)] for y in range(map_y+2)]
    mapping_edges_bottom_right = [[-1 for x in range(map_x+2)] for y in range(map_y+2)]
    mapping_lights = []
    mapping_deco = []
    mapping_element = []
    
    for pix in range(map_y*map_x):
        red = map_pix[pix * pix_byte]
        green = map_pix[pix * pix_byte + 1]
        blue = map_pix[pix * pix_byte + 2]
        if this_bloc_is(red, green, blue) == "DECORATION":
            mapping_deco.append([pix%map_x, int(pix/map_x)])
        if this_bloc_is(red, green, blue) == "EMPTY":
            mapping[int(pix/map_x)+1][pix%map_x+1] = -100
        elif this_bloc_is(red, green, blue) == "FLOOR":
            mapping[int(pix/map_x)+1][pix%map_x+1] = 5
        if this_bloc_is(red, green, blue) == "ELEMENT":
            mapping_element.append([pix%map_x, int(pix/map_x), [red, green, blue]])
            

    #set levitating tiles (ID 20 to 23)
    for y in range (1,len(mapping)-1):
        for x in range(1,len(mapping[y])-1):
            #if it's a tile
            if mapping[y][x] > 0:
                #if nothing below and upper
                if mapping[y-1][x] < 0 and mapping[y+1][x] < 0:
                    #if nothing left or right
                    if mapping[y][x-1] < 0:
                        if mapping[y][x+1] < 0:
                            mapping[y][x] = 23
                        else:
                            mapping[y][x] = 20
                    else:
                        if mapping[y][x+1] < 0:
                            mapping[y][x] = 22
                        else:
                            mapping[y][x] = 21

    #set basic tiles (ID 4 to 7) - physical
    for y in range (1,len(mapping)-1):
        for x in range(1,len(mapping[y])-1):
            #if it's a tile
            if mapping[y][x] > 0:
                #if something below and nothing upper
                if mapping[y-1][x] < 0 and mapping[y+1][x] > 0:
                    #if nothing left or right
                    if mapping[y][x-1] < 0:
                        if mapping[y][x+1] < 0:
                            mapping[y][x] = 7
                        else:
                            mapping[y][x] = 4
                    else:
                        if mapping[y][x+1] < 0:
                            mapping[y][x] = 6
                        else:
                            mapping[y][x] = 5
                          
    #set inners tiles (ID 8 to 11) - physical
    for y in range (1,len(mapping)-1):
        for x in range(1,len(mapping[y])-1):
            #if it's a tile
            if mapping[y][x] > 0:
                #if something below and upper
                if mapping[y-1][x] > 0 and mapping[y+1][x] > 0:
                    #if nothing left or right
                    if mapping[y][x-1] < 0:
                        if mapping[y][x+1] < 0:
                            mapping[y][x] = 11
                        else:
                            mapping[y][x] = 8
                    else:
                        if mapping[y][x+1] < 0:
                            mapping[y][x] = 10
                        else:
                            mapping[y][x] = 9
                            
    #set below tiles (ID 12 to 15) - physical
    for y in range (1,len(mapping)-1):
        for x in range(1,len(mapping[y])-1):
            #if it's a tile
            if mapping[y][x] > 0:
                #if nothing below and something upper
                if mapping[y-1][x] > 0 and mapping[y+1][x] < 0:
                    #if nothing left or right
                    if mapping[y][x-1] < 0:
                        if mapping[y][x+1] < 0:
                            mapping[y][x] = 15
                        else:
                            mapping[y][x] = 12
                    else:
                        if mapping[y][x+1] < 0:
                            mapping[y][x] = 14
                        else:
                            mapping[y][x] = 13

    #set edges tiles (ID 26, 27, 30, 31) - physical          
    for y in range (1,len(mapping)-1):
        for x in range(1,len(mapping[y])-1):
            #if it's not a tile
            if mapping[y][x] > 0:
                #TOP LEFT edge
                if mapping[y][x+1] > 0 and mapping[y+1][x] > 0 and mapping[y+1][x+1] < 0:
                    mapping_edges_top_left[y][x] = 24
                #TOP RIGHT edge
                if mapping[y][x-1] > 0 and mapping[y+1][x] > 0 and mapping[y+1][x-1] < 0:
                    mapping_edges_top_right[y][x] = 25
                #BOTTOM LEFT edge
                if mapping[y][x+1] > 0 and mapping[y-1][x] > 0 and mapping[y-1][x+1] < 0:
                    mapping_edges_bottom_left[y][x] = 30
                    mapping_edges_bottom_left[y-1][x] = 26
                #BOTTOM RIGHT edge
                if mapping[y][x-1] > 0 and mapping[y-1][x] > 0 and mapping[y-1][x-1] < 0:
                    mapping_edges_bottom_right[y][x] = 31
                    mapping_edges_bottom_right[y-1][x] = 27
                           
    #set upper tiles (ID 0 to 3) - not physical          
    for y in range (1,len(mapping)-1):
        for x in range(1,len(mapping[y])-1):
            #if it's not a tile
            if mapping[y][x] < 0:
                #if something below
                if mapping[y+1][x] > 0:
                    #if nothing left or right
                    if mapping[y+1][x-1] < 0:
                        if mapping[y+1][x+1] < 0:
                            mapping[y][x] = 3
                        else:
                            mapping[y][x] = 0
                            #mapping_deco.append([x-1, y-1])
                    else:
                        if mapping[y+1][x+1] < 0:
                            mapping[y][x] = 2
                        else:
                            mapping[y][x] = 1
                            #mapping_deco.append([x-1, y-1])


    return screen, mapping, mapping_edges_top_left, mapping_edges_top_right, mapping_edges_bottom_left, mapping_edges_bottom_right, mapping_deco, mapping_element, loading_gif, map_size
