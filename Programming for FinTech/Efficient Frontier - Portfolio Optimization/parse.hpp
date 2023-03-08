#ifndef __PARSE_HPP__
#define __PARSE_HPP__


#include <cstdio>
#include <cstdlib>

#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include <Eigen/Dense>

#include "assets.hpp"
#include "optimizer.hpp"


using namespace Eigen;

void parseString(std::string& line, std::vector<std::string>& priceVector, std::string& comma);

std::vector<Asset> parseAssets(char* filename, int &num);

MatrixXd parseCorMat(char* filename, int num);


#endif