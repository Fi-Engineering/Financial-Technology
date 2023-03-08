#ifndef __T_MATRIX_HPP__
#define __T_MATRIX_HPP__

#include <assert.h>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <vector>


template<typename T>
class Matrix {
 
 private:
    int numRows;
    int numCols;
    
    
    std::vector<std::vector<T> > rows;

 public:
    // constructors:
    Matrix():numRows(0), numCols(0) {}
    Matrix(int n, int m);
    Matrix(const Matrix<T> & rhs):numRows(rhs.numRows),numCols(rhs.numCols),rows(rhs.rows) {}
  
  //member functions:
  
  int getRows() const;
  int getCols() const;
  
  
    Matrix<T> &  copyMatrix(const Matrix<T> & rhs);
  
  // overloaded operators following approach used with 086_vector-2d
  const std::vector<T> & operator[](int index) const;  
  std::vector<T> & operator[](int index);
  
  // other member functions:
  
  // determines two matrices are equal, must be of same dimensions:
  bool areEqual(const Matrix<T> & rhs) const;
  
 // add the values of two matrices, must be of same dimensions:
  Matrix<T> addMats(const Matrix<T> & rhs) const;
  
};

// displays the asset names and correlation matrix:
template<typename T>
std::ostream & displayMat(std::ostream & mat, const Matrix<T> & rhs);


// transpose matrix:
template <typename T>
Matrix<T>::Matrix(int n, int m) : numRows(n), numCols(m), rows(n) 
{
  int i;
  for(i=0;i<numRows;i++)
  {
    std::vector<T> temp(numCols);
    rows[i] = temp;
  }
}



// returns deep copy of matrix:
template <typename T>
//Matrix<T> & Matrix<T>::copyMatrix(const Matrix<T> & rhs)
//Matrix<T> Matrix<T>& ::copyMatrix(const Matrix<T> & rhs)
//Matrix<T> & Matrix<T>::copyMatrix(const Matrix<T> & rhs)
//Matrix<T> &  copyMatrix(const Matrix<T> & rhs)
Matrix<T> &  Matrix<T>::copyMatrix(const Matrix<T> & rhs)
{
  if(this != &rhs)
  {
 	  numRows = rhs.numRows;
      numCols = rhs.numCols;
      rows = rhs.rows;
  }
  return *this;
}


//  Returns the number of rows.
template <typename T>
int Matrix<T>::getRows() const 
{
  return numRows;
}

//  Returns the number of columns.
template <typename T>
int Matrix<T>::getCols() const 
{
  return numCols;
}

//  overloaded index operator, validates index,  returns reference to the  row:
template <typename T>
const std::vector<T> & Matrix<T>::operator[](int index) const 
{
  assert(index>=0);
  assert(index<numRows);
  return rows[index];
}


template <typename T>

std::vector<T> & Matrix<T>::operator[](int index) {
  assert(index>=0);
  assert(index<numRows);
  return rows[index];
}

//  determines if two matrices have the same number of rows and columns,
// and each element value equals value of corresponding element in the other:

template <typename T>
bool Matrix<T>::areEqual(const Matrix<T> & rhs) const 
{
  if(numRows!=rhs.numRows || numCols!=rhs.numCols)
  {
    return false;
  }
  if(rows != rhs.rows)
  { 
      return false;
  }
  return true;
}



// tests for dimensional equivalence, then adds each element of one to the other
	
template <typename T>  
Matrix<T> Matrix<T>::addMats(const Matrix<T> & rhs) const 
{
  assert(numRows == rhs.numRows);
  assert(numCols == rhs.numCols);
  Matrix<T> newMat(numRows, numCols);
  int i;
  int j;
  for(i=0;i<numRows;i++)
  {
    for(j=0;j<numCols;j++)
	{
      newMat.rows[i][j] = rows[i][j] + rhs.rows[i][j];
    }
  }
  return newMat;
}


//displays the correlation matrix:
template <typename T>
std::ostream & displayMat(std::ostream & mat, const Matrix<T> & rhs) 
{
  if(rhs.getRows()==0)
  {
    mat<<"[  ]";
    return mat;
  }
  int i=0;
  int j=0;
  std::cout.setf(std::ios::fixed);
  mat<<std::setprecision(4)<<"[ "<<(rhs[i])[j];
  for(j=1;j<rhs.getCols();j++)
  {
    if((rhs[i])[j]>=0)
	{
      mat<<std::setprecision(4)<<", "<<(rhs[i])[j];  
    }
    else
	{
      mat<<std::setprecision(4)<<","<<(rhs[i])[j];  
    }
  }
  mat<<std::endl;
  for(i=1;i<rhs.getRows();i++)
  {
    if((rhs[i])[0]>=0)
	{
      mat<<" ";
    }
    mat<<" ";
    int j=0;
    mat<<std::setprecision(4)<<(rhs[i])[j];
    for(j=1;j<rhs.getCols();j++)
	{
      if((rhs[i])[j]>=0)
	  {
        mat<<std::setprecision(4)<<", "<<(rhs[i])[j];  
      }
      else
	  {
        mat<<std::setprecision(4)<<","<<(rhs[i])[j];  
      }
    }
    if(i==rhs.getRows()-1)
	{
      mat<<"]"<<std::endl;  
    }
    else
	{
      mat<<std::endl; 
    }
  }
  std::cout.unsetf(std::ios::fixed);
  return mat;
}

#endif
