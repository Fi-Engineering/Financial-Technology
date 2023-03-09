#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "kv.h"


static void parseLine(kvpair_t *pair, const char *line)
{
  const char *n, *m;

  n = strchr(line, '=');
  if (n == NULL) {
    goto fail;
  }

  pair->key = strndup(line, (size_t) (n - line));
  m = strchr(++n, '\n');
  if (m == NULL) {
    goto fail;
  }
  pair->value = strndup(n, (size_t) (m - n));
  if (pair->key == NULL || pair->value == NULL) {
    goto fail;
  }
  return;
fail:
  fprintf(stderr, "invalid input\n");
  exit(EXIT_FAILURE);
}



static void errorExit(void)
{
  perror("kv");
  exit(EXIT_FAILURE);
}



kvarray_t * readKVs(const char * fn) {
  FILE *f;
  char *line = NULL;
  size_t lines = 0;
  kvpair_t *base = 0;
  size_t npairs = 0;
  kvarray_t *a;

  f = fopen(fn, "r");
  if (f == NULL) {
    errorExit();
  }

  while (getline(&line, &lines, f) != -1) {
    base = realloc(base, (npairs+1) * sizeof *base);
    if (base == NULL) {
      errorExit();
    }
    parseLine(&base[npairs++], line);
  }
  if (!feof(f)) {
    errorExit();
  }
  free(line);
  fclose(f);

  a = malloc(sizeof *a);
  if (a == NULL) {
    errorExit();
  }
  a->base = base;
  a->len = npairs;
  return a;
}

void freeKVs(kvarray_t * pairs) {
  int i;

  for (i = 0; i < pairs->len; i++) {
    free(pairs->base[i].key);
    free(pairs->base[i].value);
  }
  free(pairs->base);
  free(pairs);
}

void printKVs(kvarray_t * pairs) {
  int i;
  kvpair_t *p;

  for (i = 0; i < pairs->len; i++) {
    p = &pairs->base[i];
    printf("key = '%s' value = '%s'\n", p->key, p->value);
  }
}

char * lookupValue(kvarray_t * pairs, const char * key) {
  int i;
  kvpair_t *p;

  for (i = 0; i < pairs->len; i++) {
    p = &pairs->base[i];
    if (strcmp(key, p->key) == 0) {
      return p->value;
    }
  }
  return NULL;
}


