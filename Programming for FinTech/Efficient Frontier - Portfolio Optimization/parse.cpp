
#include <cstdio>
#include <cstdlib>

#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include <Eigen/Dense>

#include "assets.hpp"
#include "parse.hpp"
#include "optimizer.hpp"


using namespace Eigen;



void parseString(std::string& line, std::vector<std::string>& priceVector, std::string& comma)
{
  std::string::size_type head, tail;
  
  head = 0.0;
  tail = line.find(comma);
  
  while(std::string::npos != tail)
  {
    priceVector.push_back(line.substr(head, tail-head));
 
    head = tail + comma.size();

    tail = line.find(comma, head);
  }

  if(head != line.length())
  {
    priceVector.push_back(line.substr(head));
  }

}

MatrixXd parseCorMat(char* file,int numAsts)
{

  int temp=0, i, j;

  std::ifstream ifs(file);

  if(!ifs.is_open())
  {
    perror("correlation file did not open");

    exit(EXIT_FAILURE);
  }

  MatrixXd Corr(numAsts, numAsts);

  std::string comma = ","; 

  std::string line;

  
  while(std::getline(ifs,line))
  {
    
    if(temp == numAsts)
  {
      perror("mismatch between universe and corr matrix ");

      exit(EXIT_FAILURE);
    }

    std::vector<std::string> values;

    parseString(line, values, comma);
  
    if(values.size() != (size_t)numAsts)
  {
        perror("mismatch between universe and corr matrix");

        exit(EXIT_FAILURE);
    }

    for(j=0; j<numAsts; j++)
  {
      if(atof(values[j].c_str()) == 0.0)
    {
          perror("found invalid values in corr matrix");

          exit(EXIT_FAILURE);
      }
      Corr(temp,j) = atof(values[j].c_str());
    }
    temp++;

  }  // end while;
  
  if(temp == 0)
  {
      perror("empty file");
      exit(EXIT_FAILURE);
  }
  
  double tolerance = .0001;
  

  for(i=0; i<numAsts; i++)
  {
    for(j=0; j<=i; j++)
  {
      if(fabs(Corr(i,j) - Corr(j,i)) > tolerance || fabs(Corr(i,j)) > (1 + tolerance))
    {
          perror("Corr matrix format error");
          exit(EXIT_FAILURE);
      }
    }
    if(fabs(Corr(i,i) - 1) > tolerance)
  {
        perror("diagonal in corr matrix does not equal 1");
        exit(EXIT_FAILURE);
    }
  }
  return Corr;
}


std::vector<Asset> parseAssets(char* file, int &numAsts)
{
  std::vector<Asset> assets;
  std::ifstream ifs(file);

  
  std::string comma = ",";  
  std::string line;
  
  while(std::getline(ifs, line))
  {
    std::vector<std::string> values;
    parseString(line, values, comma);

    if(values.size() != 3)
	{
      perror("wrong format");
   	  exit(EXIT_FAILURE);
    }
    Asset dummy;
    dummy.name = values[0];
    if(atof(values[2].c_str())==0.0 || atof(values[1].c_str())==0.0)
	{
       perror("assets have wrong value"); 
   	   exit(EXIT_FAILURE);
    }
    dummy.expectedRateRet = atof(values[1].c_str());
    dummy.stdDev = atof(values[2].c_str());
    numAsts++;
    assets.push_back(dummy);
    
  } // end while;
  
  if(numAsts == 0)
  {
     perror("file is empty");

     exit(EXIT_FAILURE);
  }
  
  if(!ifs.is_open())
  {
    perror("could not open");
    
    exit(EXIT_FAILURE);
  }

  return assets;
}


