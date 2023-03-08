CCFLAGS=--std=gnu++98 -pedantic -Wall -Werror -ggdb3
corr_matrix: asset.o parse.o main.o
	g++ -o corr_matrix $(CCFLAGS) asset.o parse.o main.o
main.o: main.cpp asset.hpp Matrix.hpp
	g++ -c $(CCFLAGS) -o main.o main.cpp
parse.o: parse.cpp parse.hpp asset.hpp
	g++ -c $(CCFLAGS) -o parse.o parse.cpp	
asset.o: asset.cpp asset.hpp
	g++ -c $(CCFLAGS) -o asset.o asset.cpp

clean:
	rm -f *.o  *~ corr_matrix