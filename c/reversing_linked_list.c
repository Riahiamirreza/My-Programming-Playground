#include <stdio.h>


typedef struct _node {
        int value;
        struct _node* next;    
} Node;


void traverse(Node* root) {
        if (root->next != NULL) {
		printf("%d\n", root->value);
                traverse(root->next);
	}
}

void reverse(Node* root) {
        Node *next, *prev, *first;
        first = root;
        prev = first;
        root = root->next;
        do {
                next = root->next;      
                root->next = prev;
                prev = root;
                root = next;
        }
        while (next->next != NULL);
        first->next = next;
}

int main(int argc, char *argv[]) {
        Node n6 = {0, NULL};
        Node n5 = {5, &n6};
        Node n4 = {4, &n5};
        Node n3 = {3, &n4};
        Node n2 = {2, &n3};
        Node n1 = {1, &n2};
        
        traverse(&n1);
        reverse(&n1);
        traverse(&n5);

        return 0;
}
