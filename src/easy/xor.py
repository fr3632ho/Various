import sys

'''
Bitwise XOR for all numbers in range [0, n]. Done by manipulating the XOR pattern
when doing bitwise operations =>

res = [n, 1, n+1, 0]

0000 -> 0 => 0 == res[0]
0001 -> 1 => 1 == res[1]
0010 -> 2 => 3 == res[2]
0011 -> 3 => 0 == res[3]
0100 -> 4 => 4 == res[0]
0101 -> 5 => 1 == res[1]
0110 -> 6 => 7 == res[2]
0111 -> 7 => 0 == res[3]

See the pattern above, which explains the solution
'''
def xor(n):
    res = [n, 1, n+1, 0]
    return res[n%4]


'''
XOR(5^6^7^8) = XOR(1^2^3^4^5^6^7^8)^(1^2^3^4), a = 5, b = 8

=> XOR([a, b]) = [0,b]^[0,a]
'''
def xorRange(a, b):
    if a == b:
        return a
    if b - a == 1:
        return a^b

    return xor(b)^xor(a-1)

'''
count := length
checksum := 0
for every r in [start, start + length^2] and step with length
    xor range [r, r + count] to checksum
'''
def answer(start, length):
    checksum = 0
    c = length
    for i in range(start, start + length*length, length):
        checksum ^= xorRange(i, i + c - 1)
        c -= 1

    return checksum



def run():
    start, length = [int(i) for i in input().split()]
    print(answer(start, length))


if __name__ == "__main__":
    run()
