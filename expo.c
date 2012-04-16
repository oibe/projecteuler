#include <stdio.h>

int modular_pow(int base, int exponent, int modulus){
	int c = 1;
	int i = 1;
	for(;i <= exponent;i++){
			c = (c*base)%modulus;
	}
	return c;
}
int main(){
	int i = 1;
	for(;i <=13;i++){
		printf("exponent %d, answer %d\n",i,modular_pow(4,i,497));
	}
	return 0;
}
