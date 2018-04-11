#ifndef _SPRITE_CLASS_
//define the sprite class (object)
#define _SPRITE_CLASS_
//include graphic library
#include <SFML/Graphics.hpp>

//class declaration
class Sprite: public sf::Sprite
{
    public:
        //declaring public sprite attributes
        sf::CircleShape shape;
        sf::Texture* texture;
        std::string name;
        unsigned int x;
        unsigned int y;
        unsigned int width;
        unsigned int height;
        //declaring constructor
        Sprite();
        void update(void);
};
#endif // _SPRITE_CLASS_
