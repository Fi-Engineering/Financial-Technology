#ifndef __PARSE_HPP__
#define __PARSE_HPP__

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "Matrix.hpp"
#include "asset.hpp"



//string with delimiter = comma:
void parser(std::string& line, std::vector<std::string>& priceVector, std::string& comma);

//Read and parse input file:
Asset* readData(char* file, int &num);


#endif