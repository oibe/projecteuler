#include <stdio.h>
#include <stdlib.h>
#include "prime.h"

#define true 1
#define false 0

struct node{
	int data;
	struct node* next;
};
typedef struct node Node;

Node* generate_primes(int num)
{
	int i = 0;
	Node* head = NULL;
	Node* ptr = NULL;

	for(;i < num;i++){
		if(is_prime(i)){
			ptr = (Node*) malloc(sizeof(Node));
			ptr->data = i;
			ptr->next = head;
			head = ptr;
		}
	}
	return head;
}

int problem()
{
	int i = 9;
	int check = false;
	for(;;i+=2){
		Node* primes = generate_primes(i);
			check = false;

		while(primes != NULL){
			double temp = sqrt((i-primes->data)/2.0);
			if(fmod(temp,1) == 0){
				check = true;
			}
			primes = primes->next;
		}
		if(check == false && is_prime((double)i)==false){
			return i;
		}
	}
}

int main(){
	printf("%d\n",problem());
	return 0;
}
