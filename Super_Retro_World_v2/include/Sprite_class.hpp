#ifndef _SPRITE_CLASS_
//define the sprite class (object)
#define _SPRITE_CLASS_
//include graphic library
#include <SFML/Graphics.hpp>
//include standard library
#include <vector>

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
        //declaring physical part
        float vertical_acceleration;
        float vertical_speed;
        float max_vertical_speed;
        float horizontal_acceleration;
        float horizontal_speed;
        float max_horizontal_speed;
        //declaring constructor
        Sprite(std::string s_type = "UNKNOWN");
        //classic update function
        void update(int framerate, std::vector<Sprite*> sprite_list, int sprite_id);
        //physic update
        void update_player_direction(void);
        void update_player_movement(void);
        void update_gravity(void);
        void update_collision(void);
        //setter function
        void set_size(unsigned int w, unsigned int h);
};
#endif // _SPRITE_CLASS_
