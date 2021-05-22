This repo contains the Python code for some algorithms courses.

Each script includes an example cell at the bottom.
Examples' related files are located in the examples/ folder. For some, a plot is included for better visualization of the example data. Most plots are generated in Gephi.

----------------------------------------------------------------------------------------------------------------------------------

The folders and files are listed below with brief descriptions:

#### Divide-and-Conquer

- `countInv`: counting the number of inversions in an array of $n$ elements in $O(n\log n)$-time.
- `Karatsuba`: Karatsuba's algorithm, multiplication of two positive integers with $n$ digits in $O(n\log n)$-time.
- `MergeSort`: sorting in $O(n\log n)$-time, where $n$ is number of elements.
- `QuickSort`: randomized quick sort in $O(n\log n)$-time, where $n$ is number of elements.
- `RSelect`: randomized selection, given an array of $n$ elements and some $k\in [1,2,\ldots,n]$, return the $k$-th smallest element in the array in $O(n)$-time.

#### DynamicProgramming

- `FloydWarshall`: the Folyd-Warshall algorithm. Given a directed graph $G=(V,E)$ with some real-valued edge length $l_e$ for all edge $e\in E$,  compute the all-pairs shortest distance in $G$ in $O(n^3)$-time where $n=|V|$.
- `Knapsack`: algorithm on the 0-1 Knapsack problem. Given a set of $n$ items, each with some value $v_i \in \mathbb{R}^+$ and some size $s_i \in \mathbb{N}$ for all $i\in [1,2,\ldots,n]$, and a Knapsack capacity $C \in \mathbb{N}$, compute the maximum total value attainable by some subset of the items, where each item can appear either 0 or 1 time, and with which the total size does not exceed $C$. Two approaches are implemented, both running in pseudo-polynomial $O(nC)$-time, depending on parameters either can run faster in practice.
- `WIS`: algorithm on the Weighted Independent Set (WIS) problem for *path graphs*. Given a path graph $G=(V,E)$ and some non-negative weight for all $v \in V$, compute the maximum-weight independent set of $G$ and its total weight in $O(n)$-time where $n=|V|$.

#### GreedyAlgorithms

- `clustering`: given $n$ nodes and the all-pairs distance, use Kruskal's minimum spanning tree algorithm (terminating early) to construct a minimum-spacing $k$-clustering. Implemented with disjoint set (defined in script `Others/disjointSet`) and running in $O(n\log n)$-time.
- `Dijkstra`: Dijkstra's shortest distance algorithm. Given a directed graph $G=(V,E)$ with some non-negative edge length $l_e$ for all $e\in E$ and a starting vertex $v\in V$, compute the shortest distance from $v$ to all vertices in $G$. Implementation with heap, complexity being $O((m+n)\log n)$-time, where $m=|E|$ and $n=|V|$. 
- `Huffman`: Huffman's algorithm for shortest encoding length. Given $n$ symbols of an alphabet $\Sigma$ and their real-valued weights, compute the $\Sigma$-tree with minimum average leaf depth, which represents the prefix-free binary code with minimum average encoding length. Implemented with tailor-made binary-trees structure (defined in script `Others/binaryTrees.py`) and heap, complexity being $O(n\log n)$-time. 
- `Prim`: Prim's  minimum spanning tree algorithm. Given a connected undirected graph $G=(V,E)$ and some real-valued cost $C_e$ for each edge $e \in E$, compute the spanning tree $T$ with the minimum total cost $\sum_{e\in T} C_e$ in $O(mn\log n)$-time, where  $m=|E|$ and $n=|V|$. 
- `scheduling`: given a set of n jobs with weights $w_i$ and lengths $l_i$ for $i\in [1,2,\ldots,n]$,  schedule the sequence of completing the jobs s.t. the weighted sum of completion time is minimized. Two greedy algorithms are implemented, both computing in $O(n\log n)$-time, with one being optimal and one not. 

#### NP-hard-related

- `TSPexhaust`: solve the Traveling Salesman Problem (TSP) by *exhaustive search* - given a completed directed graph $G=(V,E)$ with some real-valued edge length $l_e$ for all edges $e\in E$, compute the shortest possible distance of a tour $T\subseteq E$  and its path in $O(n!)$-time by exhaustively searching all permutations of nodes.
- `TSPheuristic`: solve the TSP (see above) by the nearest neighbour *heuristic algorithm* - a greedy algorithm which starts at an arbitrary node, moves iteratively to the nearest neighbouring node, and returns to the starting node after all nodes are visited. Time complexity being  $O(n^2)$-time, no approximate correctness guarantees.
- `twoSAT`: algorithm on the 2-SAT problem. Given a set of $n$ boolean variables and $m$ constraints which are disjunctions of 2 literals (i.e. 'A or B'), the algorithm determines whether there exists solution to the variables with which all constraints are satisfied in $O(m+n)$-time*. Kosaraju's algorithm (from script `Others/Kosaraju.py`) is borrowed.

#### Others

- `binaryTrees`: self-defined binary-trees structure, tailor-made for Huffman code.
- `disjointSet`: self-defined disjoint set.
- `Kosaraju`: Kosaraju's algorithm. Given a directed graph $G=(V,E)$, compute the strongly connected components in the graph in $O(m+n)$-time*, where $m=|E|$ and $n=|V|$. 
- `MaxMinHeap`: self-defined max heap and min heap.
- `medianMaintenance`: suppose $n$ data arrives consecutively, use two heaps (defined in script `Others/MaxMinHeap.py`) to update the median of the $i$ arrived data in $O(\log i)$-time in each round $i\in[1,2,\ldots,n]$.

-------------------------------------------------------------------------------

*For average cases, assuming healthy data and hash functions for the dictionaries employed.