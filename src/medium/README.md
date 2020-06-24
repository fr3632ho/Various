#### Information

1. unionfind.py &rarr Implementation of a data structure which tracks a set of elements partitioned into a number of disjoint subsets, also called Union Find. Solution is implemented using **union by size** which compares the size of the disjoints sets when union is performed. The *find* part of the data structure uses **path compression** to limit the height of the trees, created by union between elements, to speed up the process of determining wether two elements belong to the same set or not.
