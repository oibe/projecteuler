sum = 0
inc = 2
i = 0
term = 1
while  (inc-1) < 1001:
        sum+=term
	if i == 4:
		#print 'sum',sum
		i = 0
		inc+=2
		#print 'inc',inc-1
	term+=inc 
        i+=1
print sum
