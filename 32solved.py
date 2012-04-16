def is_pandigital(a,b,c):
	word = str(a)+str(b)+str(c)
	if len(word) != 9:
		return False
	wordset = set('123456789')
	word = set(word)
	return wordset.issubset(word)

answer = outer = inner = 1
sum = 0
mset = set([])
while outer < 2000:
	inner = 0
	while inner < 2000:
		answer = inner*outer
		if is_pandigital(inner,outer,answer):
			if answer not in mset:
				sum+=answer
				mset.add(answer)
		inner+=1
	outer+=1

print sum		
#print is_pandigital(2222,22222,2222)
#print is_pandigital(785,456,123)
#print is_pandigital(789,456,123)


