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

//constructor
Sprite::Sprite(std::string new_type) : sf::Sprite::Sprite()
{
    std::cout << "Sprite constructor" << std::endl;
    //define the sprite type
    type = new_type;
    collidable = false;
    if (this->type.compare("SOLID")==0 || this->type.compare("PLAYER")==0)
    {
        collidable = true;
    }
    vertical_acceleration = 400.0f;
    vertical_speed = 0.0f;
    max_vertical_speed = 400.0f;
    horizontal_acceleration = 700.0f;
    horizontal_speed = 0.0f;
    max_horizontal_speed = 150.0f;
}

void Sprite::update(int new_framerate, std::vector<Sprite*> new_sprite_list, int new_sprite_id)
{
    this->framerate = new_framerate;
    this->sprite_list = new_sprite_list;
    this->current_sprite_id = new_sprite_id;
    //update player sprite
    if (this->type.compare("PLAYER") == 0)
    {
        update_player_direction(); //horizontal speed update
        update_gravity(); //vertical speed update
        update_player_movement(); //move the player
    }
}

//update the physical part of the sprites
//update the gravity
void Sprite::update_gravity(void)
{
    if (!touch_floor && vertical_speed + vertical_acceleration/this->framerate <= max_vertical_speed) { vertical_speed += vertical_acceleration/this->framerate; }
}

//update player movement
void Sprite::update_player_movement(void)
{
    //get last good position collision-free
    previous_x = this->getPosition().x;
    previous_y = this->getPosition().y;
    //try to move
    this->move(horizontal_speed/this->framerate, vertical_speed/this->framerate);
    //declare local x + y to determine best location if collide
    float delta_x = (-1) * (this->getPosition().x - previous_x)/10;
    float delta_y = (-1) * (this->getPosition().y - previous_y)/10;
    std::cout << "[" << this->getPosition().x << ";" << this->getPosition().y << "]";
    while (collide_a_sprite() && !touch_one_direction) //test if there is a collision with a solid sprite
    {
        //move back to the first correct position
        this->move(sf::Vector2f(delta_x, delta_y));
        std::cout << delta_x << " - " << delta_y << std::endl;
    }

    std::cout << "[" << this->getPosition().x << ";" << this->getPosition().y << "]" << std::endl;
    touch_floor = false;
    touch_roof = false;
    touch_left = false;
    touch_right = false;
    touch_one_direction = false;
    if (there_is_a_sprite_below()) {vertical_speed = 0; touch_floor = true;}
    if (there_is_a_sprite_upside()) {vertical_speed = 0; touch_roof = true;}
    if (there_is_a_sprite_left()) {horizontal_speed = 0; touch_left = true;}
    if (there_is_a_sprite_right()) {horizontal_speed = 0; touch_right = true;}
    if (touch_floor || touch_roof || touch_left || touch_right) {touch_one_direction = true;}
}

//update the player direction
void Sprite::update_player_direction(void)
{
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up) && touch_floor)
    {
        vertical_speed = -250;
    }
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

//check the collision
bool Sprite::collide_a_sprite(void)
{
    //loop with others sprites
    for (unsigned int i = 0 ; i < this->sprite_list.size() ; i++)
    {
        //avoid himself
        if (i != this->current_sprite_id && this->collidable && this->sprite_list[i]->collidable)
        {
            //check collision
            if (this->sprite_list[i]->getGlobalBounds().intersects(this->getGlobalBounds()))
            {
                //collide
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

//return true if there is a sprite below
bool Sprite::there_is_a_sprite_below(void)
{
    //define local rect to determine if there is something below (check with y + 1 pixel)
    sf::FloatRect rect(previous_x, previous_y + 1, this->width,this->height);
    //loop with others sprites
    for (unsigned int i = 0 ; i < this->sprite_list.size() ; i++)
    {
        //avoid himself
        if (i != this->current_sprite_id && this->collidable && this->sprite_list[i]->collidable)
        {
            //check collision
            if (this->sprite_list[i]->getGlobalBounds().intersects(rect))
            {
                return true;
            }
        }
    }
    return false;
}

//return true if there is a sprite upside
bool Sprite::there_is_a_sprite_upside(void)
{
    //define local rect to determine if there is something upside (check with y - 1 pixel)
    sf::FloatRect rect(previous_x, previous_y - 1, this->width,this->height);
    //loop with others sprites
    for (unsigned int i = 0 ; i < this->sprite_list.size() ; i++)
    {
        //avoid himself
        if (i != this->current_sprite_id && this->collidable && this->sprite_list[i]->collidable)
        {
            //check collision
            if (this->sprite_list[i]->getGlobalBounds().intersects(rect))
            {
                return true;
            }
        }
    }
    return false;
}

//return true if there is a sprite left
bool Sprite::there_is_a_sprite_left(void)
{
    //define local rect to determine if there is something left (check with x - 1 pixel)
    sf::FloatRect rect(previous_x - 1, previous_y, this->width,this->height);
    //loop with others sprites
    for (unsigned int i = 0 ; i < this->sprite_list.size() ; i++)
    {
        //avoid himself
        if (i != this->current_sprite_id && this->collidable && this->sprite_list[i]->collidable)
        {
            //check collision
            if (this->sprite_list[i]->getGlobalBounds().intersects(rect))
            {
                return true;
            }
        }
    }
    return false;
}

//return true if there is a sprite right
bool Sprite::there_is_a_sprite_right(void)
{
    //define local rect to determine if there is something right (check with x + 1 pixel)
    sf::FloatRect rect(previous_x + 1, previous_y, this->width,this->height);
    //loop with others sprites
    for (unsigned int i = 0 ; i < this->sprite_list.size() ; i++)
    {
        //avoid himself
        if (i != this->current_sprite_id && this->collidable && this->sprite_list[i]->collidable)
        {
            //check collision
            if (this->sprite_list[i]->getGlobalBounds().intersects(rect))
            {
                return true;
            }
        }
    }
    return false;
}
