#include <stdio.h>
#include <math.h>
#include <stdlib.h>

struct node{
int data;
int count;
struct node* next;
};
typedef struct node* Node;

Node head = NULL;
void add(int data){
	if(data > 1000){
		return;
	}
	if(head == NULL){
		Node temp = malloc(sizeof(struct node));
		temp->data = data;
		temp->count = 1;
		temp->next = NULL;
		head = temp;		
		return;
	}
	Node ptr = head;
	while(ptr->next != NULL){
		if(ptr->data == data){
			ptr->count++;
			return;
		}
		ptr = ptr->next;
	}
	Node temp = malloc(sizeof(struct node));
	temp->data = data;
	temp->count = 1;
	temp->next = NULL;
	ptr->next = temp;
	return;
}

int main(int argc,char* argv[]){
	int i,j;
	float k = 0;
	for(i = 1;i <= 1000;i++){
		for(j = i;j <= 1000;j++){
			float z = (i*i+j*j);
			//printf("z = %f\n",z);
			k = sqrtf(z);
			//printf("k = %f\n",k);
			if(k - ((float)((int)k)) == 0.0){
			add(i+j+(int)k);
			}
		}
	}
	int highest= 0;
	int count= 0;
	Node ptr = head;
	for(; ptr != NULL; ptr = ptr->next){
		if(ptr->count > count){
			count = ptr->count;
			highest = ptr->data;
		}
	}
	printf("highest %d\ncount %d\n",highest,count);
	return 0;
}


