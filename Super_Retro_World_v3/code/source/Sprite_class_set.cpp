//set new size
void Sprite::set_size(unsigned int w, unsigned int h)
{
    width = w;
    height = h;
}

//set new size
void Sprite::set_hitbox(int off_x, int off_y, unsigned int w, unsigned int h)
{
  offset_x = off_x;
	offset_y = off_y;
	set_size(w, h);
}

//calculation of center of the Sprite
void Sprite::set_center_xy(void)
{
    float x = this->getPosition().x;
    float y = this->getPosition().x;
    float w = this->width;
    float h = this->height;

    center_x = x + w/2;
    center_y = y + h/2;
}