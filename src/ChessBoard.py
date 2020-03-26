import math

"""
Following a simple formula for the sum of powers of k, were k = 1,2,...,n.
=> n(n+1)(2n+1)/6!
"""

def nbrOfSquaresInBoard(n):
    x1 = n*(n+1)
    x2 = 2*n + 1
    return int((x1*x2)/6)

n = 3
print("""
Number of squares in a nxn board were
n = {}
squares = {}
""".format(n,nbrOfSquaresInBoard(n)))
n = 4
print("""
Number of squares in a nxn board were
n = {}
squares = {}
""".format(n,nbrOfSquaresInBoard(n)))

n = 5
print("""
Number of squares in a nxn board were
n = {}
squares = {}
""".format(n,nbrOfSquaresInBoard(n)))

n = 6
print("""
Number of squares in a nxn board were
n = {}
squares = {}
""".format(n,nbrOfSquaresInBoard(n)))
