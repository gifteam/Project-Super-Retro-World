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
    if (this->type.compare("PLAYER")==0 || this->type.compare("CAPPY")==0)
    {
        collide_with.push_back("SOLID");
    }
    //physic initialization
    vertical_acceleration = 500.0f;
    vertical_speed = 0.0f;
    max_vertical_speed = 400.0f;
    horizontal_acceleration = 700.0f;
    if (this->type.compare("CAPPY")==0)
    {
		horizontal_acceleration = 350.0f;
		max_vertical_speed = 600.0f;
	}
    horizontal_speed = 0.0f;
    max_horizontal_speed = 150.0f;
    //general initialization
	//background sprite
    background_layer = 0;
	//cappy sprite
	cappy_bounce = false;
	cappy_required = false;
	old_cappy_required = false;
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
		sprite_row_frame = 3;
		//current frame id
		sprite_frame = 0;
		//sprite row
		sprite_max_frame.push_back(0); //idle left
		sprite_max_frame.push_back(0); //idle right
		sprite_max_frame.push_back(11); //run left
		sprite_max_frame.push_back(11); //run right
		//sprite row speed
		sprite_framerate_factor = 1;
		sprite_framerate.push_back(1.0f); //idle left
		sprite_framerate.push_back(1.0f); //idle right
		sprite_framerate.push_back(0.1f); //run left
		sprite_framerate.push_back(0.1f); //run right
	}
}

//general update
void Sprite::update(int new_framerate, std::vector<Sprite*> new_sprite_list, int new_sprite_id)
{
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
    if (this->type.compare("CAPPY") == 0)
    {
		update_cappy(); //update cappy launch and movement
    }
}

void Sprite::update_frame(void)
{
	//simulate acceleration through frame update (usefull when running);
	sprite_framerate_factor =  1 + std::abs(float(horizontal_speed / max_horizontal_speed));

	//get the animation image set id
	if (sprite_clock.getElapsedTime().asSeconds() >= float(sprite_framerate[sprite_row_frame] / sprite_framerate_factor)){
		if (sprite_frame >= sprite_max_frame[sprite_row_frame])
		{
			sprite_frame = 0;
			sprite_rect.left = 0;
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

void Sprite::update_cappy(void)
{
	//launch cappy
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Space))
    {
		cappy_required = true;
    }
	//check if can be launch
	if (cappy_required && !old_cappy_required)
	{
		setPosition(get_player_position());
		move(get_player_width(), get_player_height()/2);
		horizontal_speed = get_player_horizontal_speed() + 400;
		vertical_speed = -100;
		cappy_life = 3*60;
		setColor(sf::Color(0, 0, 255, 255));
	}
	//update movement
	if (cappy_required && old_cappy_required)
	{
		//reduce cappy life time
		cappy_life -= 1;
	
		//reduce cappy horizontal speed
        if (horizontal_speed < 0){ horizontal_speed += horizontal_acceleration/this->framerate; }
        else if (horizontal_speed > 0){ horizontal_speed -= horizontal_acceleration/this->framerate; }

        if (horizontal_speed > (-1) * horizontal_acceleration/this->framerate && horizontal_speed < horizontal_acceleration/this->framerate){ horizontal_speed = 0; }
		
		update_gravity();
		update_movement();
		
		//bounce
		if (touch_right)
		{
			cappy_bounce = true;
			horizontal_speed = -300;
			vertical_speed = -100;
		}
		
		//attack
		if (cappy_attack)
		{
				cappy_attack = false;
				horizontal_speed = 0;
				vertical_speed = max_vertical_speed;
		}
		
		//delete
		if ((cappy_life == 0) || (horizontal_speed == 0 && touch_floor))
		{
			cappy_required = false;
			cappy_bounce = false;
			setColor(sf::Color(0, 0, 255, 0));
		}
	}
	
	old_cappy_required = cappy_required;
}

//update the player direction
void Sprite::update_player_direction(void)
{
    if ((sf::Keyboard::isKeyPressed(sf::Keyboard::Up) && touch_floor) || collide_bouncing_cappy())
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

//check if collide cappy (mode bounce activé)

bool Sprite::collide_bouncing_cappy(void)
{
	//create the collision rect of the current sprite
	sf::FloatRect rect(this->getPosition().x + offset_x, this->getPosition().y + offset_y, this->width,this->height);

    //loop with others sprites
    for (unsigned int i = 0 ; i < this->sprite_list.size() ; i++)
    {
		//check collision if the sprite must collide with the candidate
		if (this->sprite_list[i]->type.compare("CAPPY") == 0 && this->sprite_list[i]->cappy_bounce)
		{
			if (this->sprite_list[i]->getGlobalBounds().intersects(rect))
			{
				//collide with cappy
				//prepare cappy attack
				this->sprite_list[i]->cappy_attack = true;
				this->sprite_list[i]->cappy_bounce = false;
				return true;
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