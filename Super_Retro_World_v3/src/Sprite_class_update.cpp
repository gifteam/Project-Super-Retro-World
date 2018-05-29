
void Sprite::update_hitbox_mode(void)
{
  //change image if hitbox mode is one
  if (hitbox_mode)
  {
    setTexture(*hitbox_texture);
    setTextureRect({0, 0, 32, 32 });
    if (this->type.compare("PLAYER")==0) { setTextureRect({0, 0, 32, 32 }); }
    else if (this->type.compare("BACKGROUND")==0) { setTextureRect({0, 0, 0, 0 }); }
    else if (this->type.compare("SOLID")==0 ||this->type.compare("SOLID_RED")==0) { setTextureRect({0, 0, 32, 32 }); }
    else if (this->type.compare("TRANSPARENT_RED")==0) { setTextureRect({0, 0, 0, 0 });}
  }
  else
  {
    setTexture(*texture);
    if (this->type.compare("PLAYER")==0) { setTextureRect(sprite_rect); }
    else if (this->type.compare("BACKGROUND")==0) { setTextureRect({ 0, 0, 640*5, 480 }); }
    else if (this->type.compare("SOLID")==0 ||this->type.compare("SOLID_RED")==0) { setTextureRect({0, 0, 32, 32 }); }
    else if (this->type.compare("TRANSPARENT_RED")==0) { setTextureRect({0, 0, 0, 0 });}
  }
  //end of procedure
}

void Sprite::update_frame(void)
{
	//simulate acceleration through frame update (usefull when running);
	sprite_framerate_factor =  1 + std::abs(float(horizontal_speed / max_horizontal_speed));

	//update global animation (select row)
	update_row_frame();
	
	//reset frame if changing row
	if (sprite_row_frame != sprite_previous_row_frame) { sprite_frame = 0; }
	sprite_previous_row_frame = sprite_row_frame;
	
	//get the animation image set id
	if (sprite_clock.getElapsedTime().asSeconds() >= float(sprite_framerate[sprite_row_frame] / sprite_framerate_factor)){
		if (sprite_frame >= sprite_max_frame[sprite_row_frame])
		{
			sprite_frame = 0;
		}else{
			sprite_frame += 1;
		}
		//update rect position and size
		sprite_rect.left = sprite_frame * 32;
		sprite_rect.top = sprite_row_frame * 32;
		setTextureRect(sprite_rect);
		sprite_clock.restart();
	}
	//end of the procedure
}

void Sprite::update_row_frame(void)
{
    if (this->type.compare("PLAYER") == 0)
    {
		if (vertical_speed == 0){
			if (horizontal_speed < 0) { sprite_row_frame = 2;} //running left
			else if (horizontal_speed > 0) { sprite_row_frame = 3;} //running right
			else { sprite_row_frame = 1;} //idle right
		}
		else if (vertical_speed < 0){
			if (horizontal_speed < 0) { sprite_row_frame = 8;} //jumping left
			else if (horizontal_speed >= 0) { sprite_row_frame = 9;} //jumping right
		}
		else if (vertical_speed > 0){
			if (horizontal_speed < 0) { sprite_row_frame = 6;} //falling left
			else if (horizontal_speed >= 0) { sprite_row_frame = 7;} //falling right
		}
	}
}

//update the physical part of the sprites
//update the gravity
void Sprite::update_gravity(void)
{
    if (!touch_floor && vertical_speed + vertical_acceleration/this->framerate <= max_vertical_speed) { vertical_speed += vertical_acceleration/this->framerate; }
}

//update player movement
void Sprite::update_movement(void)
{
    //get last good position collision-free
    previous_x = this->getPosition().x;
    previous_y = this->getPosition().y;
	 //try to move
    this->move(horizontal_speed/this->framerate, vertical_speed/this->framerate);
    //declare local x + y to determine best location if collide
    float delta_x = (-1) * (this->getPosition().x - previous_x)/10;
    float delta_y = (-1) * (this->getPosition().y - previous_y)/10;
    while (collide_a_sprite("")) //test if there is a collision with a solid sprite
    {
        //move back to the first correct position
        this->move(sf::Vector2f(delta_x, delta_y));
    }
	//check if touch a sprite
    touch_floor = false;
    touch_roof = false;
    touch_left = false;
    touch_right = false;
    if (collide_a_sprite("DOWN")) {vertical_speed = 0; touch_floor = true;}
    if (collide_a_sprite("UP")) {vertical_speed = 0; touch_roof = true;}
    if (collide_a_sprite("LEFT")) {horizontal_speed = 0; touch_left = true;}
    if (collide_a_sprite("RIGHT")) {horizontal_speed = 0; touch_right = true;}
}

void Sprite::update_filter_activation(void)
{
  //switch filters 
  if ((current_filter == 0) && (sf::Keyboard::isKeyPressed(sf::Keyboard::Numpad1) || sf::Keyboard::isKeyPressed(sf::Keyboard::Numpad2) || sf::Keyboard::isKeyPressed(sf::Keyboard::Numpad3)))
  {
      std::cout << "Activate filter" << std::endl;
      current_filter = 1;
  } 
}

void Sprite::update_filter_type(void)
{
  if (has_two_types && current_filter==1)
  {
    type=second_type;
  }
}

//update the player direction
void Sprite::update_player_direction(void)
{	
	if (sf::Keyboard::isKeyPressed(sf::Keyboard::Space) && touch_floor)
    {
        vertical_speed = -350;
    }
	// ask for reset position
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Escape))
    {
        setPosition(sf::Vector2f(0, 0));
    }
	//check keyboard <- and -> pressure
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Q) && !touch_left)
    {
        horizontal_speed -= horizontal_acceleration/this->framerate;
        if (horizontal_speed < (-1) * max_horizontal_speed) { horizontal_speed = (-1) * max_horizontal_speed; }
    }
    else if (sf::Keyboard::isKeyPressed(sf::Keyboard::D) && !touch_right)
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