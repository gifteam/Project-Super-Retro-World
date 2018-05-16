#ifndef _THEATER_CLASS_
//define the theater class (window)
#define _THEATER_CLASS_
//include standard library
#include <string>
//include graphic library
#include <SFML/Graphics.hpp>
#include <SFML/System.hpp>
//include custom Theater play class header
#include "../include/Theater_play_class.hpp"
//include constants struct
#include "../include/Constants.hpp"

//class declaration
class Theater: public sf::RenderWindow
{
    public:
        //declaring theater play (game)
        Theater_play My_theater_play;
        //declaring public window attributes
        MAP my_map;
        std::string name;
        std::string scene;
        unsigned int fps;
        unsigned int x;
        unsigned int y;
        unsigned int width;
        unsigned int height;
        sf::Vector2u window_size;
        sf::Clock clock;
        sf::Font font;
        sf::Text text;
        sf::CircleShape shape;
        sf::Event event;
        int fps_show_timeout;
        int framerate;
        //declaring constructor + functions
        Theater();
        void update();
        void update_FPS();
        void draw_Theater();
        void create_MAP(void);
};
#endif // _THEATER_CLASS_