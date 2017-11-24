#Import basic librairies
import pyglet
from pyglet.gl import *
#Import personal packages
from constants import constants

#event_info structure:
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# 0 = event ID from minimap color (RGB color value divide by 100 = trinary value)
#     possible values = 15 16 17 19 20 21 22 23 24 25 26
# 1 = filename "xxx" ( x = [0-9])
# 2 = 1 if top_left anchor_y, 0 if bottom left anchor_y 
# 3 = z
# 4 = True if animated, False overwise
# 5 = animated speed if animated
# [6.1 ; [6.2]] = 6.1: True if collidable, False overwise ; 6.2 (if collidable) : ["..." , "..."] side activation event: "LEFT", "RIGHT", "TOP", "BOTOM"
# 7 = -x, 0 or x = offset in X mesh (step 0.25)
# 8 = -x, 0 or x = offset in Y mesh (step 0.25)
# 9 = 0 (touch activation), 1 (click activation)
# 10 = IDLE/ACTIVE/SLEEP, event state
# 11 = array of anim sprite state
# 12 = If animated: loop = True/False
# 13 = from ACTIVE to SLEEP (False) or to IDLE (True)?

class Event(object):

    def __init__(self, my_scene):

        self.check_event = False
        self.my_scene = my_scene
        self.event_info = self.create_all_animations()
        self.event_list = None
        self.player_sprite = None
        self.textbox_sprite = None


    def get_event(self, my_scene):
        return self.event_info
    
   
    def create_all_animations(self):
        
        event_info = []
        event_info_tmp = []
        self.link_id_pos = {}
        my_ID = -1
        all_states = ["IDLE", "ACTIVE", "SLEEP"]
        
        if self.my_scene == "LEVEL_0_0":
            my_ID += 1
            EVENT_ID = 15
            event_info_tmp = [EVENT_ID, "006", 0, 300, True, 0.1, [False, None], 0, 0, 0, "IDLE", None, True, False]
            event_sequence = {}
            for id_state in range(len(all_states)):
                event_sequence[all_states[id_state]] = self.get_new_sequence(event_info_tmp, all_states[id_state])
            event_info_tmp[11] = event_sequence
            event_info.append(event_info_tmp)
            self.link_id_pos[EVENT_ID] = my_ID

        #color filter event whatever the level
        my_ID += 1
        event_info.append(self.add_colorfilter_to_event_list("RED", my_ID))
        my_ID += 1
        event_info.append(self.add_colorfilter_to_event_list("GREEN", my_ID))
        my_ID += 1
        event_info.append(self.add_colorfilter_to_event_list("BLUE", my_ID))

        return event_info


    def action(self):

        if self.scene == "LEVEL_0_0":
            self.action_LEVEL_0_0()


    def action_LEVEL_0_0(self):
        
        if self.event_id == 1 and not self.player_sprite.new_jump:
            if self.event_info[self.link_id_pos[self.event_id]][10] == "IDLE":
                self.event_info[self.link_id_pos[self.event_id]][10] = "ACTIVE"
                self.event_sprite.image = self.event_info[self.link_id_pos[self.event_id]][11]["ACTIVE"]
                #ACTION = = = = = = = = = = = = = = = = = =
                self.player_sprite.want_to_jump = True
            
        if self.event_id == 15:
            if self.event_info[self.link_id_pos[self.event_id]][10] == "IDLE":
                self.event_info[self.link_id_pos[self.event_id]][10] = "ACTIVE"
                self.event_sprite.image = self.event_info[self.link_id_pos[self.event_id]][11]["ACTIVE"]
                #ACTION = = = = = = = = = = = = = = = = = =
                self.textbox_sprite.x = 100 #self.event_sprite.x + 16 - self.textbox_sprite.image.width/2
                self.textbox_sprite.y = 100 #self.event_sprite.y + self.textbox_sprite.image.height
                self.textbox_sprite.opacity = 255

        # colorfilter event action
        if (self.event_id == 2 or self.event_id == 6 or self.event_id == 18) and self.event_sprite.collidable:
            self.event_sprite.opacity = 255
            

    def check_active_events(self):

        if self.event_info[self.link_id_pos[self.event_id]][10] == "ACTIVE":
            if self.event_sprite._frame_index >= len(self.event_sprite._animation.frames) - 1:
                if self.event_info[self.link_id_pos[self.event_id]][13]:
                    self.event_info[self.link_id_pos[self.event_id]][10] = "IDLE"
                    self.event_sprite.image = self.event_info[self.link_id_pos[self.event_id]][11]["IDLE"]
                else:
                    self.event_info[self.link_id_pos[self.event_id]][10] = "SLEEP"
                    self.event_sprite.image = self.event_info[self.link_id_pos[self.event_id]][11]["SLEEP"]
                    

    def check_colorfilter_event(self):

        if (self.event_info[self.link_id_pos[self.event_id]][0] == 2 or
            self.event_info[self.link_id_pos[self.event_id]][0] == 6 or
            self.event_info[self.link_id_pos[self.event_id]][0] == 18):

            self.event_sprite.collidable = False
            self.event_sprite.opacity = 0
            self.event_sprite.color = (0,0,0)

        if (self.event_info[self.link_id_pos[self.event_id]][0] == 2 and
            self.player_sprite.go_colorfilter_blue): #BLUE ID = 2

            self.event_sprite.collidable = True
            self.event_sprite.opacity = 150
            self.event_sprite.color = (0,0,255)

        elif (self.event_info[self.link_id_pos[self.event_id]][0] == 6 and
              self.player_sprite.go_colorfilter_green): #GREEN ID = 6

            self.event_sprite.collidable = True
            self.event_sprite.opacity = 150
            self.event_sprite.color = (0,255,0)
            
        elif (self.event_info[self.link_id_pos[self.event_id]][0] == 18 and
              self.player_sprite.go_colorfilter_red): #RED ID = 18

            self.event_sprite.collidable = True
            self.event_sprite.opacity = 150
            self.event_sprite.color = (255,0,0)

                    
    def update(self, my_scene):
        
        self.check_event = not self.check_event
        self.scene = my_scene
        
        if self.check_event:
            
            for event_id in range(len(self.event_list)):
                self.event_id = self.event_list[event_id][0][0]
                self.event_sprite = self.event_list[event_id][1]
                self.check_active_events()
                self.check_colorfilter_event()
                event_rect = self.event_list[event_id][1].get_rect()
                collision = self.event_list[event_id][0][6][0]
                side_collision = self.event_list[event_id][0][6][1]
                if self.activate_event_now(event_rect, self.player_sprite.rect, collision, side_collision):
                        if self.event_list[event_id][0][9] == 0:
                            #ACTION touch
                            self.action()
                        else:
                            #ACTION key
                            pass


    def activate_event_now(self, event_rect, target_rect, collision, side_collision):

        if not collision: #non collidable event
            if (event_rect[1] + event_rect[3]) >= (target_rect[1]) and (event_rect[1]) <= (target_rect[1] + target_rect[3]):
                if (event_rect[0] + event_rect[2]) >= (target_rect[0]) and (event_rect[0]) <= (target_rect[0] + target_rect[2]):
                    return True
                else:
                    return False
            else:
                return False
        else:
            result_bool = False
            for side in side_collision:
                if side == "LEFT":
                    if ((target_rect[0] == event_rect[0] - target_rect[2] - 1) and
                        (target_rect[1] > event_rect[1] - target_rect[3]) and
                        (target_rect[1] < event_rect[1] + event_rect[3])):
                        result_bool = True
                elif side == "RIGHT":
                    if ((target_rect[0] == event_rect[0] + event_rect[2] + 1) and
                        (target_rect[1] > event_rect[1] - target_rect[3]) and
                        (target_rect[1] < event_rect[1] + event_rect[3])):
                        result_bool = True
                elif side == "TOP":
                    if ((target_rect[1] == event_rect[1] + event_rect[3] + 1) and
                        (target_rect[0] > event_rect[0] - target_rect[2]) and
                        (target_rect[0] < event_rect[0] + event_rect[2])):
                        result_bool = True
                elif side == "BOTTOM":
                    if ((target_rect[1] == event_rect[1] - target_rect[3] - 1) and
                        (target_rect[0] > event_rect[0] - target_rect[2]) and
                        (target_rect[0] < event_rect[0] + event_rect[2])):
                        result_bool = True
            return result_bool

       
    def get_new_sequence(self, event_info_tmp, state):
        
        filename = event_info_tmp[1]
        sequence = None
        animation = None
        complete_image = pyglet.image.load(constants.PATH_EVENT + filename + ".png")
        loop, nb_frame, speed = event_info_tmp[12], int(complete_image.width/constants.SPRITE_X), event_info_tmp[5]
        if event_info_tmp[4]:
            offset_y = 0
            if state == "ACTIVE":
                offset_y = 1
            elif state == "SLEEP":
                offset_y = 2
            x, y, w, h = 0, complete_image.height - constants.SPRITE_Y * (offset_y + 1), complete_image.width, constants.SPRITE_Y
            region = complete_image.get_region(x, y, w, h)
            
            sequence = pyglet.image.ImageGrid(region, 1, nb_frame)
            nb_frame_tmp = nb_frame
            for frame in range(nb_frame_tmp): #adjust nb frames depending on black ones (useless)
                event_frame = sequence[frame].get_image_data().get_data('RGB', sequence[frame].width * 3)
                r = int(str(event_frame[0]))
                g = int(str(event_frame[0+1]))
                b = int(str(event_frame[0+2]))
                if r == 0 and g == 0 and b == 0:
                    nb_frame -= 1
            sequence = pyglet.image.ImageGrid(complete_image.get_region(x, y, nb_frame*constants.SPRITE_X, h), 1, nb_frame)        
            
            for img in sequence:
                self.anti_aliasied_texture(img)
            
            if nb_frame > 1:    
                animation = pyglet.image.Animation.from_image_sequence(sequence, speed, loop)
            else:
                animation = sequence[0]
        else:
            animation = complete_image
            
        return animation
    

    def add_colorfilter_to_event_list(self, color, my_ID):

        returned_event_info_colorfilter = [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        all_states = ["IDLE", "ACTIVE", "SLEEP"]
        
        if color == "BLUE":
            BLUE_ID = 2
            event_info_tmp = [BLUE_ID, "005", 0, 300, False, 0, [True, ["TOP"]], 0, 0, 0, "IDLE", None, False, True]
            event_sequence = {}
            for id_state in range(len(all_states)):
                event_sequence[all_states[id_state]] = self.get_new_sequence(event_info_tmp, all_states[id_state])
            event_info_tmp[11] = event_sequence
            returned_event_info_colorfilter = event_info_tmp
            self.link_id_pos[BLUE_ID] = my_ID

        elif color == "GREEN":
            GREEN_ID = 6
            event_info_tmp = [GREEN_ID, "005", 0, 300, False, 0, [True, ["TOP"]], 0, 0, 0, "IDLE", None, False, True]
            event_sequence = {}
            for id_state in range(len(all_states)):
                event_sequence[all_states[id_state]] = self.get_new_sequence(event_info_tmp, all_states[id_state])
            event_info_tmp[11] = event_sequence
            returned_event_info_colorfilter = event_info_tmp
            self.link_id_pos[GREEN_ID] = my_ID

        elif color == "RED":
            RED_ID = 18
            event_info_tmp = [RED_ID, "005", 0, 300, False, 0, [True, ["TOP"]], 0, 0, 0, "IDLE", None, False, True]
            event_sequence = {}
            for id_state in range(len(all_states)):
                event_sequence[all_states[id_state]] = self.get_new_sequence(event_info_tmp, all_states[id_state])
            event_info_tmp[11] = event_sequence
            returned_event_info_colorfilter = event_info_tmp
            self.link_id_pos[RED_ID] = my_ID

        return returned_event_info_colorfilter
    

    def anti_aliasied_texture(self, img):
        
        texture = img.get_texture()
        glBindTexture(texture.target, texture.id)
        glTexParameteri(texture.target,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        glBindTexture(texture.target,0)
