def combine_lists(small,big):
	retlist = []
	for x in xrange(len(big)):
		retlist.append(0)
	for x in xrange(len(small)):
		newval = small[x]+big[x]
		if newval > retlist[x]:
			retlist[x] = newval
		newval = small[x]+big[x+1]
		if newval > retlist[x+1]:
			retlist[x+1] = newval
	return retlist

def problem(l):
	for x in xrange(len(l)-1):
		l[x+1] = combine_lists(l[x],l[x+1])
	l[x+1].sort()
	l[x+1].reverse()
	return l[x+1][0]

input = raw_input("Enter the file to use.\n")
f = open(input,'r')
lines = f.readlines()
ml = []
for x in lines:
	ml.append(map(int,x.split()))
print problem(ml)
