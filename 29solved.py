l = []
for x in xrange(2,101):
	for y in xrange(2,101):
		l.append(x**y)
l= set(l)
print len(l)
