#ifndef __T_MATRIX_H___
#define __T_MATRIX_H___

#include <vector>
#include <assert.h>
#include <cstdlib>
#include <iostream>


template<typename T>
class Matrix
{
 private:
  int numRows;
  int numColumns;
  std::vector<T> ** rows;

 public:

  Matrix() : numRows(0), numColumns(0), rows(NULL) {}
  Matrix(int n, int m) : numRows(n), numColumns(m), rows(new std::vector<T> *[n]) {
    int i;
    for (i = 0; i < n; i++) {
      rows[i] = new std::vector<T>(m);
    }
  }

  Matrix(const Matrix & rhs) :
      numRows(rhs.numRows),
      numColumns(rhs.numColumns),
      rows(new std::vector<T> *[numRows]) {
    int i;
    for (i = 0; i < numRows; i++) {
      rows[i] = new std::vector<T>(rhs[i]);
    }
  }

  ~Matrix() {
    int i;
    for (i = 0; i < numRows; i++) {
      delete rows[i];
    }
    delete[] rows;
  }


  Matrix & operator=(const Matrix & rhs) {
    if (this != &rhs) {
      
      std::vector<T> ** t = new std::vector<T> *[rhs.numRows];
      int i;
      for (i = 0; i < rhs.numRows; i++) {
        t[i] = new std::vector<T>(rhs[i]);
      }

      int j;
      for (j = 0; j < numRows; j++) {
        delete rows[j];
      }
      delete[] rows;
  
      numRows = rhs.numRows;
      numColumns = rhs.numColumns;
      rows = t;
    }
    return *this;
  }

 
  int getRows() const { return numRows; }

  int getColumns() const { return numColumns; }

 
  const std::vector<T> & operator[](int index) const {
    assert(index >= 0 && index < numRows);
    return *rows[index];
  }

  std::vector<T> & operator[](int index) {
    assert(index >= 0 && index < numRows);
    return *rows[index];
  }

 
  bool operator==(const Matrix & rhs) const {
    if (numRows != rhs.numRows || numColumns != rhs.numColumns) {
      return false;
    }
    int i;
    for (i = 0; i < numRows; i++) {
      if ((*this)[i] != rhs[i]) {
        return false;
      }
    }
    return true;
  }


  Matrix operator+(const Matrix & rhs) const {
    assert(numRows == rhs.numRows && numColumns == rhs.numColumns);
    Matrix ans(numRows, numColumns);
    ans.numRows = numRows;
    ans.numColumns = rhs.numColumns;
    int i,j;
    for (i = 0; i < numRows; i++) {
      for (j = 0; j < numColumns; j++) {
        ans[i][j] = (*this)[i][j] + rhs[i][j];
      }
    }
    return ans;
  }
};

template<typename T>
std::ostream & operator<<(std::ostream & s, const Matrix<T> & rhs) {
  if (rhs.getRows() == 0) {
    s << "[  ]";
    return s;
  }
  s << "[ ";
  int i;
  for (i = 0; i < rhs.getRows() - 1; i++) {
    s << rhs[i] << ",\n";
  }
  s << rhs[rhs.getRows() - 1] << " ]";
  return s;
}

template<typename T>
std::ostream & operator<<(std::ostream & s, const std::vector<T> & rhs) {
  if (rhs.size() == 0) {
    s << "{  }";
    return s;
  }
  s << "{ ";
  size_t i;
  for (i = 0; i < rhs.size() - 1; i++) {
    s << rhs[i] << ",";
  }
  s << rhs[rhs.size() - 1] << " }";
  return s;
}

#endif
