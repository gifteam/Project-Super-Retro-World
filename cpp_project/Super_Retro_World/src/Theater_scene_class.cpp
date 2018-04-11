//include standard libraries
#include <iostream>
//include custom Theater scene class header
#include "Theater_scene_class.h"
//include Sprite.h to create the sprite list
#include "Sprite_class.h"

//constructor
Theater_scene::Theater_scene(void)
{
    std::cout << "theater scene constructor" << std::endl;
    name = "level";
    previous_name = "";
}

//update (check if the scene has change)
void Theater_scene::update(void)
{
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

    //load_background();
    load_map();
    //load_sprites();
}

//load background
void Theater_scene::load_background(void)
{
    //create a new sprite with it's texture
    My_sprite_list.push_back(new Sprite);
    My_sprite_list.back()->texture = new sf::Texture;

    //if can't load the texture
    if (!My_sprite_list.back()->texture->loadFromFile("file/image/image_001.png"))
    {
        //error handler (no texture ? pink color ?)
        std::cout << "can't load the image on the texture" << std::endl;
        sf::Image image;
        image.create(20, 20, sf::Color::Magenta);
        My_sprite_list.back()->texture->loadFromImage(image);
    }
    //set the texture to the sprite
    My_sprite_list.back()->setTexture(*(My_sprite_list.back()->texture));
}

//load map
void Theater_scene::load_map(void)
{
    //instanceiate map object texture into image to read pixels
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
            //BLACK pixel => it's a sprite !
            if (r==0 && b==0 && b==0)
            {
                spr_x = map_x * 32;
                spr_y = map_y * 32;
                My_sprite_list.push_back(new Sprite);
                My_sprite_list.back()->texture = new sf::Texture;
                My_sprite_list.back()->setPosition(sf::Vector2f(spr_x, spr_y));
                //if can't load the sprite texture
                if (!My_sprite_list.back()->texture->loadFromFile("file/image/sprite.png"))
                {
                    My_sprite_list.back()->texture->loadFromImage(get_default_texture(32, 32));
                }
                //set the texture to the sprite
                My_sprite_list.back()->setTexture(*(My_sprite_list.back()->texture));
            }
        }
    }
}

//load sprites
void Theater_scene::load_sprites(void)
{
    //create a new sprite with it's texture
    My_sprite_list.push_back(new Sprite);
    My_sprite_list.back()->texture = new sf::Texture;

    //if can't load the texture
    if (!My_sprite_list.back()->texture->loadFromFile("file/image/image_001.png"))
    {
        My_sprite_list.back()->texture->loadFromImage(get_default_texture(32, 32));
    }
    //set the texture to the sprite
    My_sprite_list.back()->setTexture(*(My_sprite_list.back()->texture));
}

//update the current scene (every sprites)
void Theater_scene::update_current_scene(void)
{
    for (unsigned int i = 0 ; i < this->My_sprite_list.size() ; i++)
    {
       this->My_sprite_list[i]->update();
    }
}

//return a default texture if can't be properly loaded
sf::Image Theater_scene::get_default_texture(unsigned int size_x, unsigned int size_y)
{
    sf::Image image;
    image.create(size_x, size_y, sf::Color::Magenta);
    return image;
}
