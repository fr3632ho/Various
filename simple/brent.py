import math

sequence = [1,2,3,4,5,6,6,7,8,9,10]

def f(x):
    if sequence.index(x)+1 == len(sequence):
        return sequence[0]
    return sequence[sequence.index(x)+1]

def brent(x0):
    power,lam = 1,1
    tortoise = x0
    hare = f(x0)

    # Beginning phase
    while tortoise != hare:
        if power == lam:
            tortoise = hare
            power *= 2
            lam = 0
        hare = f(hare)
        lam += 1

    hare = tortoise = x0
    for i in range(lam):
        hare = f(hare)

    mu = 0

    # End phase
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1

    return lam,mu,hare

x0 = 0
lam,mu,value = brent(sequence[x0])
print(
'''
start-index: {},
sequence: {},
cycle-length: {},
index from starting point (positive direction): {},
repeated value: {}'''.format(x0,sequence,lam,mu,value))
