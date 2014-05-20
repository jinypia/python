def optprint():
	'''
	>>> input data:
	2 		 # no of test case
	1 1 5	 # x, y, n : time for 1st prt, time for 2nd prt, no of paper
	3 5 4	 # 2nd test case 

	answer:
	3 9		 # elapse time to print per test case
	'''
	print ("input data:")
	notc = input()
	tc = []
	i = 0
	while i < notc:
		a = raw_input()
		tc.append(a)
		i += 1
	
	print ("")
	print ("answer:")

	j = 0
	while j < notc:
		tcx = tc[j].split(' ')
		k = 1
		elapse = []
		x = int(tcx[0])
		y = int(tcx[1])
		n = int(tcx[2])
		while k < n:
			elapse.append( max(x*k, y*(n-k)) )
			k += 1
		print min(elapse),
		j += 1
	return 
	
optprint()
