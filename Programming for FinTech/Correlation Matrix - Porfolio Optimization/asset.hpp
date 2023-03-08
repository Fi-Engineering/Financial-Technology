#ifndef __ASSET_HPP__
#define __ASSET_HPP__


#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>

#include "Matrix.hpp"


class Asset 
{
	
  public:
  	double avgRateRet; 
    double stdDev; 
    std::string name;
    std::vector<double> timeRateRet; 
    std::vector<double> price;
    
    
    int numLines; //records of data
	
  public:
    Asset(){}
	
    ~Asset(){}
	
	typedef Matrix<double> Asset2D;
	
	friend Asset* readData(char* file);
	
    void getTimeRateRet();
	
    void getAvgStdDev();
	
	//covariance of two assets
    double getCovar(Asset asset1, Asset asset2);
	
    // correlation of two assets
    double getCorr(Asset asset1, Asset asset2);
	
	// correlation matrix of all assets:
    Asset2D getCorrMatrix(Asset* asset, int num);
};

#endif
