#include <stdio.h>

struct {
  char *p;
  char c;
} unpacked;

struct __attribute__((__packed__)) {
  char *p;
  char c;
} packed;

int main() {
  printf("Size of unpacked: %d\n", sizeof(unpacked));
  printf("Size of packed: %d\n", sizeof(packed));
  return 0;
}
