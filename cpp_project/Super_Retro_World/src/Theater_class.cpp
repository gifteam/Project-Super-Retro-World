//include standard libraries
#include <iostream>
//include graphic library
#include <SFML/Graphics.hpp>
#include <SFML/OpenGL.hpp>
//include custom Theater class header
#include "Theater_class.h"
//include custom Theater play class header
#include "Theater_play_class.h"
//include constants struct
#include "Constants.h"

//constructor
Theater::Theater(void) : sf::RenderWindow::RenderWindow(sf::VideoMode(640, 480), "My window")
{
    //initializing every window attributes
    scene = "";
    name = "window";
    fps = 0;
    x = 0;
    y = 0;
    width = 640;
    height = 480;

    //set the size of the window
    //window_size.x = width;
    //window_size.y = height;
    //setSize(window_size);

    //set fps and global graphics attributes
        //setVerticalSyncEnabled(true);
    setFramerateLimit(60);
    fps_show_timeout = 30;
    glEnable(GL_TEXTURE_2D); //pas compris ce que ça faisait

    //set font
    if (!font.loadFromFile("file/font/font_001.ttf"))
    {
        std::cout << "error loading font" << std::endl;
    }
    text.setFont(font);
    text.setString("FPS : N/A");
    text.setCharacterSize(14);
    //text.setColor(sf::Color::Red);
    //text.setStyle(sf::Text::Bold | sf::Text::Underlined);
    //text.setPosition(0,0);
    //shape.setRadius(50.0f);
    //shape.setFillColor(sf::Color(100, 250, 50));
}

//update
void Theater::update(void)
{
    while (this->isOpen())
    {
        update_FPS();

        while (this->pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                this->close();
        }

        this->My_theater_play.update();

        this->clear();
        this->draw_Theater();
        this->draw(this->text);
        this->display();
    }
}

//call the draw from theater_play class object
void Theater::draw_Theater(void)
{
    for (const auto& sprite : this->My_theater_play.My_theater_scene.My_sprite_list)
        this->draw(*sprite);
}

//updating the FPS sprite (text only)
void Theater::update_FPS(void)
{
    //fps measure and draw
    sf::Time frameTime = clock.restart();
    this->fps_show_timeout++;
    if (this->fps_show_timeout >= 30)
    {
        this->fps_show_timeout = 0;
        int framerate = 1 / (frameTime.asMilliseconds() * 0.001);
        if (framerate <= 0)
        {
            this->text.setString("FPS : N/A");
        }
        else
        {
            this->text.setString("FPS : " + std::to_string(framerate));
        }
    }

}

//create the MAP struct that define level parameters
MAP Theater::create_MAP(void){

    std::string style = "LEVEL_0_0";
    MAP my_map;

    my_map.STYLE_NAME[style] = "LEVEL_0_0";
    my_map.BACK_STYLE[style] = "forest_017";
    my_map.FRONT_STYLE[style] = "001";
    my_map.TILE_STYLE[style] = "003";
    my_map.ELEMENT_STYLE[style] = "001";
    my_map.PLAYER_STYLE[style] = "005";
    my_map.ENEMYSET_STYLE[style] = "002";
    my_map.LOADING_STYLE[style] = "002";
    my_map.WAKE_UP_STYLE[style] = "004";

    return my_map;
}
