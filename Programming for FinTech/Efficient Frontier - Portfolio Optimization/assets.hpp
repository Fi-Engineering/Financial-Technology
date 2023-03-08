#ifndef __ASSETS_HPP__
#define __ASSETS_HPP__

#include <string>
#include <vector>

#include <cstdio>
#include <cstdlib>


class Asset
{
  public:
    std::string name;

    double expectedRateRet;
    double stdDev;
	
  public:
    Asset(){}
    ~Asset(){}
};

#endif