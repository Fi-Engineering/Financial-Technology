#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#include <cstdio>

#include "asset.hpp"
#include "parse.hpp"
#include "Matrix.hpp"


int main(int argc, char ** argv) 
{
  if (argc != 2) 
  {
    fprintf(stderr, "Command line argument error\n");
    return EXIT_FAILURE;
  }
  //input file data:
  
  Asset * assets;
  int numAsts;  //the number of assets
  assets = readData(argv[1], numAsts);
  
  //Rate of return for each row: 
  //int i;
  for (int i = 0; i < numAsts; i++) 
  {
    assets[i].getTimeRateRet();
  }
  
  //average return and standard deviation of each asset:
  for (int i = 0; i < numAsts; i++) 
  {
      assets[i].getAvgStdDev();
  }
  
  typedef Matrix<double> Asset2D;
  

  Asset2D getCorrMatrix(Asset* assets, int numAsts); 
  
  //correlation matrix:
  Asset2D solutionSet;
  solutionSet = getCorrMatrix(assets, numAsts);
  
  //Display asset names one per line: 
  for (int i = 0; i < numAsts; i++) 
  {
    std::cout << assets[i].name << std::endl;
  }
  
  // Display the correlation matrix:

  std::ostream& os = std::cout;
  displayMat( os, solutionSet);

  
  return EXIT_SUCCESS;
}
