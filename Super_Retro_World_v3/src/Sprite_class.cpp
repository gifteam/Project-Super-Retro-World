//include standard libraries
#include <iostream>
//include graphic library
#include <SFML/Graphics.hpp>
//include custom Sprite class header
#include "../include/Sprite_class.hpp"
//include classic librairy
#include <iostream>
#include <string>
#include <sstream>
#include <cmath> 

//constructor
Sprite::Sprite(std::string new_type) : sf::Sprite::Sprite()
{
    std::cout << "Sprite constructor" << std::endl;
    //define the sprite type
    type = new_type;
    if (this->type.compare("PLAYER")==0)
    {
        collide_with.push_back("SOLID");
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

//initialisation of all visual sprite attributes 
void Sprite::initialize_visual_sprite_attributes(void)
{
	//player init
	if (this->type.compare("PLAYER")==0)
	{
		//rect for spritesheet
		sprite_rect.left = 0;
		sprite_rect.top = 0;
		sprite_rect.width = 32;
		sprite_rect.height = 32;
		//row frame
		sprite_row_frame = 1;
		sprite_previous_row_frame = sprite_row_frame;
		//current frame id
		sprite_frame = 0;
		//sprite row
		sprite_max_frame.push_back(0); //idle left
		sprite_max_frame.push_back(0); //idle right
		sprite_max_frame.push_back(11); //run left
		sprite_max_frame.push_back(11); //run right
		sprite_max_frame.push_back(1); //edge left
		sprite_max_frame.push_back(1); //edge right
		sprite_max_frame.push_back(0); //fall left
		sprite_max_frame.push_back(0); //fall right
		sprite_max_frame.push_back(0); //jump left
		sprite_max_frame.push_back(0); //jump right
		//sprite row speed
		sprite_framerate_factor = 1;
		sprite_framerate.push_back(0.1); //idle left
		sprite_framerate.push_back(0.1); //idle right
		sprite_framerate.push_back(0.1f); //run left
		sprite_framerate.push_back(0.1f); //run right
		sprite_framerate.push_back(0.25f); //edge left
		sprite_framerate.push_back(0.25f); //edge right
		sprite_framerate.push_back(0.25f); //fall left
		sprite_framerate.push_back(0.25f); //fall right
		sprite_framerate.push_back(0.25f); //jump left
		sprite_framerate.push_back(0.25f); //jump right
	}
}

//general update
void Sprite::update(int new_framerate, std::vector<Sprite*> new_sprite_list, int new_sprite_id, bool hit_mode)
{
	hitbox_mode = hit_mode;
    this->framerate = new_framerate;
    this->sprite_list = new_sprite_list;
    this->current_sprite_id = new_sprite_id;
    //update player sprite
    if (this->type.compare("PLAYER") == 0)
    {
        update_frame(); //update the current frame of the animation
		update_player_direction(); //horizontal speed update
        update_gravity(); //vertical speed update
        update_movement(); //move the player
    }
	update_hitbox_mode();
}

void Sprite::update_hitbox_mode(void)
{
//change image if hitbox mode is one
    if (hitbox_mode)
    {
        setTexture(*hitbox_texture);
	}
    else
    {
        setTexture(*texture);
    }
//end of procedure
}

void Sprite::update_frame(void)
{
	//simulate acceleration through frame update (usefull when running);
	sprite_framerate_factor =  1 + std::abs(float(horizontal_speed / max_horizontal_speed));

	//update global animation (select row)
	update_row_frame();
	
	//reset frame if changing row
	if (sprite_row_frame != sprite_previous_row_frame) { sprite_frame = 0; }
	sprite_previous_row_frame = sprite_row_frame;
	
	//get the animation image set id
	if (sprite_clock.getElapsedTime().asSeconds() >= float(sprite_framerate[sprite_row_frame] / sprite_framerate_factor)){
		if (sprite_frame >= sprite_max_frame[sprite_row_frame])
		{
			sprite_frame = 0;
		}else{
			sprite_frame += 1;
		}
		//update rect position and size
		sprite_rect.left = sprite_frame * 32;
		sprite_rect.top = sprite_row_frame * 32;
		setTextureRect(sprite_rect);
		sprite_clock.restart();
	}
	//end of the procedure
}

void Sprite::update_row_frame(void)
{
    if (this->type.compare("PLAYER") == 0)
    {
		if (vertical_speed == 0){
			if (horizontal_speed < 0) { sprite_row_frame = 2;} //running left
			else if (horizontal_speed > 0) { sprite_row_frame = 3;} //running right
			else { sprite_row_frame = 1;} //idle right
		}
		else if (vertical_speed < 0){
			if (horizontal_speed < 0) { sprite_row_frame = 8;} //jumping left
			else if (horizontal_speed >= 0) { sprite_row_frame = 9;} //jumping right
		}
		else if (vertical_speed > 0){
			if (horizontal_speed < 0) { sprite_row_frame = 6;} //falling left
			else if (horizontal_speed >= 0) { sprite_row_frame = 7;} //falling right
		}
	}
}

//update the physical part of the sprites
//update the gravity
void Sprite::update_gravity(void)
{
    if (!touch_floor && vertical_speed + vertical_acceleration/this->framerate <= max_vertical_speed) { vertical_speed += vertical_acceleration/this->framerate; }
}

//update player movement
void Sprite::update_movement(void)
{
    //get last good position collision-free
    previous_x = this->getPosition().x;
    previous_y = this->getPosition().y;
	 //try to move
    this->move(horizontal_speed/this->framerate, vertical_speed/this->framerate);
    //declare local x + y to determine best location if collide
    float delta_x = (-1) * (this->getPosition().x - previous_x)/10;
    float delta_y = (-1) * (this->getPosition().y - previous_y)/10;
    while (collide_a_sprite("")) //test if there is a collision with a solid sprite
    {
        //move back to the first correct position
        this->move(sf::Vector2f(delta_x, delta_y));
    }
	//check if touch a sprite
    touch_floor = false;
    touch_roof = false;
    touch_left = false;
    touch_right = false;
    if (collide_a_sprite("DOWN")) {vertical_speed = 0; touch_floor = true;}
    if (collide_a_sprite("UP")) {vertical_speed = 0; touch_roof = true;}
    if (collide_a_sprite("LEFT")) {horizontal_speed = 0; touch_left = true;}
    if (collide_a_sprite("RIGHT")) {horizontal_speed = 0; touch_right = true;}
}


//update the player direction
void Sprite::update_player_direction(void)
{	
	if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up) && touch_floor)
    {
        vertical_speed = -350;
    }
	// ask for reset position
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Escape))
    {
        setPosition(sf::Vector2f(0, 0));
    }
	//check keyboard <- and -> pressure
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left) && !touch_left)
    {
        horizontal_speed -= horizontal_acceleration/this->framerate;
        if (horizontal_speed < (-1) * max_horizontal_speed) { horizontal_speed = (-1) * max_horizontal_speed; }
    }
    else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right) && !touch_right)
    {
        horizontal_speed += horizontal_acceleration/this->framerate;
        if (horizontal_speed > max_horizontal_speed) { horizontal_speed = max_horizontal_speed; }
    }
    else
    {
        if (horizontal_speed < 0){ horizontal_speed += horizontal_acceleration/this->framerate; }
        else if (horizontal_speed > 0){ horizontal_speed -= horizontal_acceleration/this->framerate; }

        if (horizontal_speed > (-1) * horizontal_acceleration/this->framerate && horizontal_speed < horizontal_acceleration/this->framerate){ horizontal_speed = 0; }
    }
}

