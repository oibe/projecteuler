from math import sqrt

def permute(str):
	l = []
	if len(str) == 1:
		l.append(str)
	else:
		for x in range(len(str)):
			for y in permute(str[0:x]+str[x+1:]):
				l.append(str[x]+y)
	return l

def use_permute(str):
	l = permute(str)
	n = []
	for x in range(len(l)):
		l[x] = int(l[x])
		n.append(l[x])
	return n

def is_prime(n):
        if n < 0:
                n*=-1

        if n < 2:
                return False
        
        if n == 2:
                return True       
 
        if (n % 2) == 0:
                return False
        
        i = 3
	while i < sqrt(n)+1:
		if (n % i) == 0:
			return False
		i+=2
        return True;



	
list = permute("1234567")
var = len(list) -1
while var > 0:
	if is_prime(int(list[var])) == True:
		print list[var]
		print 'entered'
		break
	var-=1
