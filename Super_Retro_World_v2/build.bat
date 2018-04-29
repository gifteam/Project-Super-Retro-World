SET PATH=%PATH%;C:\MinGW\bin;

mingw32-g++.exe -Wall -fexceptions -DSFML_STATIC -O2 -DSFML_STATIC -ISFML\include -Idll -ISFML\include -Idll -c main.cpp -o obj\main.o
mingw32-g++.exe -Wall -fexceptions -DSFML_STATIC -O2 -DSFML_STATIC -ISFML\include -Idll -ISFML\include -Idll -c src\*.cpp -o obj\*.o

mingw32-g++.exe -LSFML\lib -Ldll -LSFML\lib -Ldll -o Super_Retro_World_executable.exe obj\*.o -s -lsfml-network -lsfml-audio -lsfml-graphics -lsfml-window -lsfml-system -lopengl32

pause
