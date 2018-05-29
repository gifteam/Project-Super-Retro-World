//include standard libraries
#include <iostream>
//include graphic library
#include <SFML/Graphics.hpp>
//include classic librairy
#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
//include custom Sprite class header
#include "../include/Sprite_class.hpp"

 int Sprite::current_filter = 0; // filter initialisation (0 -no filter-)

//include Sprite functions
#include "../src/Sprite_class_init.cpp"
#include "../src/Sprite_class_get.cpp"
#include "../src/Sprite_class_set.cpp" 
#include "../src/Sprite_class_update.cpp" 

//constructor
Sprite::Sprite(std::string new_type) : sf::Sprite::Sprite()
{
  
    std::cout << "Sprite constructor" << std::endl;
    //define the sprite type
    type = new_type;
    has_two_types = false;
    if (this->type.compare("PLAYER")==0)
    {
        collide_with.push_back("SOLID");
        collide_with.push_back("SOLID_RED");
    }
    if (this->type.compare("SOLID_RED")==0)
    {
        has_two_types = true;
        second_type = "TRANSPARENT_RED";
        first_type = type;
        second_type_activated = false;
    }
    //physic initialization
    vertical_acceleration = 500.0f;
    vertical_speed = 0.0f;
    max_vertical_speed = 400.0f;
    horizontal_acceleration = 700.0f;
    horizontal_speed = 0.0f;
    max_horizontal_speed = 150.0f;
    //general initialization
    //background sprite
    background_layer = 0;
    //sprite rect (visual)
    initialize_visual_sprite_attributes();
    //init physical hitbox offset
    offset_x = 0;
    offset_y = 0;
}

//general update
void Sprite::update(int new_framerate, std::vector<Sprite*> new_sprite_list, int new_sprite_id, bool hit_mode)
{
  hitbox_mode = hit_mode;
  this->framerate = new_framerate;
  this->sprite_list = new_sprite_list;
  this->current_sprite_id = new_sprite_id;
  //update filter types
  update_filter_type(); // change type according to current filter
  //update player sprite
  if (this->type.compare("PLAYER") == 0)
  {
    update_filter_activation();
    update_frame(); //update the current frame of the animation
    update_player_direction(); //horizontal speed update
    update_gravity(); //vertical speed update
    update_movement(); //move the player
  }
	update_hitbox_mode(); //update the hitbox texture (on / off)
}