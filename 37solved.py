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
def tester(x):
	if '0' in str(x):
		return False
	orig = x
	counter = 1
	while counter < len(str(orig)):
		counter+=1
		if isprime(x) == False:
			return False
		x = int(str(x)[1:])
	if isprime(x) == False:
		return False
	x = orig
	counter = 1
	while counter < len(str(orig)):
		counter+=1
		if isprime(x) == False:
			return False
		x = int(str(x)[:len(str(x))-1])
	return isprime(x)

start = 10
sum = 0
count = 0
while count < 11:
	if tester(start) == True:
		sum+= start
		count+=1
	start+=1
print sum
