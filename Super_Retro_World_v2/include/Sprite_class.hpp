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
        unsigned int width;
        unsigned int height;
        std::string type;
        int framerate;
        //declaring constructor
        Sprite(std::string s_type = "UNKNOWN");
        //classic update function
        void update(int framerate);
        void update_player(void);
        //setter function
        void set_size(unsigned int w, unsigned int h);
};
#endif // _SPRITE_CLASS_
