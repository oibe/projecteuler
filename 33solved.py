def remove(input,arg):
	if len(input) is 1:
		return input
	count = 0
	for x in range(len(input)):
		if input[x] == arg:
			return input[(x+1)%2]
		count+=1
lis = []
for x in range(10,100):
	for y in range(10,100):
		l =[] 
		l.append(str(x))
		l.append(str(y))
		lis.append(l)
newlis = []
for y in lis:
	for v in y[0]:
		for d in y[1]:
			if y[0] != y[1]:
				if v == d and v != 0:
					y.append(v)
					newlis.append(y)		
finlis = []
for x in newlis:
	li = []
	li.append(remove(x[0],x[2]))
	li.append(remove(x[1],x[2]))
	finlis.append(li)

counter = 0
for x in range(len(finlis)):
	counter = 0
	for y in finlis[x]:
		newlis[x][counter] = int(newlis[x][counter])
		finlis[x][counter] = int(y)
		counter+=1
final = []

for x in range(len(finlis)):
	if finlis[x][1] != 0 and newlis[x][1] != 0 and newlis[x][0]%10 != 0:
		if float(finlis[x][0])/float(finlis[x][1]) == float(newlis[x][0])/float(newlis[x][1]) and float(finlis[x][0])/float(finlis[x][1]) < 1 :
			#print newlis[x][0],newlis[x][1]

			#print "\n"
			l = []
			l.append(finlis[x][0])
			l.append(finlis[x][1])
			final.append(l)
print "These are the four fractions just multiply them all then simplify and use the denominator"
print final
