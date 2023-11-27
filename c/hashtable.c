#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLE_SIZE 1024

typedef unsigned int HashResult;

typedef struct _item {
	char* key;
	void* value;
} Item;


typedef struct _node {
	Item* item;
	struct _node* next;
} Node;

 
typedef struct _hashtable {
	Node* cells[TABLE_SIZE];
} HashTable;

HashTable* new_hashtable() {
	return (HashTable*)calloc(1, sizeof(HashTable));
}

HashResult hash(char* string) {
	HashResult result = 0;
	while(*string != '\0')
		result += *(string++);
	return result % TABLE_SIZE;
}

void set_item(HashTable* ht, Item* item) {
	HashResult hash_result = hash(item->key);
	Node* node = (Node*)malloc(sizeof(Node));
	node->item = item;
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

Item* get_item(HashTable* ht, char* key) {
	HashResult hash_result = hash(key);
	if (ht->cells[hash_result] == NULL)
		return NULL;
	Node* node = ht->cells[hash_result];
	while (node->next != NULL) {
		if (!strcmp(key, node->item->key))
			return node->item;
		node = node->next;
	}
	return NULL;
}

void delete_item(HashTable* ht, char* key) {
}

int
main(int argc, char* argv[]) {
	HashTable* ht = new_hashtable();
	char* key1 = "hello";
	long int value1 = 32;
	Item x = {key1, (void*)value1};

	set_item(ht, &x);
	Item* y = get_item(ht, "hello");

	return 0;
}
