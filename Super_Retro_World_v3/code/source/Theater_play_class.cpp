//include standard libraries
#include <iostream>
//include custom Theater play class header
#include "../header/Theater_play_class.hpp"
//include custom Theater scene class header
#include "../header/Theater_scene_class.hpp"
//include constants struct
#include "../header/Constants.hpp"

//constructor
Theater_play::Theater_play(void)
{
    std::cout << "theater play constructor" << std::endl;
    name = "game";
}

//update
void Theater_play::update(int framerate)
{
    this->framerate = framerate;
    this->My_theater_scene.update(framerate);
}

void Theater_play::set_map(MAP* p_my_map)
{
    my_map = p_my_map;
    this->My_theater_scene.set_map(my_map);
}
