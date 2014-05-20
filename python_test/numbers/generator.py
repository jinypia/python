# coding... 

def d():
	'''
	d(91) = 9 + 1 + 91 = 101
	1+0+0+100=101
	'''

	numlst = []
	genlst = []
	duplst = []
	for i in range(1,91):
		numlst.append(i)
		a = str(i)
		gen = 0
		for j in a:
			gen += int(j)
		gen += i
		if not gen in genlst:
			genlst.append(gen)
			numlst.append(i)
		else:
			duplst.append(i)
			numlst.remove(i)
	print genlst
	print duplst

d()
