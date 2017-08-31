import pygame, png, math, sys
from random import randint

from src.python_src.constants import *

def Function_sort_sprites_by_layer(list_to_sort):

    sorted_list = pygame.sprite.Group()

    for z in range(-1000,1000,1):
        for item in list_to_sort:
            if item.z == z:
                sorted_list.add(item)

    return sorted_list
