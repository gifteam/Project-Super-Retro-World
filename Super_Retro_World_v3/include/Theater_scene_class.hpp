#ifndef _THEATER_SCENE_CLASS_
//define the theater scene class (level)
#define _THEATER_SCENE_CLASS_
//include standard library
#include <string>
#include <vector>
//include custom Sprite class header
#include "../include/Sprite_class.hpp"
//include constants struct
#include "../include/Constants.hpp"

//class declaration
class Theater_scene
{
    public:
        //declaring public level attributes
        std::string name;
        std::string previous_name;
        MAP* my_map;
        int framerate;
        sf::View player_view;
        //declaring sprite list (vector)
        std::vector<Sprite*> My_sprite_list;
        //declaring constructor
        Theater_scene();
        //declaring classic functions
        void update(int framerate);
        void set_map(MAP* p_my_map);
        //load functions
        void load_new_scene(void);
        void load_background(void);
        void load_map(void);
        void load_player(void);
        //other update functions
        void update_current_scene(void);
        void update_camera(float center_x, float center_y);
        //special functions
        sf::Image get_default_texture(unsigned int size_x, unsigned int size_y);
};

#endif // _THEATER_SCENE_CLASS_
