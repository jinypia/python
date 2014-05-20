import random
def mk_ts_file(filename):
	a = [i for i in range(10000000)]
	random.shuffle(a)
	f = open(filename, 'w')
	for i in a:
		f.write(format(i,'07d')+'\n')
	f.close()

mk_ts_file('testfile.txt')
