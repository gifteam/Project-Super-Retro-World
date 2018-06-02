//include standard libraries
#include <iostream>
//include custom Theater scene class header
#include "../header/Theater_scene_class.hpp"
//include Sprite.h to create the sprite list
#include "../header/Sprite_class.hpp"
//include constants struct
#include "../header/Constants.hpp"

//constructor
Theater_scene::Theater_scene(void)
{
    std::cout << "theater scene constructor" << std::endl;
    name = "LEVEL_0_0";
    previous_name = "";
    player_view.setCenter(sf::Vector2f(640/2, 480/2));
    player_view.setSize(sf::Vector2f(640, 480));
	//hitbox to sprite mode
	hitbox_mode = false;
  previous_hitbox_mode = false;
}

//update (check if the scene has change)
void Theater_scene::update(int framerate)
{
    this->framerate = framerate;
    if (name.compare(previous_name) != 0)
    {
        std::cout << "loading new scene" << std::endl;
        load_new_scene();
    }
    else
    {
        update_current_scene();
    }
    previous_name = name;
}

//change the scene (unload everything + load new scene)
void Theater_scene::load_new_scene(void)
{
    My_sprite_list.clear();

    load_background();
    load_map();
    load_player();
	load_filter();
}

//load the filter color
void Theater_scene::load_filter(void)
{
    //create a new sprite with it's texture 
    My_sprite_list.push_back(new Sprite("FILTER"));
    My_sprite_list.back()->texture = new sf::Texture;
    My_sprite_list.back()->hitbox_texture = new sf::Texture;
	My_sprite_list.back()->texture->loadFromImage(get_default_texture(18, 26, sf::Color(255, 255, 255, 255)));
	My_sprite_list.back()->hitbox_texture->loadFromImage(get_default_texture(32, 32, sf::Color(255, 255, 255, 0)));
    //set the texture to the sprite
    My_sprite_list.back()->setTexture(*(My_sprite_list.back()->texture));
    My_sprite_list.back()->setPosition(sf::Vector2f(0, 0));
    My_sprite_list.back()->set_hitbox(0,0,0,0);
	My_sprite_list.back()->setTextureRect({ 0, 0, 640, 480 });
	//end of procedure
}

//load the player sprite
void Theater_scene::load_player(void)
{
    //create a new sprite with it's texture PLAYER
    std::string player_filename = my_map->PLAYER_STYLE[name];
    My_sprite_list.push_back(new Sprite("PLAYER"));
    My_sprite_list.back()->texture = new sf::Texture;
    My_sprite_list.back()->hitbox_texture = new sf::Texture;

    //if can't load the texture
    if (!My_sprite_list.back()->texture->loadFromFile("file/image/" + player_filename + ".png"))
    {
        My_sprite_list.back()->texture->loadFromImage(get_default_texture(18, 26, sf::Color::Red));
    }
    //if can't load the texture
    if (!My_sprite_list.back()->hitbox_texture->loadFromFile("file/image/" + player_filename + "_h.png"))
    {
        My_sprite_list.back()->hitbox_texture->loadFromImage(get_default_texture(32, 32, sf::Color::Red));
    }    
    //set the texture to the sprite
    My_sprite_list.back()->setTexture(*(My_sprite_list.back()->texture));
    My_sprite_list.back()->setPosition(sf::Vector2f(0, 0));
    My_sprite_list.back()->set_hitbox(7, 6, 18, 26);
    My_sprite_list.back()->setTextureRect(My_sprite_list.back()->sprite_rect);
	
}

//load background
void Theater_scene::load_background(void)
{
    //loop through every background piece
    unsigned int back_size = 0;
    std::string back_filename = "";

    for (back_size = 0; back_size < my_map->BACK_STYLE[name].size(); back_size++)
    {
        //create a new sprite with it's texture
        My_sprite_list.push_back(new Sprite("BACKGROUND"));
        My_sprite_list.back()->texture = new sf::Texture;
        My_sprite_list.back()->hitbox_texture = new sf::Texture;
		
        back_filename = my_map->BACK_STYLE[name][back_size];

        //if can't load the texture
        if (!My_sprite_list.back()->texture->loadFromFile("file/image/" + back_filename + ".png"))
        {
            My_sprite_list.back()->texture->loadFromImage(get_default_texture(640, 480, sf::Color::Red));
        }
        //set the texture to the sprite
        My_sprite_list.back()->hitbox_texture->loadFromImage(get_default_texture(640, 480, sf::Color::Black));
        My_sprite_list.back()->texture->setRepeated(true);
        My_sprite_list.back()->setTexture(*(My_sprite_list.back()->texture));
        My_sprite_list.back()->setTextureRect({ 0, 0, 640*5, 480 });

        My_sprite_list.back()->background_layer = back_size + 1;
    }
}

