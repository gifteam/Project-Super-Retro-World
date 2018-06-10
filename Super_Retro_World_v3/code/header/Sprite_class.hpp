#ifndef _SPRITE_CLASS_
//define the sprite class (object)
#define _SPRITE_CLASS_
//include graphic library
#include <SFML/Graphics.hpp>
//include standard library
#include <vector>

//class declaration
class Sprite: public sf::Sprite
{
  public:
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    //CLASS PARAMETERS
    static int current_filter; // give the current filter ID (0 -no filter- to 1 -filter- for the MVP)
	bool ask_for_player_reset; // will reset player position on hit or on demad
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    //GENERAL PARAMETERS
    int framerate; // general framerate of the game to update accordingly
    std::vector<Sprite*> sprite_list; // list of all the sprite (usefull for collision purpose)
    unsigned int current_sprite_id; // unique ID of the sprite (from the sprite_list)
    float center_x; // center of the sprite (for camera positionnement purpose)
    float center_y; // center of the sprite (for camera positionnement purpose)
    float previous_x; // previous frame correct position (to correct position if there is a collision)
    float previous_y; // previous frame correct position (to correct position if there is a collision)
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    //"BACKGROUND" PARAMETERS
    unsigned int background_layer; // ID of the current background layer (for parallaxe animation)
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

	//-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    //"COIN" PARAMETERS
    bool collected; // TRUE if collected by the player, false overwise
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

	
	//-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    //TILESET SPRITES PARAMETERS
    int row_rect_tileset_sprite;
	int col_rect_tileset_sprite;
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
	
	//-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    //"MOVING SPRITE" PARAMETERS
    bool moving_sprite_horizontal_direction; // 0 for LEFT and 1 for RIGHT
	int moving_sprite_horizontal_speed; // horizontal speed of the sprite
	bool moving_sprite_vertical_direction; // 0 for UP and 1 for DOWN
	int moving_sprite_vertical_speed; // vertical speed of the sprite
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
	
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    //TYPE PARAMETERS
    std::string type; // current type of the sprite (like "family" of the sprite, "PLAYER", "BACKGROUND", ...)
    bool has_two_types; // determine if the sprite has 2 types (usefull to change the proprety of the sprite)
    std::string first_type; // parameter to save main type 
    std::string second_type; // parameter to save second type 
    bool second_type_activated; //flag to change from first to second type
	sf::Texture* second_texture; //second texture of the sprite itseft (=spritesheet)
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
  
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    //TEXTURES PARAMETERS
    sf::Texture* texture; //texture of the sprite itseft (=spritesheet)
    sf::Texture* hitbox_texture; //texture of the sprite hitbox
    bool hitbox_mode; // flag to switch texture
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    //ANIMATION PARAMETERS
    sf::IntRect sprite_rect; //rect to select a part of the texture (=spritesheet)
    sf::Clock sprite_clock; // clock to animate the sprite
    unsigned int sprite_row_frame; // row ID of the sprite sheet
    unsigned int sprite_previous_row_frame; // previous row ID to detect the changement of row (resrt animation cycle)
    unsigned int sprite_frame; // curent frame to show in the row
    std::vector<unsigned int> sprite_max_frame; // frame amount by row in the spritesheet
    std::vector<float> sprite_framerate; // framerate by row in the spritesheet (animation speed)
    float sprite_framerate_factor; // framerate factor (for example, will be proportionnal of horizontal speed to simulate run acceleration)
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
   
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    //PHYSICAL PARAMETERS
    int offset_x; // offset of the hitbox from the sprite itseft (top-left corner)
    int offset_y; // offset of the hitbox from the sprite itseft (top-left corner)
    unsigned int width; //width ofthe hitbox
    unsigned int height; // height of the hitbox
    std::vector<std::string> collide_with; // list of family the current sprite collide with
	std::vector<std::string> top_bounce_with; // list of family the current sprite bounce with if touch from top
	std::vector<std::string> gameover_with; // list of family the current sprite with gameover with (by hit)
    bool touch_roof; // flag if touch a row (up)
    bool touch_floor;// flag if touch a floor (below)
    bool touch_left; // flag if touch a wall (left)
    bool touch_right;// flag if touch a wall (right)
    float vertical_acceleration; //Y acceleration
    float vertical_speed; //Y speed
    float max_vertical_speed; //Y max speed
    float horizontal_acceleration; //X acceleration
    float horizontal_speed; //X speed
    float max_horizontal_speed; //Y max speed
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    //CONSTRUCTOR
    Sprite(std::string s_type = "UNKNOWN"); // generic constructor with "UNKNOW" family type
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    //INITIALISATION
    void initialize_visual_sprite_attributes(void); // initialisation of the animation parameters depending on the family
    void call_file(void);
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    //UPDATE
    void update(int framerate, std::vector<Sprite*> sprite_list, int sprite_id, bool hitbox_mode); //global update (call others)
    void update_player_direction(void); //player update : check keyboard input 
	void update_moving_sprite_direction(void); //moving sprite update : direction
    void update_movement(void); //update the movement of the current sprite (with colission) comes after gravity frame update
    void update_moving_sprite_direction_and_movement(void); // update moving sprite movement and collision
	void update_gravity(void); //gravity update (vertical acceleration)
    void update_frame(void); // animation update (frame id and framerate)
    void update_row_frame(void); //update row frame
    void update_hitbox_mode(void); // change texture if hitbox mode is on/off
    void update_filter_activation(void); //update if the filter must be on / off
    void update_filter_type(void); // update the type of the sprite depending on the filter
	void update_filter_color(void); // update filtre sprite color (main one)
	void update_collect(void); // check if the current sprite collect a COIN sprite
	void update_top_bounce(void); // update vertical speed if touch a bouncing sprite from top side
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    //SETTER
    void set_hitbox(int off_x, int off_y, unsigned int w, unsigned int h); // set hitbox size and offset position
    void set_size(unsigned int w, unsigned int h); //set hitbox size
    void set_center_xy(void); // calculate the center of the sprite at the current frame
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    //GETTER
    sf::Vector2f get_player_position(void); // get player position (find the sprite in the sprite list and call get_position() (top left) )
    sf::Vector2f get_position(void); // get current sprite posiion (top left)
    float get_player_horizontal_speed(void); //get player Horitontal speed
    float get_player_height(void); // get player hitbox height
    float get_player_width(void); // get player hitbox width
    bool collide_a_sprite(std::string direction); // return true if there is a collision with a sprite (first one in the sprite list)
	bool bounce_a_sprite(std::string direction); // return true if on top of a bouncing sprite
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

};
#endif // _SPRITE_CLASS_
