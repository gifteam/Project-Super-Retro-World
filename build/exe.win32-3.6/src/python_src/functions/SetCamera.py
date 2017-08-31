import pygame, png, math, sys
from random import randint

from src.python_src.constants import *
from src.python_src.classes import *

def Function_set_camera(target, lights_src, map_size, style):

    return Camera.Camera_object(target, lights_src, map_size, style)
