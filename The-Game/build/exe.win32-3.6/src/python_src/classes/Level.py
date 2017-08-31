#Import librairies
import pygame, png, math, sys
from random import randint

from src.python_src.constants import *
from src.python_src.functions import CalculateMapping
from src.python_src.functions import DisplayMapping
from src.python_src.functions import SetRobot
from src.python_src.functions import SortSpritesByLayers
from src.python_src.functions import SetCamera
from src.python_src.functions import SetTextBox
from src.python_src.functions import SetHUD

class Level_object(object):
    
    def __init__(self, screen, style):
        #create hud sprite
        hud = SetHUD.Function_set_HUD()
        
        #calculate the mapping from the basic map
        self.screen, self.mapping, self.mapping_edges_top_left, self.mapping_edges_top_right, self.mapping_edges_bottom_left, self.mapping_edges_bottom_right, self.mapping_deco, self.mapping_element, self.loading_gif, map_size = CalculateMapping.Function_CalculateMapping(screen, style) 

        #create all the sprites (the mapping)
        self.screen, self.all_sprites_list, self.background = DisplayMapping.Function_DisplayMapping(self.screen, self.mapping, self.mapping_edges_top_left, self.mapping_edges_top_right, self.mapping_edges_bottom_left, self.mapping_edges_bottom_right, self.mapping_deco, self.mapping_element, style, hud)

        #add the hud to the sprite_list
        self.all_sprites_list.add(hud)

        #add the robot to the animated_sprites_list
        robot = SetRobot.Function_set_robot(self.all_sprites_list, style, [0,0])
        self.all_sprites_list.add(robot)
        self.robot = robot[0]
        #robot2 = SetRobot.Function_set_robot(self.all_sprites_list, style, [64,0])
        #self.all_sprites_list.add(robot2)
        #self.robot_2 = robot2[0]
                                  
        #Add a text box sprite
        #txt = "It's late..._"
        #txt_box = SetTextBox.Function_set_textbox(txt, self.robot)
        #self.all_sprites_list.add(txt_box)

        #Sort by layer (self.z) once
        self.all_sprites_list = SortSpritesByLayers.Function_sort_sprites_by_layer(self.all_sprites_list)

        #set camera center target
        self.my_camera = SetCamera.Function_set_camera(self.robot, self.mapping_deco, map_size, style)

        #stop the loading gif thread
        self.loading_gif.run = False

    def go_to_next_scene(self):
        return ""

    def update(self):
     
        #sprites's update (calculate everything)
        self.robot.update(self.my_camera.target)
        #self.robot_2.update(self.my_camera.target)
        self.my_camera.clear_all_sprites_list(self.background, self.screen)
        self.all_sprites_list.update(self.my_camera.target)
        self.my_camera.draw_all_sprites_list(self.all_sprites_list, self.screen)
        
        #update the screen once everything is calculated
        pygame.display.update()   

        #Prepare the robot for the next update
        self.robot.have_to_update = True
        #self.robot_2.have_to_update = True
