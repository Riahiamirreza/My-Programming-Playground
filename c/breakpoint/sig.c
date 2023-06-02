#include <signal.h>


int
main(int argc, char* argv[]) {

	raise(SIGINT); // the program will stop at this line.

	return 0;
}
