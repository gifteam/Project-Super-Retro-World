#Import basic librairies
import pyglet, sys
#Import personal packages
from classes import Theatre
from constants import constants

if __name__ == '__main__':

    Salle_de_theatre = Theatre.Salle_de_theatre()
    pyglet.clock.set_fps_limit(60)
    pyglet.clock.schedule_interval(Salle_de_theatre.update, 1/constants.FRAMES_PER_SECOND)

    pyglet.app.run()
    
