print("read file")
f = open("new_file.txt", 'w')
# file open mode :  w - write, r - read, a - add

for i in range(1, 11):
	data = "%d line.\n" % i
	f.write(data)
f.close()

print("read line by line : 1")
f = open("new_file.txt", 'r')
while 1:
	line = f.readline()
	if not line: break
	print(line)
f.close()

print("read line by line : 2")
f = open("new_file.txt", 'r')
lines = f.readlines()
for line in lines:
	print(line)
f.close()


print("read line by line : 3")
f = open("new_file.txt", 'r')
data = f.read()
print(data)
f.close()

# f.tell() : file pointer position
# f.seek(0) : send back the pointer

