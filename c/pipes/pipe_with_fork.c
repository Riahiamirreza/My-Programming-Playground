#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>



int
main(int argc, char *argv[]) {

	int fd[2];
	
	pipe(fd);

	int pid = fork();

	if (pid == -1)
		return 1;

	if (pid == 0) {
		/* child process */
		fprintf(stdout, "I'm the child.\n");
		char* message = "Hello parent!\n";
		write(fd[1], message, strlen(message));
	} else {
		/* parent process */
		fprintf(stdout, "I'm parent of this child %d\n", pid);
		char* buffer[15];
		read(fd[0], buffer, 15);
		fprintf(stdout, "The message received from child: %s", buffer);

	}

	return 0;
}
