import pygame, math
from src.python_src.constants import *

class Lighting_object(object):
    
    def __init__(self, mapping_light_scr, map_size, cam_x, cam_y, style):

        #LIGHTS CONDITIONS
        self.style = style
        self.light_effect_activated = False
        if constants.LIGHT_SOURCE[self.style][0] == 0:
            self.light_effect_activated = False
        else:
            self.light_effect_activated = True

        if self.light_effect_activated:

            self.light_all_spots = False    
            self.light_only_robot = False
            self.light_only_screen_center = False
            if constants.LIGHT_SOURCE[self.style][0] == 1:
                self.light_all_spots = True
                self.light_only_robot = False
                self.light_only_screen_center = False
            if constants.LIGHT_SOURCE[self.style][0] == 2:
                self.light_all_spots = False
                self.light_only_robot = True
                self.light_only_screen_center = False
            if constants.LIGHT_SOURCE[self.style][0] == 3:
                self.light_all_spots = False
                self.light_only_robot = False
                self.light_only_screen_center = True
                
            light_unit_size = constants.LIGHT_SOURCE[self.style][1]
            self.light_size_x = light_unit_size
            self.light_size_y = light_unit_size
            self.light_range = constants.LIGHT_SOURCE[self.style][2]*32
            
            if self.light_all_spots:
                x = ((map_size[0]+20*2) * constants.SPRITE_X)/light_unit_size
                y = constants.SCREEN_Y / light_unit_size
                self.light_matrix = [int(x), int(y)]
                self.light_surf_mini = pygame.Surface((self.light_size_x, self.light_size_y)).convert_alpha()
                self.light_surf = pygame.Surface(((self.light_matrix[0] * light_unit_size), constants.SCREEN_Y)).convert_alpha()
            elif self.light_only_robot:
                mapping_light_scr = [[10,8]]
                x = constants.SCREEN_X / light_unit_size
                y = constants.SCREEN_Y*3 / light_unit_size
                self.light_matrix = [int(x), int(y)]
                self.light_surf_mini = pygame.Surface((self.light_size_x, self.light_size_y)).convert_alpha()
                self.light_surf = pygame.Surface((constants.SCREEN_X, constants.SCREEN_Y*3)).convert_alpha()
            elif self.light_only_screen_center:
                mapping_light_scr = [[10,7]]
                x = constants.SCREEN_X / light_unit_size
                y = constants.SCREEN_Y / light_unit_size
                self.light_matrix = [int(x), int(y)]
                self.light_surf_mini = pygame.Surface((self.light_size_x, self.light_size_y)).convert_alpha()
                self.light_surf = pygame.Surface(((map_size[0] * constants.SPRITE_X + constants.SCREEN_X * 2), constants.SCREEN_Y)).convert_alpha()

            self.light_scr = mapping_light_scr
            self.light_screen_rect = pygame.Rect(0, 0, 640, 480)
            self.calculate_light_effect(cam_x, cam_y)

    def calculate_light_effect(self, cam_x, cam_y):
        self.light_surf.fill((0,0,0,0))
        for x in range(int(self.light_matrix[0])):
            for y in range(self.light_matrix[1]):
                dist_src = 999
                alpha = 0
                for i in range(len(self.light_scr)):
                    a = abs(self.light_scr[i][0]*32 - cam_x - self.light_size_x*x)
                    if self.light_all_spots:
                        a = abs(self.light_scr[i][0]*32 - cam_x - self.light_size_x*x + constants.SCREEN_X)
                    b = abs(self.light_scr[i][1]*32 - cam_y - self.light_size_y*y)
                    if self.light_only_robot:
                        b = abs(self.light_scr[i][1]*32 - cam_y + constants.SCREEN_Y - self.light_size_y*y)
                    dist_src = math.sqrt(math.pow(a,2)+math.pow(b,2))
                    if dist_src <= self.light_range:
                        if alpha == 0:
                            alpha = int(255 - min(1, dist_src/self.light_range)*255)    
                        else:
                            alpha = min(255,alpha + int(255 - min(1, dist_src/self.light_range)*255)) 
                r = constants.LIGHT_SOURCE[self.style][3][0]
                g = constants.LIGHT_SOURCE[self.style][3][1]
                b = constants.LIGHT_SOURCE[self.style][3][2]
                a = constants.LIGHT_SOURCE[self.style][3][3]
                self.light_surf_mini.fill((r,g,b,max(0,255 - alpha - a)))
                self.light_surf.blit(self.light_surf_mini,(self.light_size_x*x,self.light_size_y*y))

    def move_light_effect(self, screen, cam_x, cam_y):
        if self.light_all_spots:
            self.light_screen_rect.top = 0
            self.light_screen_rect.left = cam_x + constants.SCREEN_X
        if self.light_only_robot:
            self.light_screen_rect.left = 0
            self.light_screen_rect.top = 0 - cam_y + constants.SCREEN_Y*1.5
        if self.light_only_screen_center:
            self.light_screen_rect.left = 0
            self.light_screen_rect.top = 0
        screen.blit(self.light_surf,(0,0), self.light_screen_rect)
