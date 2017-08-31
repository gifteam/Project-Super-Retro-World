#Import librairies
import pygame, png, math, sys#, numpy
from random import randint

from src.python_src.constants import *
from src.python_src.classes import Pathfinding

class Class_Brain():

    def __init__(self):
        self.k_left = 0
        self.k_right = 0
        self.k_jump = 0
        self.robot = False
        self.enemy = False
        self.mapset = png.Reader(filename=constants.PATH_MAP + constants.MAP_STYLE + ".png")
        self.map_x, self.map_y, self.map_pix, self.map_data = self.mapset.read_flat()
        self.pix_byte = 4 if self.map_data['alpha'] else 3
        self.mapping = [[0 for x in range(self.map_x)] for y in range(self.map_y)]
        for pix in range(self.map_y * self.map_x):
            red = self.map_pix[pix * self.pix_byte]
            self.mapping[int(pix/constants.TILES_X)][pix%constants.TILES_X] = 0 if red == 255 else -1
        self.pathfinding = Pathfinding.Pathfinding(self.mapping)
        self.mapping_x25 = False
        self.fitness = 0
        self.previous_fitness = self.fitness
        self.w1 = [[randint(0,10) for x in range(5)] for y in range(5)]
        self.reset_needed = False
        self.nb_frame_to_wait = 0
        self.nb_frame_to_wait_max = constants.FRAME_PER_SECONDS * 1

    def multiply_input_with_w1(self):
        return
        #transformer les array en np.array
        #result = A.dot(B)
        

    def reset_enemy(self):
        self.save_text_file = open("Output.txt", "a")
        self.save_text_file.write("-----------------------------------------------------------------------\n")
        self.save_text_file.write("Best fitness: " + str(self.fitness) + "\n")
        self.save_text_file.write(str(self.w1) + "\n")
        self.save_text_file.close()
        self.fitness = 0
        self.previous_fitness = self.fitness
        self.w1 = [[randint(0,10) for x in range(5)] for y in range(5)]
        self.reset_needed = False
        self.enemy.reset_position()
        self.nb_frame_to_wait = 0
        self.nb_frame_to_wait_max = constants.FRAME_PER_SECONDS * 1
        
    def robot_position(self):
        return self.robot.collide_rect.left, self.robot.collide_rect.top

    def enemy_position(self):
        return self.enemy.collide_rect.left, self.enemy.collide_rect.top

    def get_map_size_x(self):
        return self.pathfinding.get_map_size_x()

    def get_map_size_y(self):
        return self.pathfinding.get_map_size_y()
    
    def get_map_path(self):
        return self.pathfinding.get_map_path()
        
    def update_distance(self):
        #x1, y1 = self.robot.collide_rect.left, self.robot.collide_rect.top
        #x2, y2 = self.enemy.collide_rect.left, self.enemy.collide_rect.top
        #self.pathfinding.set_robot_pos((int(x1/32),int(y1/32)))
        #self.pathfinding.set_enemy_pos((int(x2/32),int(y2/32)))
        #self.distance_robot_enemy = self.pathfinding.get_distance()
        self.fitness = self.enemy.collide_rect.left
        if self.fitness > self.previous_fitness:
            self.previous_fitness = self.fitness
            self.reset_needed = False
            self.nb_frame_to_wait = 0
        else:
            self.nb_frame_to_wait += 1
        if self.nb_frame_to_wait == self.nb_frame_to_wait_max:
            self.reset_needed = True
            
    def update_inputs(self):
        self.k_left = 0 #self.left_pressed()
        self.k_right = 0 #self.right_pressed()
        self.k_jump = 0 #self.jump_pressed()

    def left_pressed(self):
        left = 0
        for y in range(5):
            for x in range(5):
                if abs(self.mapping_x25[y][x]) == 1:
                    if self.left_reaction[y][x] == 1:
                        left += 1
                    if self.left_no_reaction[y][x] == 1:
                        left -= 1
        if left <= 0:
            return 0
        else:
            return 1

    def right_pressed(self):
        right = 0
        for y in range(5):
            for x in range(5):
                if abs(self.mapping_x25[y][x]) == 1:
                    if self.right_reaction[y][x] == 1:
                        right += 1
                    if self.right_no_reaction[y][x] == 1:
                        right -= 1
        if right <= 0:
            return 0
        else:
            return 1

    def jump_pressed(self):
        jump = 0
        for y in range(5):
            for x in range(5):
                if abs(self.mapping_x25[y][x]) == 1:
                    if self.jump_reaction[y][x] == 1:
                        jump += 1
                    if self.jump_no_reaction[y][x] == 1:
                        jump -= 1
        if jump <= 0:
            return 0
        else:
            return 1
    
    def update_tiles_around_ennemy(self):
        self.mapping_x25 = [[0 for x in range(5)] for y in range(5)]
        x2, y2 = int(self.enemy.collide_rect.left/32), int(self.enemy.collide_rect.top/32)
        for y in range(5):
            for x in range(5):
                if y-2+y2 >= 0 and y-2+y2 < self.get_map_size_y():
                    if x-2+x2 >= 0 and x-2+x2 < self.get_map_size_x():
                        self.mapping_x25[y][x] = self.mapping[y-2+y2][x-2+x2]
                else:
                    self.mapping_x25[y][x] = 0
        
    def update(self):
        self.update_distance()
        self.update_tiles_around_ennemy()
        self.update_inputs()
        if self.reset_needed:
            self.reset_enemy()
        
