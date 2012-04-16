def arrive(x):
	while(x != 89 and x != 1):
		term = 0
		for i in range(len(str(x))):
			term+=(x%10)**2
			if len(str(x)) > 1:
				x = x / (10**(i+1))
		x = term
		print x
		if x == 89:
			return True
		if x == 1:
			return False

start = 1
counter = 0
while start < 10000000:
	if arrive(start):
		counter+=1
	start+=1
	print start
print counter
