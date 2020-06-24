#### Information
1. [Union Find](https://github.com/fr3632ho/various/blob/master/src/medium/unionfind.py), link to problem statement on [kattis](https://open.kattis.com/problems/unionfind)

Implementation of a data structure which tracks a set of elements partitioned into a number of disjoint subsets, also called Union Find. The *union* method is implemented using **union by size** which compares the size of the disjoints sets when union is performed. The *find* part of the data structure uses **path compression** to limit the height of the trees, created by union between elements, to speed up the process of determining wether two elements belong to the same set or not. By the use of path compression we speed up the find part of the algorithm significantly, from O(n) to constant time.

