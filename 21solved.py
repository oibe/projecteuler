def d(n):
	start,end,sum = 1,((n/2)+1),0
	while start <= end:
		if n % start == 0:
			sum += start
		start+=1
	return sum
def find_pair_sum():
	a = sum = b  = 0
	while a < 10000:
		#print d(a),d(d(a))
		b = d(a)
		if a == d(b) and a != b:
			sum+=a
			print 'found one',a
		a+=1
	return sum

#a = 89
#b = d(a)
#print d(b),a
print 'here', find_pair_sum()

