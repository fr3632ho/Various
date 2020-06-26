#### Information
|  Nr | Problem / File  | Description & Links  |
|---|---|---|
|  1 | [Union Find](https://github.com/fr3632ho/various/blob/master/src/medium/unionfind.py)  |link to problem [statement](https://open.kattis.com/problems/unionfind). Implementation of a data structure which tracks a set of elements partitioned into a number of disjoint subsets, also called Union Find. The *union* method is implemented using **union by size** which compares the size of the disjoints sets when union is performed. The *find* part of the data structure uses **path compression** to limit the height of the trees, created by union between elements, to speed up the process of determining wether two elements belong to the same set or not. By the use of path compression we speed up the find part of the algorithm significantly, from O(n) to constant time.   |
|  2 |   |   |
|  3 |   |   |
|  4 |   |   |
|  5 |   |   |
|  6 |   |   |
|  7 |   |   |


1. [Union Find](https://github.com/fr3632ho/various/blob/master/src/medium/unionfind.py) (*unionfind.py*), link to problem [statement](https://open.kattis.com/problems/unionfind)

Implementation of a data structure which tracks a set of elements partitioned into a number of disjoint subsets, also called Union Find. The *union* method is implemented using **union by size** which compares the size of the disjoints sets when union is performed. The *find* part of the data structure uses **path compression** to limit the height of the trees, created by union between elements, to speed up the process of determining wether two elements belong to the same set or not. By the use of path compression we speed up the find part of the algorithm significantly, from O(n) to constant time.

2. [Virtual Friends](https://github.com/fr3632ho/various/blob/master/src/medium/virtual_friends.py) (*virtual_friends.py*), link to problem [statement](https://open.kattis.com/problems/virtualfriends)

More use of the Union Find data structure, just a little simpler since the time constraints are not as harsh. Basically a modified version of the problem given above.

3. [Airconditioned Minions](https://github.com/fr3632ho/various/blob/master/src/medium/AC_minions.py) (*AC_minions.py*), link to problem [statement](https://open.kattis.com/problems/airconditioned)

For every range given as a preference for a minion, determine how many of these preferences you can combine into a larger preference range where the intersection of preference is not equal to the empty set. What is to be determined here is the number of larger sets one would need to cover all the preferences of the minions.

4. [Dominoes 2](https://github.com/fr3632ho/various/blob/master/src/medium/dominoes_2.py), link to problem [statement](https://open.kattis.com/problems/dominoes2)

Count the number of dominoes that would fall over if given dominoe was to be tipped. Solved using a **BFS** to count all reachable nodes.

5. [Tarjans Algorithm for strongly connected components](https://github.com/fr3632ho/various/blob/master/src/medium/tarjan_scc.py)

Done more for the sake of learning the procedure of the algorithm and not as a correct implementation. Not tested.

6. [Dijkstras shortest path algorithm](https://github.com/fr3632ho/various/blob/master/src/medium/dijkstra.py)

Implementation just for the sake of learning the algorithm. Tested in other various problems and works.

7. [Mandlebrot](https://github.com/fr3632ho/various/blob/master/src/medium/mandlebrot.py) (*mandelbrot.py*), link to problem [statement](https://open.kattis.com/problems/mandelbrot)

Determine if a number *c* is in the mandelbrot set or not. 