//load map
void Theater_scene::load_map(void)
{
    //instanciate map object texture into image to read pixels
    sf::Texture map_texture;
    sf::Vector2u map_size;
    sf::Image map_image;
    sf::Color pixel_color;
    //get map src pixel file (png file) and transform the texture into a image
    map_texture.loadFromFile("file/image/map.png");
    map_image = map_texture.copyToImage();
    //get map size
    map_size = map_texture.getSize();
    unsigned int map_x, map_y;
    //prepare pixel color component
    unsigned int r, g, b;
    //prepare sprite position
    unsigned int spr_x, spr_y;
    //loop through every map src pixel file
    for (map_x = 0 ; map_x < map_size.x ; map_x++)
    {
        for (map_y = 0 ; map_y < map_size.y ; map_y++)
        {
            //get next pixel color
            pixel_color = map_image.getPixel(map_x, map_y);
            r = pixel_color.r;
            g = pixel_color.g;
            b = pixel_color.b;
            //BLACK pixel => it's a solid sprite !
            if (r==0 && g==0 && b==0)
            {
              spr_x = map_x * 32;
              spr_y = map_y * 32;
              My_sprite_list.push_back(new Sprite("SOLID"));
              My_sprite_list.back()->texture = new sf::Texture;
              My_sprite_list.back()->hitbox_texture = new sf::Texture;
              My_sprite_list.back()->setPosition(sf::Vector2f(spr_x, spr_y));
              My_sprite_list.back()->set_size(32, 32);
              //if can't load the sprite texture
              if (!My_sprite_list.back()->texture->loadFromFile("file/image/sprite.png")){My_sprite_list.back()->texture->loadFromImage(get_default_texture(32, 32, sf::Color::Red));}
              if (!My_sprite_list.back()->hitbox_texture->loadFromFile("file/image/sprite_h.png")){My_sprite_list.back()->hitbox_texture->loadFromImage(get_default_texture(32, 32, sf::Color::Red));}    
              //set the texture to the sprite
              My_sprite_list.back()->setTexture(*(My_sprite_list.back()->texture));
              My_sprite_list.back()->setTextureRect({ 0, 0, 32, 32 });
            }
            //RED pixel => it's a filtered sprite !
            if (r==255 && g==0 && b==0)
            {
              spr_x = map_x * 32;
              spr_y = map_y * 32;
              My_sprite_list.push_back(new Sprite("TRANSPARENT_RED"));
              My_sprite_list.back()->texture = new sf::Texture;
              My_sprite_list.back()->hitbox_texture = new sf::Texture;
              My_sprite_list.back()->setPosition(sf::Vector2f(spr_x, spr_y));
              My_sprite_list.back()->set_size(32, 32);
              //if can't load the sprite texture
              if (!My_sprite_list.back()->texture->loadFromFile("file/image/sprite_Red.png")){My_sprite_list.back()->texture->loadFromImage(get_default_texture(32, 32, sf::Color::Red));}
              if (!My_sprite_list.back()->hitbox_texture->loadFromFile("file/image/sprite_h.png")){My_sprite_list.back()->hitbox_texture->loadFromImage(get_default_texture(32, 32, sf::Color::Red));}  
              //set the texture to the sprite
              My_sprite_list.back()->setTexture(*(My_sprite_list.back()->texture));
              My_sprite_list.back()->setTextureRect({ 0, 0, 32, 32 });
            }
            //GREEN pixel => it's a filtered sprite !
            if (r==0 && g==255 && b==0)
            {
              spr_x = map_x * 32;
              spr_y = map_y * 32;
              My_sprite_list.push_back(new Sprite("TRANSPARENT_GREEN"));
              My_sprite_list.back()->texture = new sf::Texture;
              My_sprite_list.back()->hitbox_texture = new sf::Texture;
              My_sprite_list.back()->setPosition(sf::Vector2f(spr_x, spr_y));
              My_sprite_list.back()->set_size(32, 32);
              //if can't load the sprite texture
              if (!My_sprite_list.back()->texture->loadFromFile("file/image/sprite_Green.png")){My_sprite_list.back()->texture->loadFromImage(get_default_texture(32, 32, sf::Color::Green));}
              if (!My_sprite_list.back()->hitbox_texture->loadFromFile("file/image/sprite_h.png")){My_sprite_list.back()->hitbox_texture->loadFromImage(get_default_texture(32, 32, sf::Color::Green));}  
              //set the texture to the sprite
              My_sprite_list.back()->setTexture(*(My_sprite_list.back()->texture));
              My_sprite_list.back()->setTextureRect({ 0, 0, 32, 32 });
            }
            //BLUE pixel => it's a filtered sprite !
            if (r==0 && g==0 && b==255)
            {
              spr_x = map_x * 32;
              spr_y = map_y * 32;
              My_sprite_list.push_back(new Sprite("TRANSPARENT_BLUE"));
              My_sprite_list.back()->texture = new sf::Texture;
              My_sprite_list.back()->hitbox_texture = new sf::Texture;
              My_sprite_list.back()->setPosition(sf::Vector2f(spr_x, spr_y));
              My_sprite_list.back()->set_size(32, 32);
              //if can't load the sprite texture
              if (!My_sprite_list.back()->texture->loadFromFile("file/image/sprite_Blue.png")){My_sprite_list.back()->texture->loadFromImage(get_default_texture(32, 32, sf::Color::Blue));}
              if (!My_sprite_list.back()->hitbox_texture->loadFromFile("file/image/sprite_h.png")){My_sprite_list.back()->hitbox_texture->loadFromImage(get_default_texture(32, 32, sf::Color::Blue));}  
              //set the texture to the sprite
              My_sprite_list.back()->setTexture(*(My_sprite_list.back()->texture));
              My_sprite_list.back()->setTextureRect({ 0, 0, 32, 32 });
            }
            //GRAY pixel => it's a moving sprite !
            if (r==128 && g==128 && b==128)
            {
              spr_x = map_x * 32;
              spr_y = map_y * 32;
              My_sprite_list.push_back(new Sprite("SOLID_MOVING_HORIZONTAL"));
              My_sprite_list.back()->texture = new sf::Texture;
              My_sprite_list.back()->hitbox_texture = new sf::Texture;
              My_sprite_list.back()->setPosition(sf::Vector2f(spr_x, spr_y));
              My_sprite_list.back()->set_size(32, 32);
              //if can't load the sprite texture
              if (!My_sprite_list.back()->texture->loadFromFile("file/image/sprite.png")){My_sprite_list.back()->texture->loadFromImage(get_default_texture(32, 32, sf::Color::White));}
              if (!My_sprite_list.back()->hitbox_texture->loadFromFile("file/image/sprite_h.png")){My_sprite_list.back()->hitbox_texture->loadFromImage(get_default_texture(32, 32, sf::Color::White));}  
              //set the texture to the sprite
              My_sprite_list.back()->setTexture(*(My_sprite_list.back()->texture));
              My_sprite_list.back()->setTextureRect({ 0, 0, 32, 32 });
            }
        }
    }
}

