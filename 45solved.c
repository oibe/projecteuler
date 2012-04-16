#include <stdio.h>
#include <math.h>

#define MAX(x,y) (x) > (y) ? (x) : (y)

//some sort of doubleing point error that propogates to change final result
//quadratic formula is off?
//i'm skipping some value i shouldn't be
double discr(double a,double b, double c){
	return b*b-4*a*c;
}

double quad(double a, double b, double c){
	double disc = b*b-4.0*a*c;
	if(disc < 0){
		return 3.5;	//return anything not divisible by 1
	}
	double temp =  (-1.0*b+sqrtf(disc))/(2.0*a);
	double temp2 = (-1.0*b-sqrtf(disc))/(2.0*a);
	return MAX(temp,temp2);
}

int main(){
	double hex_num = 0.0;

	double n = 2.0;
	int number = 1;	
	int count = 0;
	double hex_total = 0;
	while(count < 2){
		hex_num = 2.0*n*n-n;
		if( fmod(quad(.5,.5,-1*hex_num), 1.0) != 0 || fmod(quad(1.5,-.5,-1*hex_num),1.0) != 0 ){
			
			n++;
			continue;
		}
		//this means that you found an integer solution that hex is equal to 
		//tri and penta should be equal, but aren't this is the main problem
		double tri =quad(.5,.5,-1*hex_num);
		double penta = quad(1.5,-.5,-1*hex_num);
		double hex = n;
		
		double tri_total = (tri*tri+tri)/2.0;
		double penta_total = (3.0*penta*penta - penta)/2.0;
		hex_total = 2.0*hex*hex-hex;
		if(tri_total == penta_total && penta_total == hex_total){
			printf("**********************\n");
			printf("%d\n",number++);
			printf("total = %lf\n",hex_total);
			printf("tri \t\t%lf\n",tri);
			printf("penta \t\t%lf\n",penta);
			printf("hex \t\t%lf\n",hex);
			printf("tri total \t%lf\n",tri_total);
			printf("penta total \t%lf\n",penta_total);
			printf("hex_total \t%lf\n",hex_total);
			printf("**********************\n");
			count++;
		}
		n++;
	}
	printf("The answer is: %lf\n",hex_total);
	return 0;
}
