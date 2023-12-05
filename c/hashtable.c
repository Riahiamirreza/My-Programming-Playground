#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define TABLE_SIZE 1

typedef unsigned int HashResult;


typedef struct _node {
	char *key;
	void *value;
	struct _node* next;
} Node;

 
typedef struct _hashtable {
	Node **cells;
	size_t size;
} HashTable;


HashTable* new_hashtable(size_t size) {
	HashTable* ht = (HashTable*)calloc(1, sizeof(HashTable));
	Node **cells = calloc(size, sizeof(Node));
	ht->cells = cells;
	ht->size = size;
	return ht;
}


HashResult hash(char* string) {
	HashResult result = 0;
	while(*string != '\0')
		result += *(string++);
	return result;
}

void set(HashTable* ht, char *key, void *value) {
	HashResult hash_result = hash(key) % ht->size;
	Node* node = (Node*)malloc(sizeof(Node));
	node->key = key;
	node->value = value;
	node->next = NULL;
	if (ht->cells[hash_result] == NULL) {
		ht->cells[hash_result] = node;
	} else {
		Node* root = ht->cells[hash_result];
		while (root->next != NULL)
			root = root->next;
		root->next = node;
	}
}

void* get(HashTable* ht, char* key) {
	HashResult hash_result = hash(key) % ht->size;
	if (ht->cells[hash_result] == NULL)
		return NULL;
	Node* node = ht->cells[hash_result];
	if (!strcmp(key, node->key))
			return node->value;
	do {
		if (!strcmp(key, node->key))
			return node->value;
		node = node->next;
	}
	while (node != NULL);

	return NULL;
}

void delete(HashTable* ht, char* key) {
	void *i = get(ht, key);
	if (i == NULL)
		return;
	HashResult hash_result = hash(key) % ht->size;
	Node *current, *prev, *temp;
	current = ht->cells[hash_result];
	if (!strcmp(current->key, key)) {
		free(current);
		current = NULL;
		ht->cells[hash_result] = NULL;
		return;
	}
	while (current->next != NULL) {
		temp = current;
		current = current->next;
		prev = temp;
		if (!strcmp(current->key, key)) {
			free(current);
			current = NULL;
			prev->next = NULL;
			return;
		}
	}
}

void print_chain(Node *root) {
	while (root != NULL) {
		fprintf(stdout, "Node at %p ", root);
		fprintf(stdout, "k: %s, v: %p ", root->key, root->value);
		root = root->next;
	}
}

void print_table(HashTable *ht) {
	for (int i=0; i < ht->size; i++) {
		fprintf(stdout, "%1d-------", i);
		putc('\n', stdout);
		if (ht->cells[i] == NULL)
			fprintf(stdout, "empty cell");
		else
			print_chain(ht->cells[i]);
		putc('\n', stdout);
	}
}

int
main(int argc, char* argv[]) {
	HashTable* ht = new_hashtable(8);
	while (!feof(stdin)) {
		fprintf(stdout, ">>> ");
		char input[256];
		fgets(input, 256, stdin);
		char *command;
		command = strtok(input, " ");
		if (!strcmp(command, "SET")) {
			char *sub = &input[(int)strlen(command) + 1];
			char *key = strtok(sub, " ");
			sub = &input[(int)strlen(command) + (int)strlen(key) + 2];
			char *value = strtok(sub, "\n");
			key = strncpy(malloc(strlen(key)), key, strlen(key));
			value = strncpy(malloc(strlen(value)), value, strlen(value));
			set(ht, key, (void*)value);
		} else if (!strcmp(command, "GET")) {
			char *sub = &input[(int)strlen(command) + 1];
			char *key = strtok(sub, "\n");
			char *value = get(ht, key);	
			fprintf(stdout, "%s\n", (char*)value);
		} else if (!strcmp(command, "DEL") || !strcmp(command, "DELETE")) {
			char *sub = &input[(int)strlen(command) + 1];
			char *key = strtok(sub, "\n");
			delete(ht, key);
		} else if (!strcmp(command, "SHOW") || !strcmp(command, "SHOW\n")) {
			print_table(ht);
		} else if (input[0] != '\n') {
			puts("Invalid command!");
		}
	}
	free(ht);

	return 0;
}
