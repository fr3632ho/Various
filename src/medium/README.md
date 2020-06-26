#### Information
1. [Union Find](https://github.com/fr3632ho/various/blob/master/src/medium/unionfind.py) (*unionfind.py*), link to problem [statement](https://open.kattis.com/problems/unionfind)

Implementation of a data structure which tracks a set of elements partitioned into a number of disjoint subsets, also called Union Find. The *union* method is implemented using **union by size** which compares the size of the disjoints sets when union is performed. The *find* part of the data structure uses **path compression** to limit the height of the trees, created by union between elements, to speed up the process of determining wether two elements belong to the same set or not. By the use of path compression we speed up the find part of the algorithm significantly, from O(n) to constant time.

2. [Virtual Friends](https://github.com/fr3632ho/various/blob/master/src/medium/virtual_friends.py) (*virtual_friends.py*), link to problem [statement](https://open.kattis.com/problems/virtualfriends)

More use of the Union Find data structure, just a little simpler since the time constraints are not as harsh. Basically a modified version of the problem given above.

3. [Tarjans Algorithm for strongly connected components](https://github.com/fr3632ho/various/blob/master/src/medium/tarjanSCC.py) [link](https://github.com/fr3632ho/various/blob/master/src/medium/tarjanSCC.py)

Done more for the sake of learning the procedure of the algorithm and not as a correct implementation. Not tested.

