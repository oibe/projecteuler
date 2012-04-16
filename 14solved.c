#include <stdio.h>

int collatz(long long  x){
	int counter = 0;
	while(x != 1){
		/*if(hold > 113000){
			printf("col %d: %d\n",hold,x);
		}*/
		counter++;
		if(x%2==0){
			x/=2;
		}
		else{
			x*=3;
			x++;
		}
	}
	return 1+counter;
}
int main(){
	long long i=1;
	int check = 0;
	int temp = 0;
	int start = 0;
	while(i < 1000000){
		temp = collatz(i);
		if(temp > check){
			check = temp;
			start = i;
		}
		i++;
		if(i % 100000 == 0){
		printf("i = %d\n",i);
		}
	}
	printf("answer %d\n",check);
	printf("real answer %d\n",start);
}
