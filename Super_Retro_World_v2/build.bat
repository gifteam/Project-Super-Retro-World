SET PATH=%PATH%;C:\MinGW\bin;
g++ -lstdc++ main.cpp src\*.cpp -o project_compiled.exe -Iinclude/ -ISFML/bin/ -BSFML/include/ -ISFML/include/ -LSFML/include/ -LSFML/lib/ -lsfml-network -lsfml-audio -lsfml-graphics -lsfml-window -lsfml-system -lopengl32
rem -lstdc++
rem -Wall -Wextra -Werror


rem g++ main.o -o sfml-app -Lc:\SFML-2.0\lib -lsfml-window -lsfml-system
pause
