def palindrome(x):
	l = list(x)
	l.reverse()
	a = ""
	a = a.join(l)
	print a,x
	return a == x

def ispandigital(x):
	slist = set(range(1,len(str(x))+1))
	l = []
	for i in str(x):
		l.append(int(i))
	return slist.issubset(set(l))

def isprime(n):
	n = abs(int(n))

	if n < 2:
		return False
	if n == 2:
		return True
	if not n & 1:
		return False
	for x in range(3, int(n**0.5)+1, 2):
		if n % x == 0:
			return False
	return True	
