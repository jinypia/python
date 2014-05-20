def insertion(lst):
	tmp = 0
	for p in range(1,len(lst)):
		for i in range(p):
			if lst[i] > lst[p]:
				j = p
				tmp = lst[p]	
				while j > i:
					lst[j] = lst[j-1]
					j -= 1
				lst[j] = tmp
	print lst

a = [5,2,4,6,1,3]
insertion(a)
