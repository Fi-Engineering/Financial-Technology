#include "function.h"


#include <cstdlib>
#include <cstdio>



int binarySearchForZero(Function<int, int> * f, int low, int high) {
  while (low + 1 < high) {
    int mid = (low + high) / 2;
    int val = f->invoke(mid);
    if (val == 0) {
      return mid;
    }
    else if (val > 0) {
      high = mid;
    }
    else {
      low = mid;
    }
  }
  return low;
}
