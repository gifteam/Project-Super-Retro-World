import pygame, png, math, sys
from random import randint

from src.python_src.constants import *
from src.python_src.classes import RobotSprite
from src.python_src.classes import RobotSpriteShadow

def Function_set_robot(all_sprites_list, style, pos):

    sprite = RobotSprite.Class_RobotSprite(pos[0], pos[1], 0, constants.SPRITE_X, constants.SPRITE_Y, all_sprites_list, style)
    #shadow = RobotSpriteShadow.Class_RobotSpriteShadow(constants.ROBOTSET_STYLE + "_shadow", 0, 0, -100, sprite)
    #sprite.shadow_sprite = shadow
    return [sprite, sprite.jump_effect_sprite] #, shadow]
