#Build du projet
all: 
	g++ -c -ISFML/include -std=c++11 main.cpp
	g++ -c -ISFML/include -std=c++11 src/*.cpp
	g++ *.o -o sfml-app -lsfml-network -lsfml-audio -lsfml-graphics -lsfml-window -lsfml-system
	./sfml-app

#Suppression des objets
clean:
	rm -rf *.o
