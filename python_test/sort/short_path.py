def shortpath(S):
	i = 0
	path = 0
	shortest = [0,0]
	shortpath = []
	while i < len(S)-1:
		path = S[i+1] - S[i]
		if path < shortest: 
			shortest = path
			shortpath = [S[i],S[i+1]]
		i += 1
	print shortpath

S = [1,3,4,8,13,17,20]
shortpath(S)
