#include <stdio.h>

long double nCr(long double n, long double r){
	if((n-r) > r){
		r = n-r;
	}
	long double number = 1;
	long double div = n-r;
	while(n > r){
		number*=n;
		n--;
	}
	while(div > 0){
		number/=div;
		div--;
	}
	return number;
}
int main(int argc, char* argv[]){
	int n,r;
	int count = 0;
	int check = 0;
	for(n=1;n <= 100;n++){
		for(r=n;r >0;r--){
			if(nCr(n,r) > 1000000){
				count++;
			}
		}
	}
	printf("count = %d\n",count);
	return 0;
}

