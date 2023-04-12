#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>


int
main(int argc, char *argv[]) {
	
	int fd[2];

	if (pipe(fd) == -1)
		return 1;
	
	char* string = "Hello\n";
	write(fd[1], string, strlen(string));
	
	char* buffer[10];
	read(fd[0], buffer, strlen(string));

	fprintf(stdout, "%s", buffer);

	return 0;
}
