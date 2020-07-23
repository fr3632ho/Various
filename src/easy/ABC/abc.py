import sys


def main():
    nums = list(map(int, input().split()))
    lookup = dict()
    a, c = min(nums), max(nums)
    b = [i for i in nums if a < i < c][0]

    lookup['A'], lookup['B'], lookup['C'] = str(a), str(b), str(c)
    res = []
    for i in input():
        res.append(lookup[i])

    print(' '.join(res))


if __name__== '__main__':
    main()
