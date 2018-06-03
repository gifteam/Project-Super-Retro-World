//check the collision
bool Sprite::collide_a_sprite(std::string direction)
{
	//create the collision rect of the current sprite
	sf::FloatRect rect(this->getPosition().x + offset_x, this->getPosition().y + offset_y, this->width,this->height);
	if (direction.compare("RIGHT") == 0) { rect.left = rect.left + 1; }
	else if (direction.compare("LEFT") == 0) { rect.left = rect.left - 1; }
	else if (direction.compare("DOWN") == 0) { rect.top = rect.top + 1; }
	else if (direction.compare("UP") == 0) { rect.top = rect.top - 1; }

    //loop with others sprites
    for (unsigned int i = 0 ; i < this->sprite_list.size() ; i++)
    {
		for (unsigned int j = 0 ; j < this->collide_with.size() ; j++)
		 {
			if ((this->collide_with[j].compare(this->sprite_list[i]->type) == 0) && i != this->current_sprite_id)
			{
				if (this->sprite_list[i]->getGlobalBounds().intersects(rect))
				{
					//collide
					return true;
				}
			}
        }
    }
    //dont collide
    return false;
}

//get player height whoever ask for it
float Sprite::get_player_height(void)
{
	for (unsigned int i = 0 ; i < this->sprite_list.size() ; i++)
	{
		if (this->sprite_list[i]->type.compare("PLAYER") == 0) { return this->sprite_list[i]->height; }
	}
	return 0;
}

//get player horizontal speed whoever ask for it
float Sprite::get_player_width(void)
{
	for (unsigned int i = 0 ; i < this->sprite_list.size() ; i++)
	{
		if (this->sprite_list[i]->type.compare("PLAYER") == 0) { return this->sprite_list[i]->width; }
	}
	return 0;
}

//get player horizontal speed whoever ask for it
float Sprite::get_player_horizontal_speed(void)
{
	for (unsigned int i = 0 ; i < this->sprite_list.size() ; i++)
	{
		if (this->sprite_list[i]->type.compare("PLAYER") == 0) { return this->sprite_list[i]->horizontal_speed; }
	}
	return 0;
}

//get player position whoever ask for it
sf::Vector2f Sprite::get_player_position(void)
{
	for (unsigned int i = 0 ; i < this->sprite_list.size() ; i++)
	{
		if (this->sprite_list[i]->type.compare("PLAYER") == 0) { return this->sprite_list[i]->get_position(); }
	}
	return sf::Vector2f(0,0);
}

//get itself position
sf::Vector2f Sprite::get_position(void)
{
	return sf::Vector2f(this->getPosition().x, this->getPosition().y);
}