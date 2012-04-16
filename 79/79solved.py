file = open('keylog.txt','r')
lines = file.readlines()
lin = []
for x in lines:
	lin.append(x.strip())
linset = set(lin)
print linset,len(linset)

#this problem is really easy if u run this program and do the rest on pencil
#and paper, in theory they could have made this problem MUCH harder.