//set new size
void Sprite::set_size(unsigned int w, unsigned int h)
{
    width = w;
    height = h;
}

//set new size
void Sprite::set_hitbox(int off_x, int off_y, unsigned int w, unsigned int h)
{
    offset_x = off_x;
	offset_y = off_y;
	set_size(w, h);
}

//check the collision
bool Sprite::collide_a_sprite(std::string direction)
{
	//create the collision rect of the current sprite
	bool have_to_check_collision = false;
	sf::FloatRect rect(this->getPosition().x + offset_x, this->getPosition().y + offset_y, this->width,this->height);
	if (direction.compare("RIGHT") == 0) { rect.left = rect.left + 1; }
	else if (direction.compare("LEFT") == 0) { rect.left = rect.left - 1; }
	else if (direction.compare("DOWN") == 0) { rect.top = rect.top + 1; }
	else if (direction.compare("UP") == 0) { rect.top = rect.top - 1; }

    //loop with others sprites
    for (unsigned int i = 0 ; i < this->sprite_list.size() ; i++)
    {
		have_to_check_collision = false;
		for (unsigned int j = 0 ; j < this->collide_with.size() ; j++)
		 {
			if (this->collide_with[j].compare(this->sprite_list[i]->type) == 0)
			{
				have_to_check_collision = true;
			}
            //check collision if the sprite must collide with the candidate
			if (have_to_check_collision)
			{
				if (this->sprite_list[i]->getGlobalBounds().intersects(rect))
				{
					//collide
					return true;
				}
			}
        }
    }
    //dont collide
    return false;
}

//calculation of center of the Sprite
void Sprite::get_center_xy(void)
{
    float x = this->getPosition().x;
    float y = this->getPosition().x;
    float w = this->width;
    float h = this->height;

    center_x = x + w/2;
    center_y = y + h/2;

}

//get player height whoever ask for it
float Sprite::get_player_height(void)
{
	for (unsigned int i = 0 ; i < this->sprite_list.size() ; i++)
	{
		if (this->sprite_list[i]->type.compare("PLAYER") == 0) { return this->sprite_list[i]->height; }
	}
	return 0;
}

//get player horizontal speed whoever ask for it
float Sprite::get_player_width(void)
{
	for (unsigned int i = 0 ; i < this->sprite_list.size() ; i++)
	{
		if (this->sprite_list[i]->type.compare("PLAYER") == 0) { return this->sprite_list[i]->width; }
	}
	return 0;
}

//get player horizontal speed whoever ask for it
float Sprite::get_player_horizontal_speed(void)
{
	for (unsigned int i = 0 ; i < this->sprite_list.size() ; i++)
	{
		if (this->sprite_list[i]->type.compare("PLAYER") == 0) { return this->sprite_list[i]->horizontal_speed; }
	}
	return 0;
}

//get player position whoever ask for it
sf::Vector2f Sprite::get_player_position(void)
{
	for (unsigned int i = 0 ; i < this->sprite_list.size() ; i++)
	{
		if (this->sprite_list[i]->type.compare("PLAYER") == 0) { return this->sprite_list[i]->get_position(); }
	}
	return sf::Vector2f(0,0);
}

//get itself position
sf::Vector2f Sprite::get_position(void)
{
	return sf::Vector2f(this->getPosition().x, this->getPosition().y);
}