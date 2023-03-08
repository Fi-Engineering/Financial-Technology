
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "asset.hpp"
#include "parse.hpp"
#include "Matrix.hpp"


//string with delimiter = comma:
void parser(std::string& line, std::vector<std::string>& priceVector, std::string& comma)
{
  
  std::string::size_type head, tail;
  head = 0;
  tail = line.find(comma);
  
  while(std::string::npos != tail)
  {
    priceVector.push_back(line.substr(head, tail-head));
 
    head = tail + comma.size();

    tail = line.find(comma, head);
  }

  if(head != line.length())
    priceVector.push_back(line.substr(head));

}

//input price data from file as second argument in cmd line:
Asset* readData(char* file, int &numAsts)
{
  std::ifstream ifs(file);
  
  // series of input file error checks:
  

  std::string line;
  std::getline(ifs, line);
  
  // test for file with nothing in it:
  if(line.size() == 0)
  {
    perror("Empty file");
   	exit(EXIT_FAILURE);
  }

  // no file to open:
  if(!ifs.is_open())
  {
    perror("Could not open file");
    exit(EXIT_FAILURE);
  }
  
  
  std::vector<std::string> priceVector;
  std::string comma = ","; //comma is delimiter
  parser(line, priceVector, comma);
  
  numAsts = priceVector.size()-1; //assets which corresponds to columns in input file
  
  Asset* prices = new Asset[numAsts];
  
  int i;
  for(i=0; i<numAsts; i++)
  {
	prices[i].name = priceVector[i+1];	
  }
  
  int numLines = 0;  //the number of records or lines in the file
  
  std::vector<std::string> candidatePrices;
  while(std::getline(ifs,line))
  {
    parser(line,candidatePrices,comma);
    int priceCount = candidatePrices.size() + 0;
	//number of prices not the same as assets
    if(priceCount != (numAsts + 1))
	{
      perror("columns do not match expected count");
   	  exit(EXIT_FAILURE);
    }
	//first line has non-numeric data:
    if(numLines==0)
	{
      for(i=0; i<numAsts; i++)
	  {
        if(candidatePrices[i+1] == "null" || atof(candidatePrices[i+1].c_str())==0.0)
		{
          perror("invalid data first line ");
   	      exit(EXIT_FAILURE);
        }
      }
    }
    for(i=0;i<numAsts;i++)
	{
	  // using previous price value if current price value is missing:
      if(candidatePrices[i+1] == "null" || atof(candidatePrices[i+1].c_str())==0.0)
	  {   
		double temp = prices[i].price.back();
		prices[i].price.push_back(temp);
      }
      else
		  // for valid prices, add price to price vector:
	  {
       
		prices[i].price.push_back(atof(candidatePrices[i+1].c_str()));
      }
    }
    numLines++;
	
	
    candidatePrices.clear();
  }
  
  //checks for insufficient data: 
  if(numLines <= 2)
  {
    perror("insufficient data to perform asset covariance and correlation");
 	  exit(EXIT_FAILURE);
  }
  
  for(i=0;i<numAsts;i++)
  {
      prices[i].name = priceVector[i+1];
  }
  
  for(i=0; i<numAsts; i++)
  {
	prices[i].numLines = numLines;
  }
  
    return prices;
}
