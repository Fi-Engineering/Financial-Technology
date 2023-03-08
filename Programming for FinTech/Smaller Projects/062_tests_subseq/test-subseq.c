
/*
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>


size_t maxSeq(int * array, size_t n);

void doTest(int * array, int n) {
  printf("maxSeq(");
  if (array == NULL || n==0) {
    printf("NULL");
  }
  else {
    printf("{");
    for (int i =0; i < n; i++) {
      printf("%d", array[i]);
      if (i < n -1) {
  printf(", ");
      }
    }
    printf("}");
  }
  printf(", %d) is \n", n);
  //int maxLen = maxSeq(array, n);
  size_t maxLen = maxSeq(array, n);
  //if (maxLen == NULL) {
   if (maxLen == -1 || n==0) {
    printf("NULL\n");
  }
  else {
    printf("%d\n", maxLen);
  }
}


int main(void) {
  int array1[] = { 5, 6, 3, 5, 7, 8, 9, 1, 2};
  int array2[] = { 12, 13, 1, 5, 4, 7, 8, 10, 10, 11};
  int array3[] = { 425, 59, -3, 77, 0, 36};
  int array4[] = { 0, 36};
  int array5[] = { 36, 0};

  doTest (array1, 9);
  doTest (array2, 10);
  doTest (array3, 6);
  doTest (array4, 2);
  doTest (array5, 2);
  doTest (NULL, 0);
  doTest (array1, 0);
  
  return EXIT_SUCCESS;
}

*/
#include <stdio.h>
#include <stdlib.h>

size_t maxSeq(int * array, size_t n);

void run_check(int count, int * array, size_t n, size_t ans) {

  size_t temp = maxSeq(array, n);

  if (temp != ans) {

    fprintf(stderr,"%d: Should be %zu but was %zu\n", count, ans, temp);

    exit(EXIT_FAILURE);

  }

}

int main(void) {


  int array1[] = {1,2,3,4,5,6,7,8,9,10,11,12,13};
  int array2[] = {-1,0,1,2,3};
  int array3[] = {425,424,423,422};
  int array4[] = {0,0,0,0,0};
  int array5[] = {1,2,1,3,4,5,6,7,8,9};
  int array6[] = {};

  run_check(1,NULL, 0, 0);
  run_check(2,array1, 10, 10);
  run_check(3,array2, 5, 5);
  run_check(4,array3, 2, 1);
  run_check(5,array4, 5,1);
  run_check(6,array5, 10,8);
  run_check(7,array6, 0,0);
  

  return EXIT_SUCCESS;

}