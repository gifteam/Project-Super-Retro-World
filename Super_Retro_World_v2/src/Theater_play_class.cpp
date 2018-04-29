//include standard libraries
#include <iostream>
//include custom Theater play class header
#include "../include/Theater_play_class.hpp"
//include custom Theater scene class header
#include "../include/Theater_scene_class.hpp"
//include constants struct
#include "../include/Constants.hpp"

//constructor
Theater_play::Theater_play(void)
{
    std::cout << "theater play constructor" << std::endl;
    name = "game";
}

//update
void Theater_play::update()
{
    this->My_theater_scene.update();
}

void Theater_play::set_map(MAP* p_my_map)
{
    my_map = p_my_map;
    this->My_theater_scene.set_map(my_map);
}
