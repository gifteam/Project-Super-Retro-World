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
        //declaring general sprites variables
        std::vector<Sprite*> sprite_list;
        unsigned int current_sprite_id;
        //declaring collision variables and collision check function
        bool collidable;
        bool check_collision(void);
        //sprite others variables
        sf::Color origin_color;
        int previous_x;
        int previous_y;
        //declaring acceleration and speed in both axes (X anb Y)
        //Y
        float vertical_acceleration;
        float vertical_speed;
        float max_vertical_speed;
        //X
        float horizontal_acceleration;
        float horizontal_speed;
        float max_horizontal_speed;
        //declaring constructor
        Sprite(std::string s_type = "UNKNOWN");
        //classic update function
        void update(int framerate, std::vector<Sprite*> sprite_list, int sprite_id);
        //player physic update
        void update_player_direction(void);
        void update_player_movement(void);
        void update_gravity(void);
        //setter function
        void set_size(unsigned int w, unsigned int h);
};
#endif // _SPRITE_CLASS_
