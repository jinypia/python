def grpsort(lst):
	'''
	[a1,a2,a3,,,,an,b1,b2,b3...bn]
	->
	[a1,b1,a2,b2,,,an,bn]
	'''
	q1 = []
	q2 = []
	result = []
	for i in range(len(lst)):
		if i < len(lst)/2:
			q1.append(lst[i])
		else:
			q2.append(lst[i])
	for j in range(len(q1)):
		result.append(q1[j])
		result.append(q2[j])

	print result

a = ['a1','a2','a3','a4','a5','a6','b1','b2','b3','b4','b5','b6']
grpsort(a)
