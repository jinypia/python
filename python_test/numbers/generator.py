# coding... 

def d(num):
	'''
	d(91) = 9 + 1 + 91 = 101
	1+0+0+100=101
	generator = 91
	'''
	val = 0
	if num >= 10:
		val = val + num
	for i in str(num):
		val += int(i)
	return val

gen = {}
for i in range(1,31):
	gen[i] = d(i)

print gen


