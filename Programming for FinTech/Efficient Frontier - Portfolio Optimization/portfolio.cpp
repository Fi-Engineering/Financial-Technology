
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

#include <Eigen/Dense>

#include "assets.hpp"
#include "parse.hpp"
#include "portfolio.hpp"

using namespace Eigen;

    double Restrict(Portfolio &Port,double &ror)
	{
	  int numAsts = Port.numAsts;
	  MatrixXd assets1 = MatrixXd::Ones(1, numAsts);
	  MatrixXd assets2(1,numAsts);
	  for(int i=0;i<numAsts;i++)
	  {
		assets2(i) = Port.assets[i].expectedRateRet;
	  }
	  MatrixXd assets(2, numAsts);
	  assets << assets1, assets2;
	  
	  MatrixXd zerosMatrix = MatrixXd::Zero(numAsts,1);
	  MatrixXd rorVector(2,1);
	  rorVector <<1, ror;
	  MatrixXd rorMatrix(numAsts+2,1);
	  rorMatrix << zerosMatrix, rorVector;
	  MatrixXd CovMat(numAsts, numAsts); 

	  for(int i=0; i<numAsts; i++)
	  {
		for(int j=0; j<numAsts; j++)
		{
		  CovMat(i,j) = Port.assets[i].stdDev * Port.corrMat(i,j) * Port.assets[j].stdDev;
		}
	  }
	  MatrixXd nullMat = MatrixXd::Zero(2,2); //Initialize 2x2 matrix of zeros
	  MatrixXd CovTranspose(numAsts+2,numAsts+2); 
	  CovTranspose<<CovMat,assets.transpose(),assets,nullMat; //Initialize CovTranspose
	  VectorXd weightsVector(numAsts+2, 1); 

	  // https://eigen.tuxfamily.org/dox/classEigen_1_1FullPivHouseholderQR.html


	  weightsVector = CovTranspose.fullPivHouseholderQr().solve(rorMatrix);  // solve using Eigen library
	  
		  
	  // set up for constrains computations:
  	  MatrixXd dupAssets = assets;
	  MatrixXd duprorMatrix = rorMatrix;
	  VectorXd dupweightsVector = weightsVector;
	  
	  for(int i=1; i<numAsts; i++)
	  { 
	   
		MatrixXd Constraints;  
		 
		bool chk = true;
		int dimAdder=0;
		for(int j=0; j<numAsts; j++) 
		{		
			if(dupweightsVector(j) < 0.00001)  	
			{
				  MatrixXd Temp = MatrixXd::Zero(numAsts,1); 
				  Temp(j,0) = 1;
				  MatrixXd temp = Constraints;
				  Constraints.resize(numAsts, dimAdder+1);
				  if(dimAdder==0)
				  {
					 Constraints << Temp;  
				  }
				  else
				  {
					  Constraints << temp, Temp; 
				  }
				  chk = false;
				  dimAdder++;
				 
			}
		}
		if(chk == true)
	    {		
		    break;
		}
		 
		 
		MatrixXd tempAssets = dupAssets;
		dupAssets.resize(tempAssets.rows() + Constraints.cols(), numAsts);
		dupAssets << tempAssets, Constraints.transpose();
		  
		MatrixXd tempRor = duprorMatrix;
		duprorMatrix.resize(tempRor.rows() + Constraints.cols(),1);
		duprorMatrix << tempRor, MatrixXd::Zero(Constraints.cols(),1);
		MatrixXd nullMatrix = MatrixXd::Zero(dupAssets.rows(),dupAssets.rows());
		MatrixXd dupCovTranspose((CovMat.rows() + dupAssets.rows()), (CovMat.rows() + dupAssets.rows()));
		dupCovTranspose << CovMat, dupAssets.transpose(), dupAssets, nullMatrix;
		 
		dupweightsVector = dupCovTranspose.fullPivHouseholderQr().solve(duprorMatrix);//use Eigen library solution routine

	  } 
	  
	  Port.weights = dupweightsVector.head(numAsts);
	  Port.getStdDev();
	  return Port.stdDev;
    }
	
	
	double Unrestrict(Portfolio &Port, double &ror)
	{
		  int numAsts = Port.numAsts;
		  MatrixXd assets1 = MatrixXd::Ones(1, numAsts);
		  
		  MatrixXd assets2(1, numAsts);
		  
		  for(int i=0; i<numAsts; i++)
		  {
			 assets2(i) = Port.assets[i].expectedRateRet;
		  }
		  
		  MatrixXd assets(2, numAsts);
		  
		  assets<<assets1, assets2;
		
		  
		  MatrixXd zerosMatrix = MatrixXd::Zero(numAsts,1);
		   
		  MatrixXd rorVector(2,1);
		  rorVector<<1,ror;
		
		  
		  MatrixXd rorMatrix(numAsts+2,1);
		  rorMatrix <<zerosMatrix,rorVector;
		
		  MatrixXd CovMat(numAsts, numAsts);
		  for(int i=0;i<numAsts;i++)
		  {
			for(int j=0;j<numAsts;j++)
			{
			  CovMat(i,j) = Port.assets[i].stdDev * Port.corrMat(i,j) * Port.assets[j].stdDev;
			}
		  }
	
		  MatrixXd nullMat = MatrixXd::Zero(2,2);
		

		  MatrixXd CovTranspose(numAsts+2,numAsts+2); 
		  CovTranspose<<CovMat,assets.transpose(),assets,nullMat; 
		

		  VectorXd weightsVector(numAsts+2, 1); 

		  // https://eigen.tuxfamily.org/dox/classEigen_1_1FullPivHouseholderQR.html

		  weightsVector = CovTranspose.fullPivHouseholderQr().solve(rorMatrix); 
		
		  Port.weights = weightsVector.head(numAsts);
		
		  Port.getStdDev();
		  return Port.stdDev;
	}










