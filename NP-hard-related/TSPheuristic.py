# =============================================================================
# Traveling Salesman Problem
# Given a complete undirected graph G=(V,E) and the edge distance for all e in E,
# this script gives an *heuristic* algorithm that searches for the tour with the minimum 
# path distance in polynomial time and with no approximate correctness guarantees.
# =============================================================================
#%%
from math import sqrt   #for computing Euclidean distance

#Input: array G being list of the (x,y)-coordinates of nodes
#Output: the minimum tour distance. If path, return also the corresponding tour as list.
#Time complexity: O(n^2), n=|V|
#Correctness: no approximate correctness guarantees
def TSPheuristic(G, path=False):
    n = len(G)
    current = 0   #current node (starts arbitrarily from node 0)
    visited = set([0])   #nodes visited
    total = 0   #total distance travelled
    if path:
        p=[0]
    while len(visited)<n:
        dist = 99999999
        #pick the closest unvisited node as next node to visit 
        #(break tie by picking the one with lower index)
        for j in range(n):
            if j not in visited:
                #compute (Euclidean) distance squared between i and j
                k = (G[current][0]-G[j][0])**2+(G[current][1]-G[j][1])**2
                if k < dist:
                    nxt = j   #record the closest unvisited node from current node
                    dist = k   #and the corresponding distance (squared)
        total += sqrt(dist)
        if path:
            p.append(nxt)
        current = nxt
        visited.add(nxt)
    #add distance to node 0 to complete the tour
    total += sqrt((G[current][0]-G[0][0])**2+(G[current][1]-G[0][1])**2)
    if path:
        return total, p
    return total



# =============================================================================
#%% functions to read example graph data (in examples/)

#load data from txt file, each line is the (x,y)-coordinates of a node on the Cartesian plane 
def loadGraph(path): 
    with open(path) as file:
        next(file)
        E = file.readlines()
        E = [[float(n) for n in E[i].split()] for i in range(len(E))]
    return E


#%% example

G = loadGraph('examples/TSPheuristic.txt')   #file comtains coordinates of 1000 nodes
shortestDist, path = TSPheuristic(G,True)
