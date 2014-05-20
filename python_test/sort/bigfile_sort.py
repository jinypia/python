def bigsort(filename):
	lines = []
	f = open(filename, 'r')
	line = f.readline()
	for lines in line:
		print line
		lines.append(line)
	f.close()
	lines.sort()
	print "sort finished"

	f = open("result.txt", 'w')
	while lines == '\n':
		f.write(lines)
	f.close()


bigsort('a.txt')
