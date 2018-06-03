//include standard libraries
#include <iostream>
//include graphic library
#include <SFML/Graphics.hpp>
//include classic librairy
#include <iostream>
#include <string>
#include  <cstdlib>
#include <sstream>
#include <cmath>
//include custom Sprite class header
#include "../header/Sprite_class.hpp"

 int Sprite::current_filter = 0; // filter initialisation (0 -no filter-)

//include Sprite functions
#include "Sprite_class_init.cpp"
#include "Sprite_class_get.cpp"
#include "Sprite_class_set.cpp" 
#include "Sprite_class_update.cpp" 

//constructor
Sprite::Sprite(std::string new_type) : sf::Sprite::Sprite()
{
  
    std::cout << "Sprite constructor" << std::endl;
	
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
    //init physical hitbox offset
    offset_x = 0;
    offset_y = 0;
	
    //define the sprite type
    type = new_type;
    has_two_types = false;
    if (this->type.compare("PLAYER")==0)
    {
        collide_with.push_back("SOLID_RED");
		collide_with.push_back("SOLID_GREEN");
		collide_with.push_back("SOLID_BLUE");
		collide_with.push_back("SOLID");
    }
    if (this->type.compare("TRANSPARENT_RED")==0)
    {
        has_two_types = true;
        second_type = "SOLID_RED";
        first_type = type;
        second_type_activated = false;
		collide_with.push_back("PLAYER");
		collide_with.push_back("SOLID_MOVING_HORIZONTAL");
    }
    if (this->type.compare("TRANSPARENT_GREEN")==0)
    {
        has_two_types = true;
        second_type = "SOLID_GREEN";
        first_type = type;
        second_type_activated = false;
		collide_with.push_back("PLAYER");
		collide_with.push_back("SOLID_MOVING_HORIZONTAL");
    }
    if (this->type.compare("TRANSPARENT_BLUE")==0)
    {
        has_two_types = true;
        second_type = "SOLID_BLUE";
        first_type = type;
        second_type_activated = false;
		collide_with.push_back("PLAYER");
		collide_with.push_back("SOLID_MOVING_HORIZONTAL");
    }
    if (this->type.compare("SOLID_MOVING_HORIZONTAL")==0)
    {
		moving_sprite_horizontal_direction = false; // 0 for LEFT and 1 for RIGHT
		moving_sprite_horizontal_speed = 40 + rand() %10; // horizontal speed of the sprite
		horizontal_speed = moving_sprite_horizontal_speed;
		moving_sprite_vertical_direction = false; // 0 for UP and 1 for DOWN
		moving_sprite_vertical_speed = 0; // vertical speed of the sprite
		vertical_speed = moving_sprite_vertical_speed;
        collide_with.push_back("SOLID");
		collide_with.push_back("SOLID_MOVING_HORIZONTAL");
        collide_with.push_back("SOLID_RED");
		collide_with.push_back("SOLID_GREEN");
		collide_with.push_back("SOLID_BLUE");
    }
    if (this->type.compare("COIN")==0)
    {
		collected = false;
    }
    //sprite rect (visual)
    initialize_visual_sprite_attributes();
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
  update_filter_color(); //update filter color
  //update player sprite
  if (this->type.compare("PLAYER") == 0)
  {
    update_filter_activation();
    update_frame(); //update the current frame of the animation
    update_player_direction(); //horizontal speed update
    update_gravity(); //vertical speed update
    update_movement(); //move the player
	update_collect(); // check if the current sprite collect a COIN sprite
  }
  
  if (this->type.compare("SOLID_MOVING_HORIZONTAL") == 0)
  {
    //update_filter_activation();
    //update_frame(); //update the current frame of the animation
    //update_moving_sprite_direction(); //horizontal speed update
    update_moving_sprite_direction_and_movement(); //move the moving sprite
  }
  
	update_hitbox_mode(); //update the hitbox texture (on / off)
}



