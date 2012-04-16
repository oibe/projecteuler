months = [31,28,31,30,31,30,31,31,30,31,30,31]
year = 1901
day = [0,1,2,3,4,5,6]
start = 2
count = 0
while year < 2001:
	if year % 4 == 0 and start % 100 != 0:
		print year
		months[1] = 29
	else:
		months[1] = 28
	
	if year == 1996:
		months[1] = 29
	#print months[1],year,year%4
	for x in range(12):
		for y in range(months[x]):
			if start % 7 == 0 and y == 0:
				count+=1
			start+=1
	year+=1
print count