//update the current scene (every sprites)
void Theater_scene::update_current_scene(void)
{
	//update hitbox_mode trigge value (CTRL key)
	if (sf::Keyboard::isKeyPressed(sf::Keyboard::LControl) || sf::Keyboard::isKeyPressed(sf::Keyboard::RControl))
  {
    if (hitbox_mode == previous_hitbox_mode) {hitbox_mode = not hitbox_mode; };
  }
  else
  {
    previous_hitbox_mode = hitbox_mode;
  }

    //initialize camera center
    float camera_center_x = 0;
    float camera_center_y = 0;
    //update every sprite position, state and animation cycle
    for (unsigned int i = 0 ; i < this->My_sprite_list.size() ; i++)
    {
       this->My_sprite_list[i]->update(this->framerate, this->My_sprite_list, i, hitbox_mode);
       //get new camera center
       if (this->My_sprite_list[i]->type.compare("PLAYER")==0)
       {
           this->My_sprite_list[i]->set_center_xy();
           camera_center_x = this->My_sprite_list[i]->center_x;
           camera_center_y = 480/2;
       }
    }
    //correction of the background and filter x position
    for (unsigned int i = 0 ; i < this->My_sprite_list.size() ; i++)
    {
       if (this->My_sprite_list[i]->type.compare("BACKGROUND")==0)
       {
           this->My_sprite_list[i]->setPosition(sf::Vector2f(camera_center_x - 640/2 - (camera_center_x*this->My_sprite_list[i]->background_layer)/10, 0));
       }
	   if (this->My_sprite_list[i]->type.compare("FILTER")==0)
       {
           this->My_sprite_list[i]->setPosition(sf::Vector2f(camera_center_x - 640/2, 0));
       }
    }
    //update the camera position (center)
    update_camera(camera_center_x, camera_center_y);
}

//update the camera position (center)
void Theater_scene::update_camera(float center_x, float center_y)
{
    player_view.setCenter(sf::Vector2f(center_x, center_y));
}

//return a default texture if can't be properly loaded
sf::Image Theater_scene::get_default_texture(unsigned int size_x, unsigned int size_y, sf::Color color)
{
    sf::Image image;
    image.create(size_x, size_y, color);
    return image;
}

//follow the map settings pointer to the scene
void Theater_scene::set_map(MAP* p_my_map)
{
    my_map = p_my_map;

}
