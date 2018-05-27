//include standard libraries
#include <iostream>
//include graphic library
#include <SFML/Graphics.hpp>
#include <SFML/OpenGL.hpp>
//include custom Theater class header
#include "../include/Theater_class.hpp"
//include custom Theater play class header
#include "../include/Theater_play_class.hpp"
//include constants struct
#include "../include/Constants.hpp"

//constructor
Theater::Theater(void) : sf::RenderWindow::RenderWindow(sf::VideoMode(640, 480), "My window")
{
    //initializing every window attributes
    this->scene = "";
    this->name = "window";
    this->fps = 0;
    this->x = 0;
    this->y = 0;
    this->width = 640;
    this->height = 480;
    this->framerate = 0;

    //set fps and global graphics attributes
	this->text_bc.loadFromImage(get_default_texture(300, 130));
    setFramerateLimit(60);
    fps_show_timeout = 30;

    //set font
    if (!font.loadFromFile("file/font/font_001.ttf"))
    {
        std::cout << "error loading font" << std::endl;
    }
    this->text.setFont(font);
    this->text.setString(" FPS : N/A");
    this->text.setCharacterSize(14);
    guide_text = "\n\n [LEFT] and [RIGHT] to move\n [UP] to jump\n [Num_1] to [Num_3] to swap colors.\n [CTRL] to switch sprite/hitbox modes\n [ESC] to reset position";
	
    //set levels characteristics
    create_MAP();
    MAP* p_my_map = &my_map;
    this->My_theater_play.set_map(p_my_map);
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
        //general update
        this->My_theater_play.update(this->framerate);
        //draw everything (sprite, labels and camera view)
        this->clear();
        this->setView(My_theater_play.My_theater_scene.player_view);
        this->draw_Theater();
        this->text.setPosition(sf::Vector2f(this->getView().getCenter().x - 640/2, 0));
		sf::Sprite sprite(this->text_bc);
		sprite.setPosition(sf::Vector2f(this->getView().getCenter().x - 640/2, 0));
		sprite.setColor(sf::Color(0,0,0,125));
		this->draw(sprite);
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
        this->framerate = 1 / (frameTime.asMilliseconds() * 0.001);
        if (this->framerate <= 0)
        {
            this->text.setString(" FPS : N/A" + guide_text);
        }
        else
        {
            this->text.setString(" FPS : " + std::to_string(this->framerate) + guide_text);
        }
    }

}

//create the MAP struct that define level parameters
void Theater::create_MAP(void){

    std::string style = "LEVEL_0_0";

    my_map.STYLE_NAME[style] = "LEVEL_0_0";
    my_map.BACK_STYLE[style].push_back("forest_017");
    my_map.BACK_STYLE[style].push_back("forest_016");
    my_map.BACK_STYLE[style].push_back("forest_015");
    my_map.BACK_STYLE[style].push_back("forest_014");
    my_map.FRONT_STYLE[style] = "001";
    my_map.TILE_STYLE[style] = "003";
    my_map.ELEMENT_STYLE[style] = "001";
    my_map.PLAYER_STYLE[style] = "005";
	my_map.CAPPY_STYLE[style] = "006";
    my_map.ENEMYSET_STYLE[style] = "002";
    my_map.LOADING_STYLE[style] = "002";
    my_map.WAKE_UP_STYLE[style] = "004";
}

//return a default texture if can't be properly loaded
sf::Image Theater::get_default_texture(unsigned int size_x, unsigned int size_y)
{
    sf::Image image;
    image.create(size_x, size_y, sf::Color::Magenta);
    return image;
}