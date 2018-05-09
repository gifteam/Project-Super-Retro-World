//include standard libraries
#include <iostream>
//include graphic library
#include <SFML/Graphics.hpp>
//include custom Sprite class header
#include "../include/Sprite_class.hpp"

//constructor
Sprite::Sprite(std::string new_type) : sf::Sprite::Sprite()
{
    std::cout << "Sprite constructor" << std::endl;
    //define the sprite type
    type = new_type;
    collidable = false;
    origin_color = getColor();
    if (this->type.compare("SOLID")==0 || this->type.compare("PLAYER")==0)
    {
        collidable = true;
    }
    vertical_acceleration = 200.0f;
    vertical_speed = 0.0f;
    max_vertical_speed = 200.0f;
    horizontal_acceleration = 500.0f;
    horizontal_speed = 0.0f;
    max_horizontal_speed = 100.0f;
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
    if (vertical_speed + vertical_acceleration/this->framerate <= max_vertical_speed) { vertical_speed += vertical_acceleration/this->framerate; }
}

//update the collision with others sprites
bool Sprite::check_collision(void)
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
                //collide !
                return true;
            }
        }
    }
    //no collision found
    return false;
}

//update player movement
void Sprite::update_player_movement(void)
{
    //get last good position
    previous_x = this->getPosition().x;
    previous_y = this->getPosition().y;
    //try to move
    this->move(horizontal_speed/this->framerate, vertical_speed/this->framerate);
    //check collision
    if (check_collision())
    {
        //if there is a collision, get the bad position
        int current_x = this->getPosition().x;
        int current_y = this->getPosition().y;
        float vector_x = current_x - previous_x;
        float vector_y = current_y - previous_y;
        //set to last good position
        this->setPosition(sf::Vector2f(previous_x, previous_y));
        //todo: detect collision side to perform speed adjustment
        vertical_speed = 0;
    }
}

//update the player direction
void Sprite::update_player_direction(void)
{
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up))
    {
        vertical_speed = -200;
    }

    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
    {
        horizontal_speed -= horizontal_acceleration/this->framerate;
        if (horizontal_speed < (-1) * max_horizontal_speed) { horizontal_speed = (-1) * max_horizontal_speed; }
    }
    else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
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
