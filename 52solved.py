
def equals(a,b):
	if a.issubset(b) and b.issubset(a):
		return True
	return False

def problem(list):
	set1 = set(str(list[0]))
	set2 = set(str(list[1]))
	set3 = set(str(list[2]))
	set4 = set(str(list[3]))
	set5 = set(str(list[4]))
	set6 = set(str(list[5]))
	if equals(set1,set2) and equals(set2,set3) and equals(set3,set4) and equals(set4,set5) and equals(set5,set6):
		return True
	return False

number = 1
list = [number*1,number*2,number*3,number*4,number*5,number*6]

while problem(list) is False:
	list = []
	for x in range(1,7):
		list.append(number*x)
	number+=1
print number-1
