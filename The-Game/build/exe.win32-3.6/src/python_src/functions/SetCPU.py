import pygame, png, math, sys
from random import randint

from src.python_src.constants import *
from src.python_src.classes import *

def Function_set_CPU(all_sprites_list, brain):

    sprite = CPUSprite.Class_CPUSprite(constants.ENEMYSET_STYLE, 0, 0, 0, constants.SPRITE_X, constants.SPRITE_Y, all_sprites_list, brain)
    brain.enemy = sprite
    #shadow = RobotSpriteShadow.Class_RobotSpriteShadow(constants.ROBOTSET_STYLE + "_shadow", 0, 0, -100, sprite)
    #sprite.shadow_sprite = shadow
    return sprite #, shadow
