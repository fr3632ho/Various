import sys
from fractions import gcd

class Graph:

    def __init__(self,N):
        self.N         = N
        self.graph     = dict()
        self.weights   = [0]*N
        self.terminals = []

    def add_edge(self,u,v, weight):
        if weight != 0:
            if u in self.graph.keys():
                self.graph[u].append((v,weight))
            else:
                self.graph[u] = [(v,weight)]
            self.weights[u] += weight

    def set_terminals(self):
        for p in range(self.N):
            if self.weights[p] == 0:
                self.terminals.append(p)

    def __str__(self):
        s = ""
        for key,value in self.graph.items():
            s += '{} -> {}'.format(key, value)
            s += '\n'
        return s

    def dfs_helper(self, u, visited, p):
        visited[u] = True
        for n, weight in self.graph[u]:
            if not visited[n] and n in self.graph.keys():
                p[n] = (u, weight)
                self.dfs_helper(n,visited, p)
            elif not visited[n]:
                visited[n] = True
                p[n] = (u, weight)

    def dfs(self, N, start):
        visited, parents = [False]*N, [(-1, 0)]*N
        visited[start] = True

        for n, weight in self.graph[start]:
            if not visited[n] and n in self.graph.keys():
                parents[n] = (start, weight)
                self.dfs_helper(n, visited, parents)
            elif not visited[n]:
                visited[n], parents[n] = True, (start, weight)

        result = []
        start_weight = self.weights[start]
        for i in self.terminals:
            calcs = [1, 1]
            root, gcd_i = i, 1
            while parents[root][0] != -1:
                # Set the numerator to that of the weight
                calcs[0] *= parents[root][1]
                if self.weights[root] != 0:
                    calcs[1] *= self.weights[root]

                root = parents[root][0]

            # Update the root weights
            if root != i:
                calcs[0] *= parents[root][1] + 1
                calcs[1] *= start_weight
                gcd_i = gcd(calcs[0],calcs[1])
                calcs[0], calcs[1] = calcs[0]/gcd_i, calcs[1]/gcd_i
            else:
                calcs[0] = 0

            result.append(calcs)

        return result

def calculate_lcm(arr):
    lcm = arr[0][1]
    for i in arr[1:]:
        lcm = i[1]*lcm / gcd(lcm,i[1])
    return lcm

def solution(m):
    # Setup graph
    G = Graph(len(m))
    [[G.add_edge(i,j,m[i][j]) for j in range(len(m))] for i in range(len(m))]
    G.set_terminals()

    # Calculate paths
    results = G.dfs(len(m), 0)
    lcm = calculate_lcm(results)
    arr = [0]*len(results)
    arr.append(lcm)
    for i in range(len(results)):
        cur = results[i][1]
        if cur < lcm:
            results[i][0] = results[i][0] * (lcm / cur)
        arr[i] = results[i][0]

    print(arr)

# [7, 6, 8, 21] is the expected solution
solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])

# [0, 3, 2, 9, 14] is the expected solution
solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])


# END
