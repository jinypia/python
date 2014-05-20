def josephus(num, rem):
	    
	'''
	1st round: 1 2 (3) 4 5 (6) 7 8 (9) 10
	2nd round:                            1 (2) 4 5 (7) 8 10
	3rd round:                                                (1) 4 5 (8) 10
	4th round:                                                               4 (5) 10
	5th round:                                                                        4 (10)
	initial data:
	10 3
	
	answer:
	4
	'''
	
	lst = []
	remlst = []
	for i in range(1, num + 1):
		lst.append(i)

	cnt = 1
	while len(lst) != 1:
		for i in lst:
			if cnt % rem == 0:
				remlst.append(i)
			cnt += 1
		
		for j in remlst:
			lst.remove(j)
			remlst = []

	print lst[0]


josephus(10, 3)
		
	
