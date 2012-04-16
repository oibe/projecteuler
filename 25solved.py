def num_len(x):
	counter = 0
	while x != 0:
		counter+=1
		x/=10
	return counter

def fib():
	counter = 2
	a = b = 1
	print 1, b
	while True:
		hold = num_len(b)
		print hold
		if hold == 1000:
			print 'count',counter
			return b
		temp = b
		b = a + b
		a = temp
		counter+=1
	
print 'answer',fib()
