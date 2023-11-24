#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int compare_words(char *a, char *b) {
	return ~strcmp(*(const char**)a, *(const char**)b);
}

void sort_words(char *words[], int count) {
	qsort(words, count, sizeof(words[0]), compare_words);
	
}

int
main() {
	char *words[] = { "cherry", "orange", "apple" };
	sort_words(words, 3);
	for (int i = 0; i < 3; i++) {
		printf("%s ", words[i]);
	}
	putc('\n', stdout);
}
