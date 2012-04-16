#include <stdio.h>
#include "prime.h"

/*GLOBAL VARIABLES*/
int a,b,count = 0;

int prime_chain(int x, int y){
	int n = 0;
	int inner_count = 0;
	while(is_prime(n*n + x*n + y)){
		inner_count++;
		n++;
	}
	/*inner_count stans for how many primes*/
	return inner_count;
}

int main(int argc, char* argv[]){
	int i,j,temp = 0;
	for(i = -1000;i < 999;i++){
		for(j = -1000;j < 999;j++){
			temp = prime_chain(i,j);
			if(temp  > count){
				a = i;
				b = j;
				count = temp;
			}
		}
		//printf("%d/999\n",i);
	}
	printf("a = %d\nb = %d\ncount = %d\nmultiply%d\n",a,b,count,a*b);
	return 0;
}
