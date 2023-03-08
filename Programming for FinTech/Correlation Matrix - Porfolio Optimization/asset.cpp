
#include <cmath>
#include <iostream>

#include "Matrix.hpp"
#include "asset.hpp"
#include "parse.hpp"

typedef Matrix<double> Asset2D;

// asset rate of return over time:
void Asset::getTimeRateRet()
{
  for(int i=0; i<numLines-1; i++)
  {
      timeRateRet.push_back((price[i+1] - price[i])/price[i]);
	//timeRateRet[i].push_back((price[i+1] - price[i])/price[i]);
  }
}
// average standard deviation of asset:
void Asset::getAvgStdDev()
{
  double sum=0;
  for(int i=0; i<numLines-1; i++)
  {
    sum = sum + timeRateRet[i];
  }
  avgRateRet = sum/(numLines-1);
  
  sum = 0; 
  for(int i=0; i<numLines-1; i++)
  {
    sum = sum + (timeRateRet[i] - avgRateRet)*(timeRateRet[i] - avgRateRet);
  }
  
  stdDev = std::sqrt(sum/(numLines-2));
}

// covariance of two assets:
double getCovar(Asset asset1, Asset asset2)
{
  double sum = 0;
  for(int i=0;i<asset1.numLines-1;i++)
  {
    sum = sum + (asset1.timeRateRet[i] - asset1.avgRateRet)*(asset2.timeRateRet[i] - asset2.avgRateRet);
  }
  double covar = sum/(asset1.numLines-1);
  return covar;
}

// correlation of two assets:
double getCorr(Asset asset1, Asset asset2)
{
  double covar = getCovar(asset1, asset2);
  double corr = covar/(asset1.stdDev*asset2.stdDev);
  return corr;
}

// correlation matrix:
Asset2D getCorrMatrix(Asset* A, int num)
{
  Asset2D corMat(num,num);
  for(int i=0;i<num;i++)
  {
    for(int j=0;j<num;j++)
	{
      if(i == j){
        corMat[i][j] = 1.0;
      }
      else{
        corMat[i][j] = getCorr(A[i], A[j]);
      }
    }
  }
  return corMat;
}

