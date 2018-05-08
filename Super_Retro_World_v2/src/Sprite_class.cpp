//include standard libraries
#include <iostream>
//include graphic library
#include <SFML/Graphics.hpp>
//include custom Sprite class header
#include "../include/Sprite_class.hpp"

//constructor
Sprite::Sprite(std::string s_type) : sf::Sprite::Sprite()
{
    std::cout << "Sprite constructor" << std::endl;
    //define the sprite type
    type = s_type;
    vertical_acceleration = 200.0f;
    vertical_speed = 0.0f;
    max_vertical_speed = 200.0f;
    horizontal_acceleration = 500.0f;
    horizontal_speed = 0.0f;
    max_horizontal_speed = 100.0f;
}

void Sprite::update(int framerate, std::vector<Sprite*> sprite_list, int sprite_id)
{
    this->framerate = framerate;
    //update player sprite
    if (this->type.compare("PLAYER") == 0)
    {
        update_player_direction(); //horizontal speed update
        update_gravity(); //vertical speed update
        update_collision(); //correction of the trajectory
        update_player_movement(); //move the player accordingly
    }
}

//update the physical part of the sprites
//update the gravity
void Sprite::update_gravity(void)
{
    if (vertical_speed + vertical_acceleration/this->framerate <= max_vertical_speed) { vertical_speed += vertical_acceleration/this->framerate; }
    //this->move(0.0f, vertical_speed/this->framerate);
}

//update the collision with others sprites
void Sprite::update_collision(void)
{
    float current_x = this->getPosition().x;
    float current_y = this->getPosition().y;
    float dest_x = current_x + horizontal_speed;
    float dest_y = current_y + vertical_speed;
}

//update player movement
void Sprite::update_player_movement(void)
{
    this->move(horizontal_speed/this->framerate, vertical_speed/this->framerate);
}

//update the player direction
void Sprite::update_player_direction(void)
{
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
    {
        if (horizontal_speed - horizontal_acceleration/this->framerate >= (-1) * max_horizontal_speed) { horizontal_speed -= horizontal_acceleration/this->framerate; }
    }
    else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
    {
        if (horizontal_speed + horizontal_acceleration/this->framerate <= max_horizontal_speed) { horizontal_speed += horizontal_acceleration/this->framerate; }
    }
    else
    {
        if (horizontal_speed < 0)
        {
            horizontal_speed += horizontal_acceleration/this->framerate;
        }
        else if (horizontal_speed > 0)
        {
            horizontal_speed -= horizontal_acceleration/this->framerate;
        }

        if (horizontal_speed > (-1) * horizontal_acceleration/this->framerate && horizontal_speed < horizontal_acceleration/this->framerate)
        {
            horizontal_speed = 0;
        }
    }
}

//set new size
void Sprite::set_size(unsigned int w, unsigned int h)
{
    width = w;
    height = h;
}
