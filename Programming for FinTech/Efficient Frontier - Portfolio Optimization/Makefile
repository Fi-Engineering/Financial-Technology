CCFLAGS=--std=gnu++98 -pedantic -Wall -Werror -ggdb3
efficient_frontier: parse.o optimizer.o main.o
	g++ -o efficient_frontier $(CCFLAGS) parse.o optimizer.o main.o
parse.o: parse.cpp optimizer.cpp parse.hpp assets.hpp optimizer.hpp 
	g++ -c $(CCFLAGS) -o parse.o parse.cpp
main.o: main.cpp optimizer.cpp assets.hpp parse.hpp optimizer.hpp
	g++ -c $(CCFLAGS) -o main.o main.cpp

clean:
	rm -f *.o  *~ efficient_frontier