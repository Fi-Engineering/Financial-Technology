#ifndef __OPTIMIZER_HPP__
#define __OPTIMIZER_HPP__

#include <cstdio>
#include <cstdlib>

#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>

#include <Eigen/Dense>

#include "assets.hpp"

using namespace Eigen;


class Portfolio
{
  public:
    std::vector<Asset> assets;    
    MatrixXd corrMat;    

	double expectedRateRet;         
    int numAsts;                  
	double stdDev;      

    VectorXd weights;             
   
	
  public:
  
    Portfolio(){}
	
    void getStdDev()
	{   
      int i,j;
      double sum = 0;

      for(i=0; i<numAsts; i++)
	  {
        for(j=0; j<numAsts; j++)
		{
          sum = sum + weights(i)*weights(j)*corrMat(i,j)*assets[i].stdDev*assets[j].stdDev;
        }
      }
      stdDev = std::sqrt(sum);
    } 
	
	void getExpRateRet()
	{
      int i;
      int sum = 0;

      for(i=0; i<numAsts; i++)
	  {
        sum = sum + weights(i)*assets[i].expectedRateRet;
      }
      expectedRateRet = sum;
    }
	
	
    ~Portfolio(){}
};

#endif
