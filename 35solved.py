def num_digits(x):
	return len(str(x))

def num_rotate(x):
	return str(x)[1:] + str(x)[0]

def isprime(n):
	n = abs(int(n))
	if n < 2:
		return False
	if n == 2:
		return True
	if not n & 1:
		return False
	for x in range(3, int(n**0.5)+1,2):
		if n % x == 0:
			return False
	return True	

def circular_prime(x):	
	counter = 0
	init = x
	strform = str(x)
	while counter < num_digits(init):
		if isprime(x) == False:
			return False
		strform = num_rotate(strform)
		x = int(strform)
		counter+=1	
	return True

def find_circular_primes_up_to(x):
	sum ,counter = 0, 2
	while counter < x:
		if circular_prime(counter) == True:
			sum+=1
		counter+=1
	return sum

#print circular_prime(907)
print find_circular_primes_up_to(1000000)

