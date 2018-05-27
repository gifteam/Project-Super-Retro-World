SET PATH=%PATH%;C:\MinGW\bin;

mingw32-g++.exe -Wall -fexceptions -ISFML\include -Idll -c main.cpp -o obj\main.o
mingw32-g++.exe -Wall -fexceptions -ISFML\include -Idll -c src\Sprite_class.cpp -o obj\src\Sprite_class.o
mingw32-g++.exe -Wall -fexceptions -ISFML\include -Idll -c src\Theater_class.cpp -o obj\src\Theater_class.o
mingw32-g++.exe -Wall -fexceptions -ISFML\include -Idll -c src\Theater_play_class.cpp -o obj\src\Theater_play_class.o
mingw32-g++.exe -Wall -fexceptions -ISFML\include -Idll -c src\Theater_scene_class.cpp -o obj\src\Theater_scene_class.o

mingw32-g++.exe -static-libgcc -static-libstdc++ -LSFML\lib -Ldll -o Super_Retro_World_executable.exe obj\main.o obj\src\*.o -s -lsfml-network -lsfml-audio -lsfml-graphics -lsfml-window -lsfml-system

rem call Super_Retro_World_executable.exe

pause