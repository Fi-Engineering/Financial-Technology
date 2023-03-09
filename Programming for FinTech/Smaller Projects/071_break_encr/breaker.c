#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>


int count_frequency(int array[], int n)
{
	int max_id = 0;
	int i = 0;

	for (i; i < n; i++) {
		if (array[i] > array[max_id]) {
			max_id = i;
		}
	}
	return max_id;
}

int caesar_cipher(FILE *f)
{
	int freq[26] = {0};
	int h;
	int max_id;

	while ((h = fgetc(f)) != EOF) {
		if (isalpha(h)) {
			freq[tolower(h) - 'a']++;
		}
	}
	max_id = count_frequency(freq, 26);
	
	return (max_id + 22) % 26;
}

int main(int argc, char *argv[])
{
	FILE *f;
	int key;

	if (argc != 2) {
		fprintf(stderr, "usage %s file\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	f = fopen(argv[1], "r");
	if (f == NULL) {
		fprintf(stderr, "failed to open the file %s\n", argv[1]);
		exit(EXIT_FAILURE);
	}

	key = caesar_cipher(f);
	printf("%d\n", key);

	fclose(f);
	return 0;
}
