def num_len(x):
	sum = 0
	while x != 0:
		x/=10
		sum+=1
	return sum

def get_digit(i,num):
	count = (num_len(num)-1)-i
	while  count > 0:
		num/=10
		count-=1
	return num%10
def problem():
	start,sum = 1, 0
	while start < 3000000: #didn't know when to stop so I went to 3 million
		temp = 0
		for j in range(0,num_len(start)):
			temp += get_digit(j,start)**5
			#temp =((get_digit(0,start)**5)+(get_digit(1,start)**5)+(get_digit(2,start)**5)+(get_digit(3,start)**5))
		if start == temp:
			print 'temp',temp
			sum += temp
		start+=1
	return sum

#print num_len(3)
print problem()-1 # should not count 1 for this problem since 1 to any power is not technically summation blah blah

