//include standard libraries
#include <iostream>
//include graphic library
#include <SFML/Graphics.hpp>
//include custom Sprite class header
#include "../include/Sprite_class.hpp"

//constructor
Sprite::Sprite(std::string new_type) : sf::Sprite::Sprite()
{
    std::cout << "Sprite constructor" << std::endl;
    //define the sprite type
    type = new_type;
    collidable = false;
    origin_color = getColor();
    if (this->type.compare("SOLID")==0 || this->type.compare("PLAYER")==0)
    {
        collidable = true;
    }
    vertical_acceleration = 400.0f;
    vertical_speed = 0.0f;
    max_vertical_speed = 400.0f;
    horizontal_acceleration = 700.0f;
    horizontal_speed = 0.0f;
    max_horizontal_speed = 150.0f;
}

void Sprite::update(int new_framerate, std::vector<Sprite*> new_sprite_list, int new_sprite_id)
{
    this->framerate = new_framerate;
    this->sprite_list = new_sprite_list;
    this->current_sprite_id = new_sprite_id;
    //update player sprite
    if (this->type.compare("PLAYER") == 0)
    {
        update_player_direction(); //horizontal speed update
        update_gravity(); //vertical speed update
        update_player_movement(); //move the player
    }
}

//update the physical part of the sprites
//update the gravity
void Sprite::update_gravity(void)
{
    if (vertical_speed + vertical_acceleration/this->framerate <= max_vertical_speed) { vertical_speed += vertical_acceleration/this->framerate; }
}

//update the collision with others sprites
void Sprite::check_collision(void)
{
    //initialize collision side flag
    collide_floor = false;
    collide_left_wall = false;
    collide_right_wall = false;
    collide_roof = false;
    //loop with others sprites
    for (unsigned int i = 0 ; i < this->sprite_list.size() ; i++)
    {
        //avoid himself
        if (i != this->current_sprite_id && this->collidable && this->sprite_list[i]->collidable)
        {
            //check collision
            if (this->sprite_list[i]->getGlobalBounds().intersects(this->getGlobalBounds()))
            {
                //collide yes, but which side ? Get the correct collision flag
                this->get_collision_flag(i);
            }
        }
    }
}

//update player movement
void Sprite::update_player_movement(void)
{
    //get last good position
    previous_x = this->getPosition().x;
    previous_y = this->getPosition().y;
    //try to move
    this->move(horizontal_speed/this->framerate, vertical_speed/this->framerate);
    //check collision
    check_collision();
    //if collide with floor / roof
    if (collide_floor || collide_roof)
    {
        vertical_speed /= 2;
        this->setPosition(sf::Vector2f(this->getPosition().x, previous_y));
    }
    //if collision with a wall
    if (collide_left_wall || collide_right_wall)
    {
        horizontal_speed /= 2;
        this->setPosition(sf::Vector2f(previous_x, this->getPosition().y));
    }
}

//update the player direction
void Sprite::update_player_direction(void)
{
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up))
    {
        vertical_speed = -250;
    }
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
    {
        horizontal_speed -= horizontal_acceleration/this->framerate;
        if (horizontal_speed < (-1) * max_horizontal_speed) { horizontal_speed = (-1) * max_horizontal_speed; }
    }
    else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
    {
        horizontal_speed += horizontal_acceleration/this->framerate;
        if (horizontal_speed > max_horizontal_speed) { horizontal_speed = max_horizontal_speed; }
    }
    else
    {
        if (horizontal_speed < 0){ horizontal_speed += horizontal_acceleration/this->framerate; }
        else if (horizontal_speed > 0){ horizontal_speed -= horizontal_acceleration/this->framerate; }

        if (horizontal_speed > (-1) * horizontal_acceleration/this->framerate && horizontal_speed < horizontal_acceleration/this->framerate){ horizontal_speed = 0; }
    }
}

//set new size
void Sprite::set_size(unsigned int w, unsigned int h)
{
    width = w;
    height = h;
}

//calculation of the collision flag (up, down, left or right)
void Sprite::get_collision_flag(int sprite_collided_id)
{
    //get previous area where the sprite was
    int previous_area = get_previous_area_before_hit(sprite_collided_id);
    std::cout << previous_area;
    //check if the sprite hit the floor
    if (previous_area == 1 || previous_area == 2 ||previous_area == 3){collide_floor = true;}
    //check if the sprite hit the floor
    if (previous_area == 4){collide_left_wall = true;}
    //check if the sprite hit the right wall
    if (previous_area == 5 || previous_area == 6 ||previous_area == 7){collide_roof = true;}
    //check if the sprite hit the left wall
    if (previous_area == 8){collide_right_wall = true;}
}

/* get the area (int) where the sprite moving was before the hit with the sprite "#" (moving or not)
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 8 | # | 4 |
+---+---+---+
| 7 | 6 | 5 |
+---+---+---+*/
int Sprite::get_previous_area_before_hit(int sprite_collided_id)
{
    float x = previous_x;
    float y = previous_y;
    float w = this->width;
    float h = this->height;
    float s_hit_x = this->sprite_list[sprite_collided_id]->getPosition().x;
    float s_hit_y = this->sprite_list[sprite_collided_id]->getPosition().y;
    float s_hit_w = this->sprite_list[sprite_collided_id]->width;
    float s_hit_h = this->sprite_list[sprite_collided_id]->height;

    if (x + w < s_hit_x && y + h <= s_hit_y) {return 1;}
    if (x + w >= s_hit_x && x <= s_hit_x + s_hit_w && y + h <= s_hit_y) {return 2;}
    if (x > s_hit_x + s_hit_w && y + h <= s_hit_y) {return 3;}
    if (x > s_hit_x + s_hit_w && y + h > s_hit_y && y < s_hit_y + s_hit_h) {return 4;}
    if (x > s_hit_x + s_hit_w && y >= s_hit_y + s_hit_h) {return 5;}
    if (x + w >= s_hit_x && x <= s_hit_x + s_hit_w && y >= s_hit_y + s_hit_h) {return 6;}
    if (x + w < s_hit_x && y >= s_hit_y + s_hit_h)  {return 7;}
    if (x + w < s_hit_x && y + h > s_hit_y && y < s_hit_y + s_hit_h) {return 8;}
}

//calculation of center of the Sprite
void Sprite::get_center_xy(void)
{
    float x = this->getPosition().x;
    float y = this->getPosition().x;
    float w = this->width;
    float h = this->height;

    center_x = x + w/2;
    center_y = y + h/2;

}

