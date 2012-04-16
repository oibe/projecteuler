#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int len(int number)
{
	if(number == 0)
	{
		return 0;
	}
	return 1 + len(number/10);
}
int problem()
{
	//RETRACE ALL LOGIC
	int answer = 1;
	int power = 10;
	int counter = 1;
	int counter_end = 0;
	int start = 1;
	int end = 10;
	int array[10];
	int iter = 0;
	int memory = 5;
	char ptr[2];
	ptr[1]= '\0';
	while(counter_end <= 1000000){
		for(iter = start; iter <= end;iter++)
		{
			array[iter-start]=iter;
			memory+=len(iter);
		}
		char* container = malloc(sizeof(char)*memory);
		sprintf(container,"%d%d%d%d%d%d%d%d%d%d",array[0],array[1],array[2],array[3],array[4],array[5],array[6],array[7],array[8],array[9]);
		
		counter_end = (counter + strlen(container))-1;
		if( power >= counter && power <= counter_end)
		{
			ptr[0]=container[power-counter];
			answer*=atoi(ptr);//counter has 97th digit 83833
			power*=10;
			//power is 100
		}
		start+=10;
		end+=10;
		counter= counter_end+1;
		free(container);
	}
	return answer;
}

int main(int argc, char* argv[])
{
	printf("The answer is %d\n",problem());
	return 0;
}
