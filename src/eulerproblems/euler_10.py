import time
import math

t0 = time.time()

def isPrime(number):
    if number == 1:
        return False
    if number == 2:
        return True

    if number % 2:
        return False

    current = 3
    while (current * current) <= number:
        if number % current == 0:
            return False
        else:
            current+=1
    return True

def zeroSome(number, oldList,index):
    newList = list(oldList[0:index])
    print(index)
    for x in range(iterator, len(oldList)):
        if oldList[x] % number != 0 or oldList[x] == number:
            newList.append(oldList[x])
    return newList


print("Sieve of Eraosthenes \n")

N = 2000000
myList = list(range(3,2000001,2))
print(myList[0])
print()
p = 3
index = myList.index(p)
sum = 0
iterator = 0
#print(len(myList))

while math.pow(p,2) <= N:
    newList = zeroSome(myList[iterator],myList,iterator)
    myList = newList
    iterator +=1
    p = newList[iterator]

t1 = time.time()
total = t1 - t0

for x in myList:
    sum += x
sum +=2
print(sum)
print(total)
