import math

def right_triangle(n):
    found = []
    count = 0
    for a in range(3, n+1, 3):
        if a in found: continue
        for b in range(1, n+1-a):
            c = math.sqrt(a**2+b**2)
            if a+b+c == n:
                found+=[a,b,c]
                count+=1
    return count


m = -1
found = -1
for i in range(1, 1001):
    v = right_triangle(i)
    if v > m:
        m = v
        found = i

print found, m
