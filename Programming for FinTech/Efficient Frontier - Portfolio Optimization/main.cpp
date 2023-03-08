#include <cstdio>
#include <cstdlib>

#include <algorithm>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <unistd.h>
#include <vector>

#include <Eigen/Dense>

#include "assets.hpp"
#include "parse.hpp"
#include "optimizer.hpp"

using namespace Eigen;

double Unrestrict(Portfolio &P, double &ror); 

double Restrict(Portfolio &P,double &ror);


int main(int argc, char ** argv){
  

  if (argc !=4 && argc != 3)  
  {
     fprintf(stderr, "Input Error\n");

     return EXIT_FAILURE;
  }
  
  if(strlen(argv[1]) != 2 && argc == 4 )
  {
      std::cerr<<"position sizing error";

      return EXIT_FAILURE;
  }
  

  int rcode;

  bool r = false;

  while ((rcode = getopt(argc, argv, "r")) != -1)
  {
	
	if(rcode == 'r')
  {
		r = true;
  }

	else
	{
		std::cerr<<"wrong option";

        return EXIT_FAILURE;
	}
  }
  
//input assets from file:
  int numAsts = 0;

  std::vector<Asset> Avec;
  MatrixXd CorrMat;

  if(r == true)
  {
    Avec = parseAssets(argv[2], numAsts);
    CorrMat = parseCorMat(argv[3], numAsts);
  }
  else
  {
    Avec = parseAssets(argv[1],numAsts);
    CorrMat = parseCorMat(argv[2],numAsts); 
  }
  

  Portfolio Port;

  Port.numAsts = numAsts;
  Port.assets = Avec;
  Port.corrMat = CorrMat;
  
  // rate of return parameters:
  double rorStart = 0.01;
  double rorEnd   = 0.265;
  double rorInc   = 0.01;
  
  
  std::cout<<"ROR,volatility"<<std::endl;
 // std::cout<<"ROR, volatility";
  std::cout.setf(std::ios::fixed);
    
//unrestricted
  if(r == false)
  {
    for(double ror = rorStart; ror <= rorEnd; ror = ror + rorInc)
	{
       std::cout<<std::fixed<<std::setprecision(1)<< ror*100<<"%,";

       std::cout<<std::fixed<<std::setprecision(2)<< Unrestrict(Port, ror)*100<<"%"<<std::endl;
    }
  }
  
//restricted
  if(r == true)
  {
    for(double ror = rorStart; ror <= rorEnd; ror = ror + rorInc)
	{
		
       std::cout<<std::fixed<<std::setprecision(1)<<ror*100<<"%,";

       std::cout<<std::fixed<<std::setprecision(2)<<Restrict(Port, ror)*100<<"%"<<std::endl;
    }
  }
  std::cout.unsetf(std::ios::fixed);

  return EXIT_SUCCESS;
}