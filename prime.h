#include <stdio.h>
#include <math.h>

int is_prime(float n){
	if(n < 0){
		n*=-1;
	}
	if(n < 2){
		return 0;
	}
	if(n == 2){
		return 1;
	}
	if((int)n % 2 == 0){
		return 0;
	}
	int i = 3;
	for(;i < ((int)sqrt(n))+1;i+=2){
		if((int)n%i == 0){
			return 0;
		}
	}
	return 1;
}
