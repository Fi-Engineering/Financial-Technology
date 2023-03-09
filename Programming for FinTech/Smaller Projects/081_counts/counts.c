#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include "counts.h"


counts_t * createCounts(void) {
  counts_t *c;

  c = malloc(sizeof *c);
  if (c == 0) {
    perror("counts");
    exit(EXIT_FAILURE);
  }
  c->base = NULL;
  c->len = 0;
  c->unknowns = 0;
  return c;
}

void addCount(counts_t * c, const char * name) {
  int i;
  one_count_t *n;

  assert(c != NULL);

  if (name == NULL) {
    c->unknowns++;
    return;
  }
  for (i = 0; i < c->len; i++) {
    n = &c->base[i];
    if (strcmp(n->key, name) == 0) {
      break;
    }
  }
  if (i == c->len) {
    c->base = realloc(c->base, (c->len + 1) * sizeof c->base[0]);
    if (c->base == NULL) {
      perror("counts");
      exit(EXIT_FAILURE);
    }
    n = &c->base[c->len++];
    n->key = strdup(name);
    if (n->key == NULL) {
      perror("counts");
      exit(EXIT_FAILURE);    }
    n->count = 0;
  }
  n->count++;
}

void printCounts(counts_t * c, FILE * outFile) {
  int i;
  one_count_t *m;

  for (i = 0; i < c->len; i++) {
    m = &c->base[i];
    fprintf(outFile, "%s: %d\n", m->key, m->count);
  }
  if (c->unknowns > 0) {
    fprintf(outFile, "<unknown> : %d\n", c->unknowns);
  }
}

void freeCounts(counts_t * c) {
  int i;
  one_count_t *n;

  for (i = 0; i < c->len; i++) {
    n = &c->base[i];
    free(n->key);
  }
  free(c->base);
  free(c);
}


