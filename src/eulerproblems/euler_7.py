import math

def isPrime(number):
    if number == 1:
        return False
    if number % 2 == 0:
        return False

    current = 3
    while (current * current) <= number:
        if number % current == 0:
            return False
        else:
            current+=2

    return True

tracker = 0
current_number = 0
while tracker != 10001:
    current_number += 1
    if isPrime(current_number):
        tracker+=1

print(current_number)
