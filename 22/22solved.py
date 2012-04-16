def word_value(word):
	sum = 0
	for x in range(len(word)):
		sum+=(ord(word[x])-64)
	return sum

f = open("names.txt",'r')
lines = f.readline()
list = lines.split(",")
newlist = []
for x in list:
	newlist.append(x.strip('"'))
newlist.sort()

answer = 0
counter = 1
for x in newlist:
	answer+=word_value(x)*counter
	counter+=1
print answer
