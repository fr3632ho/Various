import math

n = 600851475143
n2 = n
largest_prime = 1
i = 1
while i < math.sqrt(n):
     if n2 % i == 0 :
         largest_prime = i
         n2 = n2 / i
         i += 1
     i+=1
print(largest_prime)
