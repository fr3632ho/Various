import sys
from collections import deque

def get_neighbours(graph, u, r, c, allowed):
    n = []
    if u % c - 1 > 0:
        if graph[u-1] == allowed:
            n.append(u-1)
    if u % c + 1 < c:
        if graph[u+1] == allowed:
            n.append(u+1)
    if u - c > 0:
        if graph[u-c] == allowed:
            n.append(u-c)
    if u + c < r*c:
        if graph[u+c] == allowed:
            n.append(u + c)
    print(n)
    return n


def BFS(graph, start, end, allowed, r, c):
    if graph[start[0]][start[1]] != allowed or graph[end[0]][end[1]] != allowed:
        return False

    queue = deque([start])
    visited = set()

    while queue:
        print("in")
        u = queue.pop()

        # If path is found
        if u == end:
            return True

        visited.add(u)
        for i in get_neighbours(graph, u, r, c, allowed):
            if i not in visited:
                queue.appendleft(i)

    return False



'''
Binary has to stay inside path with zeros.
'''
def main():
    r, c = map(int, sys.stdin.readline().strip().split())
    graph = [sys.stdin.readline().strip() for _ in range(r)]
    print(graph)

    n = sys.stdin.readline().strip()
    for query in range(int(n)):
        r1, c1, r2, c2 = map(int, sys.stdin.readline().strip().split())
        start, end = (r1-1, c1-1), (r2-1, c2-1)
        print(start,'->' ,end)
        print(graph[start[0]][start[1]], graph[end[0]][end[1]])

        if BFS(graph, start, end, 0, r, c):
            sys.stdout.write('binary\n')
        elif BFS(graph, start, end, 1, r, c):
            sys.stdout.write('decimal\n')
        else:
            sys.stdout.write('neither\n')

if __name__ == "__main__":
    main()
