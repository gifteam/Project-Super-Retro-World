//initialisation of all visual sprite attributes 
void Sprite::initialize_visual_sprite_attributes(void)
{
	//player init
	if (this->type.compare("PLAYER")==0)
	{
		//rect for spritesheet
		sprite_rect.left = 0;
		sprite_rect.top = 0;
		sprite_rect.width = 32;
		sprite_rect.height = 32;
		//row frame
		sprite_row_frame = 1;
		sprite_previous_row_frame = sprite_row_frame;
		//current frame id
		sprite_frame = 0;
		//sprite row
		sprite_max_frame.push_back(0); //idle left
		sprite_max_frame.push_back(0); //idle right
		sprite_max_frame.push_back(11); //run left
		sprite_max_frame.push_back(11); //run right
		sprite_max_frame.push_back(1); //edge left
		sprite_max_frame.push_back(1); //edge right
		sprite_max_frame.push_back(0); //fall left
		sprite_max_frame.push_back(0); //fall right
		sprite_max_frame.push_back(0); //jump left
		sprite_max_frame.push_back(0); //jump right
		//sprite row speed
		sprite_framerate_factor = 1;
		sprite_framerate.push_back(0.1); //idle left
		sprite_framerate.push_back(0.1); //idle right
		sprite_framerate.push_back(0.1f); //run left
		sprite_framerate.push_back(0.1f); //run right
		sprite_framerate.push_back(0.25f); //edge left
		sprite_framerate.push_back(0.25f); //edge right
		sprite_framerate.push_back(0.25f); //fall left
		sprite_framerate.push_back(0.25f); //fall right
		sprite_framerate.push_back(0.25f); //jump left
		sprite_framerate.push_back(0.25f); //jump right
	}
}