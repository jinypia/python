def bubble_sort(a):
	'''
	bubble sort algorithm
	input :
	a = [3, 1, 4, 1, 5, 9, 2, 6]
	i < j, a[i] <= a[j]
	
	t = a[i]
	a[i] = a[j]
	a[j] = t
	
	output : 
	5 8 (number of loop, number of swap)
	'''
	n_loop = 0
	n_swap = 0
	while True:
		i = 0	
		n_loop += 1 
		swap_hist = n_swap
		while i < len(a)-1:
			if a[i] > a[i+1]:
				tmp = a[i]
				a[i] = a[i+1]
				a[i+1] = tmp
				n_swap += 1
			i += 1
		if swap_hist == n_swap:
			print n_loop, n_swap
			return()
	
a = [3, 1, 4, 1, 5, 9, 2, 6]
bubble_sort(a)
