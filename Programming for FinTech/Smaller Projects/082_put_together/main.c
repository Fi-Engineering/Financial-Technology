#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "kv.h"
#include "counts.h"
#include "outname.h"

counts_t * countFile(const char * filename, kvarray_t * kvPairs) {
  FILE *f;
  char *line = NULL;
  
  counts_t *c;

  size_t lines = 0;
  int r;

  //WRITE ME
  f = fopen(filename, "r");
  if (f == NULL) {
    perror("cannot read");
    exit(EXIT_FAILURE);
  }
  c = createCounts();
  while ((r = getline(&line, &lines, f)) != -1) {
    if (r > 0 && line[r-1] == '\n')
      line[r-1] = '\0'; 
    addCount(c, lookupValue(kvPairs, line));
  }
  if (!feof(f)) {
    fprintf(stderr, "invalid input\n");
    exit(EXIT_FAILURE);
  }
  free(line);
  fclose(f);
  return c;
}

int main(int argc, char ** argv) {
  kvarray_t *kv;
  int i;
  //WRITE ME (plus add appropriate error checking!)
  if (argc <= 1) {
    fprintf(stderr, "need one argument\n");
    exit(EXIT_FAILURE);
  }
  //read the key/value pairs from the file named by argv[1] (call the result kv)
  kv = readKVs(argv[1]);

 //count from 2 to argc (call the number you count i)
  for (i = 2; i < argc; i++) {
    counts_t *c;
    char *outName;
    FILE *f;

    //count the values that appear in the file named by argv[i], using kv as the key/value pair
    
    c = countFile(argv[i], kv);
    //compute the output file name from argv[i] (call this outName)
    outName = computeOutputFileName(argv[i]);

    //open the file named by outName (call that f)
    f = fopen(outName, "w");
    if (f == NULL) {
      perror("can't open file");
      exit(EXIT_FAILURE);
    }

    //print the counts from c into the FILE f
    printCounts(c, f);

    //close f
    fclose(f);

    //free the memory for outName and c
    free(outName);
    freeCounts(c);
  }
 //free the memory for kv
  freeKVs(kv);

  return EXIT_SUCCESS;
}


