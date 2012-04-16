def divlist(i):
	l = []
	for x in range(1,(i/2)+1):
		if i % x == 0:
			l.append(x)
	return sum(l) > i

#run each part in sequence

#part1	
#file = open("abundant.txt","w+")
#part1
#ml = []
#counter = 1
#while counter <= 28123:
#	if divlist(counter):
#		file.write(str(counter))
#		file.write("\n")
#	counter+=1

#part2
#fil = open("abundant.txt","r")
#outfile = open("2sums.txt","w+")
#lines = fil.readlines()
#number = 0
#se = set([])
#for x in lines:
#	for y in lines:
#		number = int(x)+int(y)
#		if number <= 28123:
#			se.add(str(number))
#for x in se:
#	outfile.write(x)
#	outfile.write("\n")

#part3
#fil = open("2sums.txt","r")
#outfile = open("2sums_sorted.txt","w+")
#lines = fil.readlines()
#ml = map(int, lines)
#ml.sort()
#for x in ml:
#	outfile.write(str(x))
#	outfile.write("\n")

#part4
fil = open("2sums_sorted.txt","r")
lines = fil.readlines()
ml = set(map(int,lines))
sum = 0
counter = 1
while counter <= 28123:
	if counter not in ml:
		sum+=counter
	counter+=1
print sum
