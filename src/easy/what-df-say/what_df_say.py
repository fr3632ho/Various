import sys
from collections import defaultdict


def main():
    T = int(input())
    for i in range(T):
        recording = input().split()
        animals = defaultdict(list)

        q = sys.stdin.readline().split()
        while q[0] != "what":
            animals[q[0]] = q[2]
            q = sys.stdin.readline().split()


        values = animals.values()
        for i in recording:
            if i not in values:
                animals["fox"].append(i)

        print(" ".join(animals["fox"]))


if __name__=="__main__":
    main()
