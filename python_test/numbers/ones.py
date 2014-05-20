def ones(num):
	i=1
	ones = []
	while i < num:
		if i % 2 != 0 and i % 5 != 0 :
			ones.append(i)
		i += 1
	print (ones)
	
ones(10000)
