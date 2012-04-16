import math

def factorial(x):
	if x == 0:
		return 1
	return x * factorial(x - 1)
	

def problem(y):
	x = 3
	totalsum = 0
	while x < y:
		sum = 0
		v = x
		while v != 0:
			sum+=factorial(v % 10)
			v/=10
		#print x,sum
		if x == sum:
			totalsum+= sum
		x+=1
	return totalsum

print problem(1000000)


