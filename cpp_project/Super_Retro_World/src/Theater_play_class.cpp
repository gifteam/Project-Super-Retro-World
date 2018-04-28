//include standard libraries
#include <iostream>
//include custom Theater play class header
#include ""/home/ayoub/Project-Super-Retro-World/cpp_project/Super_Retro_World/include/Theater_play_class.h"
//include custom Theater scene class header
#include ""/home/ayoub/Project-Super-Retro-World/cpp_project/Super_Retro_World/include/Theater_scene_class.h"

//constructor
Theater_play::Theater_play(void)
{
    std::cout << "theater play constructor" << std::endl;
    name = "game";
}

//update
void Theater_play::update(void)
{
    this->My_theater_scene.update();
}
