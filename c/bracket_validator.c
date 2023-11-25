#include <stdio.h>
#include <string.h>

#define STACK_SIZE 1024


typedef struct _stack {
	char cells[STACK_SIZE];
	int tip;
} Stack;

void init_stack(Stack* stack) {
	stack->tip = 0;
	for (int i=0; i<STACK_SIZE; i++)
		stack->cells[i] = 0;
}

int is_string_valid(char* string, size_t length) {
	Stack stack;
	init_stack(&stack);
	for (int i=0; i<length; i++) {
		switch (string[i]) {
			case '(':
				stack.cells[stack.tip] = '(';
				stack.tip++;
				break;
			case ')':
				if (stack.cells[stack.tip-1] == '(')
					stack.tip--;	
				else
					return 0;
				break;
			case '[':
				stack.cells[stack.tip] = '[';
				stack.tip++;
				break;
			case ']':
				if (stack.cells[stack.tip-1] == '[')
					stack.tip--;	
				else
					return 0;
				break;
			case '{':
				stack.cells[stack.tip] = '{';
				stack.tip++;
				break;
			case '}':
				if (stack.cells[stack.tip-1] == '{')
					stack.tip--;	
				else
					return 0;
				break;
		}
	}
	return stack.tip == 0 ? 1:0;
}


int
main(int argc, char *argv[]) {
	if(is_string_valid(argv[1], strlen(argv[1])))
		puts("Input is valid!");
	else 
		puts("Input is invalid!");
	return 0;
}
