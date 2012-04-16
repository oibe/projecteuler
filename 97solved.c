#include <stdio.h>
#include <stdlib.h>


int* createNumber(int number)
{
	int *array = malloc(sizeof(int)*10);
	int i = 9;
	for(; i >= 0; i--)
	{
		array[i] = number % 10;
		number/=10;
	}
	return array;
}

void printArray(int *array)
{
	int i = 0;
	for(;i < 10;i++)
	{
		printf("%d",array[i]);
	}
	printf("\n");
	return;
}

int* carryover(int* array,int index, int value)
{
	for(;index >= 0; index++)
	{
		array[index];
	}
}

int* power(int* base,int* exp)
{
	if(exp == 0)
	{
		return createNumber(1);
	}
	mult(
}

int* mult(int* top, int* bottom)
{
	//create int array of size 10
	int *answer = malloc(sizeof(int)*10);
	int carryover[10];
	//make i and j point to last index answer array
	int temp = 0;
	int check = 0;
	int i = 9;
	int j = 9;
	int k = 0;
	int index = 0;
	int second = 0;
	//initialize answer array
	for(; temp < 10;temp++)
	{
		answer[temp] = 0;
		carryover[temp] = 0;
	}
	int z = 9;
	for(; j >= 0; j--)	//hold bottom number fixed on last index then decrement
	{
		
		index = j;
		for(i = 9 ;i >= 0; i--)  //iterate by changing top number
		{

			
			temp = top[i]*bottom[j];	//multiply fixed bottom by every number in top
			if(index > 0)
			{
				carryover[index -1] = ((temp/10)%10);
			}
			check = (carryover[index]+temp) % 10;	
			answer[index] += (carryover[index]+temp) % 10;
		
			carryover[index] = 0;
			
			index--;
		}
		
	}
	for(; z >= 0; z--)
	{
		temp = answer[z];
		answer[z] = temp %10;
		if(z > 0){
		answer [z-1] += ((temp/10)%10);
		}
	}
	return answer;
}

int main()
{
	printArray(createNumber(5433));
	printArray(createNumber(5522));
	printArray(mult(createNumber(5433),createNumber(5522)));
}
