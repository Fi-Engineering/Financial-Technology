#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "outname.h"

char * computeOutputFileName(const char * inputName) {
  int l;
  char *out;

  l = strlen(inputName);
  out = malloc(l + 8); 
  memcpy(out, inputName, l);
  memcpy(out + l, ".counts", 8);
  return out;
}


