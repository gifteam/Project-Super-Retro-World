//include standard libraries
#include <iostream>
//include graphic library
#include <SFML/Graphics.hpp>
//include custom Sprite class header
#include "Sprite_class.h"

//constructor
Sprite::Sprite() : sf::Sprite::Sprite()
{
    std::cout << "Sprite constructor" << std::endl;
    //initializing every sprite attributes
    //...
}

void Sprite::update(void)
{

}
