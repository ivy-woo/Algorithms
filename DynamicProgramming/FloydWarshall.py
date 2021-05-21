# =============================================================================
# Floyd-Warshall's all-pairs shortest path algorithm
# Given a directed graph G=(V,E) and some real-valued edge length for all edges, compute the shortest 
# distance from v to w for all v,w in V, or return that there exists negative cycle in the graph.
# =============================================================================

#%%

#Input: array G being the adjacency list representation of a graph
#Output: a 2D array A containing all-pairs shortest distance (999999 represents inaccessible), 
        #or the string signaling that a negative cycle exists in the graph.
        #if fullArray, return full array with solutions to subproblems.
#Time complexity: O(n^3), n=|V|
def FloydWarshall(G, fullArray=False):
    n = len(G)
    A = [[[None for i in range(n)] for i in range(n)] for i in range(n+1)]   #(n+1)*n*n empty array
    #base cases
    for v in range(n):
        for w in range(n):
            if v==w:
                A[0][v][w] = 0   
            else:
                try:
                    idx = G[v]['head'].index(w)   #if edge (v,w) in E
                    A[0][v][w] = G[v]['dist'][idx]   #assign length of (v,w)
                except ValueError:
                    A[0][v][w] = 999999   #else assign infinite distance
    #solve subproblems recursively
    for k in range(1,n+1):
        for v in range(n):
            for w in range(n):
                #case1: k not in shortest v-w path. case2: otherwise.
                A[k][v][w] = min(A[k-1][v][w], A[k-1][v][k-1]+A[k-1][k-1][w])   #assign min of 2 cases
    for v in range(n):
        if A[n][v][v] < 0:
            return "Negative cycle in graph."
    if fullArray:
        return A
    return A[n]   #A[n] = solution to original problem with n nodes



# =============================================================================
#%% functions to read example graph data (in examples/)

#txt file contains list of edges of a directed graph (sorted by index of the edge's tail) 
#e.g. a line "i j k" represents edge (i,j) with distance k.
#nodes indexed from 0.
def loadGraph(path):
    edges = []
    with open(path) as file:
        for line in file:
            values = [int(n) for n in line.split()]
            edges.append(values)
        nnode = max([max(i,j) for i,j,_ in edges]) +1
    return edges, nnode

#make adjacency list representation from list of edges.
#return list of dictionaries, one for each node i, with three keys 'node', 'head' and 'dist',
#corresponding to node index i, list of nodes j that i points to, and list of distance from i to each j
#Note: parellel edges are eliminated by picking only the shortest one.
def makeList(edges,nnode):
    adjlist = []
    i=0
    for idx in range(nnode):
        adjlist.append({'node':idx, 'head':[], 'dist':[]})
        if i<len(edges):   #continue if not yet finished scanning edges
            while (edges[i][0])==idx:
                try:   #check if there is parallel edge
                    parellel = adjlist[idx]['head'].index(edges[i][1])   #if yes
                    if edges[i][2] < adjlist[idx]['dist'][parellel]:   #and if new edge is shorter
                        print("Parellel edges at ({0},{1}), the one with distance {2} is removed."
                              .format(idx, edges[i][1], adjlist[idx]['dist'][parellel]))
                        adjlist[idx]['dist'][parellel] = edges[i][2]   #replace by new edge
                except ValueError:
                    adjlist[idx]['head'].append(edges[i][1])
                    adjlist[idx]['dist'].append(edges[i][2])
                i+=1
                if i==len(edges):
                    break
    return adjlist   #list of dictionaries of form {'node':i, 'head':[...], 'dist':[...]}


#%% example

#see plot in examples/ for visualization of the graph
edges, nnode = loadGraph('examples/FloydWarshall.txt')   #file comtains edges of a graph with 16 nodes
G = makeList(edges,nnode)
shortestDist = FloydWarshall(G)   #for all v,w in V, shortestDist[v][w] = shortest distance from v to w
