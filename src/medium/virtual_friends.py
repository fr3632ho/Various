# Union Find problem
import sys

class Sets:

    def __init__(self, n):
        self.sizes  = [1]*n
        self.parents = [i for i in range(n)]

    '''
    Check if u, v are connected in the same tree
    '''
    def is_connected(self, u, v):
        if u == v:
            return True
        return self.parents[u] == self.parents[v]

    '''
    Union between u,v
    Compare on number of children
    '''
    def union(self, u, v):
        x_parent, y_parent = self.find_parent(u), self.find_parent(v)

        if x_parent == y_parent:
            return

        if self.sizes[x_parent] > self.sizes[y_parent]:
            self.sizes[x_parent] += self.sizes[y_parent]
            self.parents[y_parent] = x_parent
        else:
            self.sizes[y_parent] += self.sizes[x_parent]
            self.parents[x_parent] = y_parent

    '''
    Find parent of u and parent of v and move them up the tree structure
    '''
    def find_parent(self, v):
        root = v
        # First find the root
        while root != self.parents[root]:
            root = self.parents[root]

        # Path compression
        p_prime = v
        while p_prime != root:
            _p = self.parents[p_prime]
            self.parents[p_prime] = root
            p_prime = _p

        return root

def main():
    # Query handling
    data = []
    T = int(sys.stdin.readline().strip())
    F = int(sys.stdin.readline().strip())
    for i in sys.stdin:
        data.append(i.split())
    



if __name__ == '__main__':
    main()


# END
