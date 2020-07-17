import sys, math

'''
Floyd-Warshall algorithm for all pairs shortest path.
Takes a matrix A with set edge relations and computes minimal distance between
each and every node.
'''
def floyd_warshall(A, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                A[i][j] = min(A[i][j], A[i][k] + A[k][j])

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = -math.inf

def main():
    n, m, q = map(int, sys.stdin.readline().split())
    while True:
        # Create matrix
        matrix = [[math.inf for i in range(n)] for j in range(n)]

        # Add the edge relations!
        for edge in range(m):
            u, v, w = map(int, sys.stdin.readline().split())
            if u == v:
                matrix[u][v] = 0
            else:
                matrix[u][v] = w

        floyd_warshall(matrix, n)

        # Queries to be answered
        for query in range(q):
            u, v = map(int, sys.stdin.readline().split())

            dist = matrix[u][v]
            if dist == -math.inf:
                print('-Infinity')
            elif dist == math.inf:
                print('Impossible')
            else:
                print(dist)
                
        n, m, q = map(int, sys.stdin.readline().split())

        if not (n + m + q):
            break
        print()

if __name__ == '__main__':
    main()
