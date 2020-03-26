import math


def isPrime(number):
    for x in range(2,number):
        if number % x == 0:
            return False
    return True;

myPrimeList = list()
myNotPrimeList = list()
#Fixa primtalslistan och icke primtalslistan
for x in range(2,20):
    if isPrime(x):
        myPrimeList.append(x)
    else:
        myNotPrimeList.append(x)

starting_number = 1
all_numbers = list(range(2,20))

#Fixa starting_number
for x in myPrimeList:
    starting_number *= x

for x in myNotPrimeList:
    starting_number *= x
    bool = True
    for y in myNotPrimeList:
        if starting_number % y != 0:
            bool = False
    if bool:
        break



print("the smallest number divisible of all numbers in the range 1-20 is: ")
print(starting_number)
print()
