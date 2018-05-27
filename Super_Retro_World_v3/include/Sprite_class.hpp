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
		//visual sprite attributes
        sf::Texture* texture;
		sf::Texture* hitbox_texture;
		sf::IntRect sprite_rect;
		sf::Clock sprite_clock;
		unsigned int sprite_row_frame;
		unsigned int sprite_previous_row_frame;
		unsigned int sprite_frame;
		std::vector<unsigned int> sprite_max_frame;
		std::vector<float> sprite_framerate;
		float sprite_framerate_factor;
        std::string name;
		//physical sprite
		int offset_x;
		int offset_y;
        unsigned int width;
        unsigned int height;
        std::string type;
        int framerate;
        //declaring general sprites variables
		bool hitbox_mode;
        std::vector<Sprite*> sprite_list;
        unsigned int current_sprite_id;
        unsigned int background_layer;
        //declaring collision variables and collision check function
        std::vector<std::string> collide_with;
        bool collide_a_sprite(std::string direction);
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
		//declaring player oriented variables

        //declaring constructor
        Sprite(std::string s_type = "UNKNOWN");
		
		//initialization functions
		void initialize_visual_sprite_attributes(void);
		
        //update functions
        void update(int framerate, std::vector<Sprite*> sprite_list, int sprite_id, bool hitbox_mode);
        void update_player_direction(void);
        void update_movement(void);
        void update_gravity(void);
		void update_frame(void);
		void update_row_frame(void);
		void update_hitbox_mode(void);
        //setter function
		void set_hitbox(int off_x, int off_y, unsigned int w, unsigned int h);
        void set_size(unsigned int w, unsigned int h);
        //getter function
        void get_center_xy(void);
		sf::Vector2f get_player_position(void);
		sf::Vector2f get_position(void);
        float get_player_horizontal_speed(void);
		float get_player_height(void);
		float get_player_width(void);
};
#endif // _SPRITE_CLASS_
