//include standard libraries
#include <iostream>
//include graphic library
#include <SFML/Graphics.hpp>
//include custom Theater class header
#include "../code/header/Theater_class.hpp"
#include "../code/header/Constants.hpp"

//main procedure
int main(int argc, char* argv[])
{
    //creating theater instance (window)
    Theater My_theater;
    // updating the whole thing
    My_theater.update();
    //returning correct exit value (0)
    return 0;
    //end of procedure
}
