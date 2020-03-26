import math
import time


def isPrime(number):
    nbr = int(number)
    if nbr == 1:
        return False
    if nbr == 2:
        return True
    if nbr % 2 == 0:
        return False
    current = 3
    while current * current <= math.sqrt(nbr):
        if nbr % current == 0:
            return False
    return True

def divisibilityCounter(number):
    counter = 0
    current = 1
    while current <= math.sqrt(number):
        if number % current == 0:
            counter +=1
        current+=1
    #return number of divisors smaller or equal to square root of n. add divisor n in the end
    return counter+1

def sumOfNumbers(number):
    return (number * (number + 1))/2


n = 500
largest_number = 0
current_max = 0
current = 2
while current_max <= 500:
    i = sumOfNumbers(current)
    j = divisibilityCounter(i)
    if j >= 500:
        largest_number = i
        break
    current_max = j
    current +=1

print(largest_number)
