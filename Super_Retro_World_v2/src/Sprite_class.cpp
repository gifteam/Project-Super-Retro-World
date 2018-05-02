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
    acceleration = 2.0f;
    speed = 0.0f;
}

void Sprite::update(int framerate)
{
    this->framerate = framerate;
    //update player sprite
    if (this->type.compare("PLAYER") == 0)
    {
        update_player();
        update_gravity();
    }
}

//update the physical part of the sprites
//update the gravity
void Sprite::update_gravity(void)
{
    speed += acceleration;
    this->move(0.0f, speed/this->framerate);
}


//update the player movements
void Sprite::update_player(void)
{
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
    {
        std::cout << "left" << std::endl;
        this->move(-100.0f/this->framerate, 0.0f);
    }
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
    {
        std::cout << "right" << std::endl;
        this->move(100.0f/this->framerate, 0.0f);
    }
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up))
    {
        std::cout << "up" << std::endl;
        this->move(0.0f, -100.0f/this->framerate);
    }
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down))
    {
        std::cout << "down" << std::endl;
        this->move(0.0f, 100.0f/this->framerate);
    }
}

//set new size
void Sprite::set_size(unsigned int w, unsigned int h)
{
    width = w;
    height = h;
}
