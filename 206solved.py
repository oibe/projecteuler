number = '1x2x3x4x5x6x7x8x9x0'

def change_val(num,x):
	num = list(num)
	num[1]=num[3]=num[5]=num[7]=num[9]=num[11]=num[13]=num[15]=num[17]=x
	st = ""
	for y in num:
		st = st + str(y)
	return int(st)

for x in range(10):
	print x,change_val(number,x)**.5
