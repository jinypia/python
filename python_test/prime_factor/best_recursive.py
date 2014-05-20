def Largest_prime(n):
    cnt = 2
    while cnt < n:
        if n % cnt  ==  0:
            Largest_prime(n/cnt)
            return 0
        cnt += 1
    print n

Largest_prime(600851475143)
