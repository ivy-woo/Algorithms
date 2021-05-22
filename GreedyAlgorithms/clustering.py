# =============================================================================
# Kruskal's algorithm for bottom-up clustering
# Given n nodes, compute the min-spacing k-clustering of the nodes and the resulting spacing.
# Uses the Kruskal's minimum spanning tree algorithm and terminates the edge appending process early.
# Spacing defined as the minimum distance between any two nodes in different clusters.
# =============================================================================
#%%

#Input: G=list of edges (sorted by node indices) of a connected undirected graph and their length,
      # k=requied number of clusters
#Output: list T of edges with which the k-clustering is formed, the spacing of the resulting cluster
#Time complexity: O(nlogn), n=|V|
def cluster(E,k):
    n = E[-1][1]   #number of nodes
    if k>n:
        print("Error. Number of clusters greater than number of nodes in graph.")
        return
    T = []   #to hold edges which form the clustering
    DS = disjointSet([i for i in range(1,n+1)])   #see `../Others/disjointSet.py`
    E = sorted(E, key=lambda x:x[2])   #sort edges by length in non-decreasing order
    for e in E:
        if DS.find(e[0])!=DS.find(e[1]):   #if the two endpoints of the edge are in different groups
            if len(T)==n-k:   #if there are already k clusters
                spacing = e[2]   #mark spacing as the current edge length
                break   #and terminate loop
            T.append((e[0],e[1]))   #add edge to T
            DS.union(e[0],e[1])   #and group the two groups into one
    return T, spacing



# =============================================================================
#%% function to read example graph data (in examples/) 

#file contains distance between all nodes of an undirected graph (sorted by node indices)
#e.g. a line 'i j k' means distance between nodes i and j is k. nodes indexed from 1.
def loadGraph(path):
    with open(path) as file:
        G = file.readlines()
        G = [[int(n) for n in G[i].split()] for i in range(len(G))]
    return G


#%% example

E = loadGraph('examples/clustering.txt')   #file contains all-pairs distance between 256 nodes
clusterEdges, spacing = cluster(E,4)   #append 252 edges to construct a 4-clustering, spacing=1199

