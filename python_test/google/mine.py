cnt = 0
for i in range(1, 10000, 1):
	a = str(i)
	j = ""
	for j in a:
		if j == "8":
			cnt += 1
print cnt
print str(range(1,10000)).count('8')

