import sys
from collections import defaultdict,deque
# '''
# Graphing solution. Too Slow.
# '''
# def in_same_set(G,v1,v2,n):
#     visited = [False] * n
#     stack = [v1]
#
#     while stack:
#
#         current_vertex = stack.pop()
#
#         if current_vertex == v2:
#             return True
#
#         if visited[current_vertex]:
#             continue
#
#         visited[current_vertex] = True
#
#         for neighbour in G[current_vertex]:
#             if neighbour == v2:
#                 return True
#             elif not visited[neighbour]:
#                 stack.append(neighbour)
#
#     return False
#
# '''
# Union solution, too slow
# '''
# def in_same(G,v1,v2):
#     return v1 in G[v2]


'''
Solution is still too slow, might have to implement this in Java.
'''
class Sets:

    def __init__(self,N):
        self.parents = [i for i in range(N)]
        self.sizes   = sizes   = [1]*N

    def find_parent(self,p):
        root = p
        while root != self.parents[root]:
            root = self.parents[root]
        while p != root:
            _p = self.parents[p]
            self.parents[p] = root
            p = _p

        return root

    def union(self,x,y):
        x_parent = self.find_parent(x)
        y_parent = self.find_parent(y)

        # Same root
        if x_parent == y_parent:
            return

        if self.sizes[x_parent] < self.sizes[y_parent]:
            self.parents[x_parent] = y_parent
            self.sizes[y_parent] += self.sizes[x_parent]
        else:
            self.parents[y_parent] = x_parent
            self.sizes[x_parent] += self.sizes[y_parent]

    def is_connected(self,x,y):
        if x == y:
            return True
        return self.find_parent(x) == self.find_parent(y)

'''
Solution is too slow.. Have to do something that keeps track of all existing children
for every set. Try creating sets that keep track on which sets are joined!
'''

data = []
for i in sys.stdin:
    data.append(i.rstrip().split())
    print(i)
N,Q = int(data[0][0]),int(data[0][1])

sets = Sets(N)

for i in data[1:]:
    print(f'Query: {i}')
    u,v = int(i[1]),int(i[2])
    if i[0] == '=':
        sets.union(u,v)
        print(sets.parents)
    else:
        if sets.is_connected(u,v):
            print("yes")
        else:
            print("no")
