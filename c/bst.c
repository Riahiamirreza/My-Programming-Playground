#include <stdio.h>


typedef struct Node {
	int value;
	struct Node *left;
	struct Node *right;
} Node;

int contains(const Node *root, int value) {
	if (root->value == value)
		return 1;
	if (root->left == NULL && root->right == NULL)
		return 0;
	return value < root->value ? contains(root->left, value): contains(root->right, value);
}


int main() {
	Node n1 = {.value=1, .left=NULL, .right=NULL};
	Node n3 = {.value=3, .left=NULL, .right=NULL};
	Node n2 = {.value=2, .left=&n1, .right=&n3};
	printf("%d\n", contains(&n2, 3));
	printf("%d\n", contains(&n2, 2));
	printf("%d\n", contains(&n2, 1));
	printf("%d\n", contains(&n2, 6));
} 
