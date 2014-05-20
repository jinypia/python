def prime_factor(num):
   '''
   >>> prime_factor(13195)
   5, 7, 13, 29
   '''
#   print type(num)
   prime = []
   cnt = 2
   while cnt < num + 1 : 
      if num % cnt == 0:
         no = num/cnt
#         print cnt
         prime.append(cnt)
         num = num/cnt 
      cnt += 1
   return prime   
      
print max(prime_factor(600851475143))
#print max(prime_factor(13195))
      
