import math

sum2 = 0
square_sum = 0
for x in range(0,101):
    square_sum += math.pow(x,2)
    sum2 += x
print(math.pow(sum2,2) - square_sum)
