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
        sf::Texture* texture;
        std::string name;
        unsigned int width;
        unsigned int height;
        std::string type;
        int framerate;
        //declaring general sprites variables
        std::vector<Sprite*> sprite_list;
        unsigned int current_sprite_id;
        unsigned int background_layer;
        //declaring collision variables and collision check function
        bool collidable;
        bool collide_a_sprite(void);
        bool touch_roof;
        bool touch_floor;
        bool touch_left;
        bool touch_right;
        bool touch_one_direction; //old
        //sprite others variables
        float center_x;
        float center_y;
        float previous_x;
        float previous_y;
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
        //getter function
        void get_center_xy(void);
        std::string get_previous_area_before_hit(int sprite_collided_id);
        //checker function
        bool there_is_a_sprite_below(void);
        bool there_is_a_sprite_upside(void);
        bool there_is_a_sprite_left(void);
        bool there_is_a_sprite_right(void);
};
#endif // _SPRITE_CLASS_
