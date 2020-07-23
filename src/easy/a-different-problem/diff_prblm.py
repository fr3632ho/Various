import sys

def main():
    while True:
        try:
            query = sys.stdin.readline().split()
            if len(query) == 0:
                break
            u, v = map(int, query)
            print(abs(u - v))
        except EOFError:
            break

if __name__ == '__main__':
    main()
