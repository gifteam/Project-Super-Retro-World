SET PATH=%PATH%;C:\MinGW\bin;

mingw32-g++.exe -Wall -fexceptions -Icode\SFML\include -Idll -c code\main.cpp -o code\objet\main.o
mingw32-g++.exe -Wall -fexceptions -Icode\SFML\include -Idll -c code\source\Sprite_class.cpp -o code\objet\Sprite_class.o
mingw32-g++.exe -Wall -fexceptions -Icode\SFML\include -Idll -c code\source\Theater_class.cpp -o code\objet\Theater_class.o
mingw32-g++.exe -Wall -fexceptions -Icode\SFML\include -Idll -c code\source\Theater_play_class.cpp -o code\objet\Theater_play_class.o
mingw32-g++.exe -Wall -fexceptions -Icode\SFML\include -Idll -c code\source\Theater_scene_class.cpp -o code\objet\Theater_scene_class.o

mingw32-g++.exe -static-libgcc -static-libstdc++ -Lcode\SFML\lib -Lcode\dll -o SuperRetroWorld.exe code\objet\*.o -s -lsfml-network -lsfml-audio -lsfml-graphics -lsfml-window -lsfml-system

pause