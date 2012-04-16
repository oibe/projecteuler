f = open("input_file.txt",'r')
lines = f.readlines()
f.close()

list = []
for x in lines:
	list.append((x.strip("\n")).split(" "))	
def print_2d(list):
	for x in list:
		print x

def diag_helper(list,x,y):
	# x is columns
	# y is rows
	greatest = 0
	upperleft = upperright = lowerleft = lowerright = 1
	if x - 3 < 0:
		upperleft =  lowerleft = 0
	if x + 3 > 19:
		upperright = lowerright = 0
	if y - 3 < 0:
		upperleft = upperright = 0
	if y + 3 > 19:
		lowerleft = lowerright = 0
	if upperleft == 1:
		temp = list[x][y]*list[x-1][y-1]*list[x-2][y-2]*list[x-3][y-3]			
		if temp > greatest:
			greatest = temp
	if upperright == 1:
                temp = list[x][y]*list[x+1][y-1]*list[x+2][y-2]*list[x+3][y-3]
                if temp > greatest:
                        greatest = temp
	if lowerleft == 1:
                temp = list[x][y]*list[x-1][y+1]*list[x-2][y+2]*list[x-3][y+3]
                if temp > greatest:
                        greatest = temp
	if lowerright == 1:
                temp = list[x][y]*list[x+1][y+1]*list[x+2][y+2]*list[x+3][y+3]
                if temp > greatest:
                        greatest = temp		
	#print 'upperleft',upperleft
	#print 'upperright',upperright
	#print 'lowerleft',lowerleft
	#print 'lowerright',lowerright
	return greatest
def diag(list):
	great = 0
	for i in range(20):
		for j in range(20):
			temp = diag_helper(list,i,j)
			if great < temp:
				great = temp
	return great
def transpose(list):
	master_list = []
	for x in range(20):
		inner_list = []
		for row in list:	
			inner_list.append(row[x])
		master_list.append(inner_list)	
	return master_list

def convert_to_int(list):
	master_list = []
	for i in list:
		master_list.append(map(int,i))
	return master_list

def great_row_helper(list):
	result, start, end , product = 0, 0, 4, 0
	list = map(int, list)
	for x in list:
		temp = reduce(lambda x, y: x*y, list[start:end])
		if temp > result:
			result = temp
		start+=1
		end+=1
	return result

def great_row(doublelist):
	result = 0
	for x in doublelist:
		temp = great_row_helper(x)
		if temp > result:
			result = temp
	return result
#print_2d(list)
#print '\n'
print 'trans', great_row(transpose(list))
print 'norm', great_row(list)
list = convert_to_int(list)
#print_2d(list)
print 'diag', diag(list)
