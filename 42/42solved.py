def get_word_val(x):
	sum = counter = 0
	while counter < len(x):
		sum+= ord(x[counter])-64
		counter+=1
	return sum
	
def generate_tri_list(x):
	return map(lambda x:(x*(x+1))/2,xrange(1,(x+1)))

f = open("words.txt",'r')
line = f.readline()
l = line.split(',')
newlist = []
trilist = generate_tri_list(1000)
for x in l:
	newlist.append(x.strip('"\n'))
sum = 0
for x in newlist:
	temp = get_word_val(x)
	for y in trilist:
		if y == temp:
			sum+=1
			break
print sum
