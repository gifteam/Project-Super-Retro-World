//include standard libraries
#include <iostream>
//include graphic library
#include <SFML/Graphics.hpp>
//include custom Sprite class header
#include "/home/ayoub/Project-Super-Retro-World/cpp_project/Super_Retro_World/include/Sprite_class.hpp"

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
