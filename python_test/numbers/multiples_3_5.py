num = 0
for i in range(1,1000):
	if i % 3 == 0 or i % 5 == 0:
		num += i

print num

# ref
print sum(list([x for x in range(1000) if x%3==0 or x%5==0]))
