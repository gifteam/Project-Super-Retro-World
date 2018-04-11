#ifndef _THEATRE_PLAY_CLASS_
//define the theater play class (game)
#define _THEATRE_PLAY_CLASS_
//include standard library
#include <string>
//include custom Theater scene class header
#include "Theater_scene_class.h"

//class declaration
class Theater_play
{
    public:
        //declaring theater scene (level)
        Theater_scene My_theater_scene;
        //declaring public game attributes
        std::string name = "";
        //declaring constructor
        Theater_play();
        //declaring classic functions
        void update();
};

#endif // _THEATRE_PLAY_CLASS_
