#include <stdio.h>

typedef unsigned int big_t;

big_t total = 0;

big_t combo(big_t x, big_t accum, big_t endpoint)
{
	if(accum == endpoint) {
		total++;
	}
	else if(accum > endpoint) {
		return 0;
	}
	else {
		combo(x,accum+x,endpoint);
		if ( x < ( endpoint-1)) {
			combo(x+1,accum, endpoint);
		}
	}
}

int main(int argc, char * argv[])
{
	//190569291 is the answer
	//TAKES A LONG AS TIME UNLESS YOU USE -03 Optimization =)

	//printf("%d\n",combo_iter(5));
	int n = 0;
	printf("calculating %u\n", (n = atoi(argv[1])));
	combo(1,0,n);
	printf("total %u\n", total);
	return 0;
}
