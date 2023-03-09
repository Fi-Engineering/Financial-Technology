#include <stdio.h>
#include <stdlib.h>

#define ROWS 10
#define COLUMNS 10


void error(const char *m)
{
	fprintf(stderr, "input not valid: %s\n", m);
	exit(EXIT_FAILURE);
}


void read_errors(char line[], FILE *f)
{
	
	int get;

	int j = 0;
	
	while(j<11)
	{ 
		get = fgetc(f);
		switch (get)
		{
			case EOF:
				if (j == COLUMNS) {
					error("EOF");
				} else {
					error("too short");
				}
				break;
			case '\n':
				if (j == COLUMNS) {
					line[COLUMNS] = '\0';
					return;
				} else {
					error("too short");
				}
				break;
			default:
				if (j < COLUMNS) {
					line[j++] = (char) get;
				} else {
					error("too long");
				}
				break;
		}
	}
}

void print(char R[ROWS][COLUMNS])
{
	int i;
	int j;

	for (i = 0; i < ROWS; i++) {
		for (j = 0; j < COLUMNS; j++) {
			
			putchar(R[COLUMNS-1-j][i]);
		}
		putchar('\n');
	}
}


int main(int argc, char *argv[])
{
	char matrix[ROWS][COLUMNS];
	FILE *f;
	int i;
	int get;

	if (argc != 2) {
		fprintf(stderr, "input incorrect\n");
		exit(EXIT_FAILURE);
	}
	
	if ((f = fopen(argv[1], "r")) == 0) {
		fprintf(stderr, "did not open %s\n", argv[1]);
		exit(EXIT_FAILURE);
	}
	
	for (i=0; i < ROWS; i++) {
		read_errors(matrix[i], f);
	}
	
	if ((get = fgetc(f)) != EOF) {
		fprintf(stderr, "invalid input\n");
		exit(EXIT_FAILURE);
	}
	fclose(f);

	print(matrix);

	return 0;
}
