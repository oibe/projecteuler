def word_from_digit(num):
	orignum = num
	retstr = ""
	place = 0
	teen =  int(str((num/10)%10)+str(num %10))
	if len(str(num)) >= 2 and teen > 9 and teen < 20:
		retstr = teenlist[teen %10]
		place+=2
		num/=100
	while num != 0:
		temp = num % 10
		if temp != 0:
			retstr = masterlist[place][temp-1] + retstr
		num/=10
		place+=1
	if orignum > 100 and retstr not in set(hundredlist):
		retstr += 'and'
	return retstr
			
teenlist = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']	
onelist = ['one','two','three','four','five','six','seven','eight','nine']
tenlist = ['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
hundredlist = ['onehundred','twohundred','threehundred','fourhundred','fivehundred','sixhundred','sevenhundred','eighthundred','ninehundred']
masterlist = []
masterlist.append(onelist)
masterlist.append(tenlist)
masterlist.append(hundredlist)

sum = 0
for x in range(1,1000):
	sum+=len(word_from_digit(x))
print sum+len('onethousand')

#for x in range(1,1000):
#	print word_from_digit(x)
