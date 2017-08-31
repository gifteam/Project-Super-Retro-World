import pygame, png, math, sys
from random import randint

#from src.python_src.constants import *
#from src.python_src.classes import *

class Pathfinding():

    def __init__(self, mymap):
        self.found = False
        self.blocked = False
        self.size_x = len(mymap[0])
        self.size_y = len(mymap)
        self.around = 2
        self.distance = 0
        self.origin = self.around
        self.mymap = mymap
        self.mymap_original = [row[:] for row in self.mymap]
        self.start = (0,0)
        self.end = (0,0)

    def get_map_size_x(self):
        return self.size_x

    def get_map_size_y(self):
        return self.size_y

    def get_map_path(self):
        self.track()
        return self.mymap
           
    def track(self):
        x = self.end[0]
        y = self.end[1]
        if self.found:
            while self.around > self.origin:
                if y-1 >= 0 and self.mymap[y-1][x] == self.around:
                    self.mymap[y-1][x] = 1
                    self.around -= 1
                    y -= 1
                if y+1 < self.size_y and self.mymap[y+1][x] == self.around:
                    self.mymap[y+1][x] = 1
                    self.around -= 1
                    y += 1
                if x-1 >= 0 and self.mymap[y][x-1] == self.around:
                    self.mymap[y][x-1] = 1
                    self.around -= 1
                    x -= 1
                if x+1 < self.size_x and self.mymap[y][x+1] == self.around:
                    self.mymap[y][x+1] = 1
                    self.around -= 1
                    x += 1

    def set_robot_pos(self, pos):
        self.end = pos
        self.reset_mymap()
        
    def set_enemy_pos(self, pos):
        self.start = pos
        self.reset_mymap()
        
    def reset_mymap(self):
        self.mymap = [row[:] for row in self.mymap_original]
        self.mymap[self.start[1]][self.start[0]] = self.origin
        self.mymap[self.end[1]][self.end[0]] = self.origin-1
        
    def findpath(self):
        self.found = False
        self.blocked = False
        self.distance = 0
        self.around = self.origin
        while not self.found and not self.blocked:
            self.blocked = True
            for y in range(self.size_y):
                for x in range(self.size_x):
                    if self.mymap[y][x] == self.around:
                        self.stepup(x, y, self.around)
                        self.stepdown(x, y, self.around)
                        self.stepleft(x, y, self.around)
                        self.stepright(x, y, self.around)
            self.around += 1
        self.around -= 1
        self.distance = self.around -1
        
    def get_distance(self):
        self.findpath()
        return self.distance
            
    def stepup(self, x, y, around):
        if y-1 >= 0:
            if self.mymap[y-1][x] == 0:
                if self.mymap[y+1][x] == -1 or self.mymap[y+2][x] == -1:
                    self.mymap[y-1][x] = around + 1
                    self.blocked = False
            if self.mymap[y-1][x] == 1:
                self.found = True
            
    def stepdown(self, x, y, around):
        if y+1 < self.size_y and self.mymap[y+1][x] == 0:
            self.mymap[y+1][x] = around + 1
            self.blocked = False
        if y+1 < self.size_y and self.mymap[y+1][x] == 1:
            self.found = True  

    def stepleft(self, x, y, around):
        if x-1 >= 0 and self.mymap[y][x-1] == 0:
            self.mymap[y][x-1] = around + 1
            self.blocked = False
        if x-1 >= 0 and self.mymap[y][x-1] == 1:
            self.found = True 

    def stepright(self, x, y, around):
        if x+1 < self.size_x and self.mymap[y][x+1] == 0:
            self.mymap[y][x+1] = around + 1
            self.blocked = False
        if x+1 < self.size_x and self.mymap[y][x+1] == 1:
            self.found = True  

    def print_mymap(self):
        for y in range(self.size_y):
            print (self.mymap[y])
        print ("")
