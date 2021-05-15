# =============================================================================
# Traveling Salesman Problem
# Given a complete undirected graph G=(V,E) and the edge distance for all e in E,
# this script gives an *heuristic* algorithm that searches for the tour with the minimum 
# path distance in polynomial time and with no approximate correctness guarantees.
# =============================================================================
#%%

#Input: array G being adjacency list representation of a graph
#Output: the minimum tour distance. If path, return also the corresponding tour as list.
#Time complexity: O(n^2), n=|V|
#Correctness: no approximate correctness guarantees
def TSPheuristic(G, path=False):
    n = len(G)
    current = 0   #current node (starts arbitrarily from node 0)
    visited = [0]   #nodes visited
    total = 0   #total distance travelled
    if path:
        p=[0]
    while len(visited)<n:
        #pick the closest node not yet visited as next node to visit 
        #(break tie by visiting the one with lower index)
        nxt, dist = min([(h,d) for h,d in G[current] if h not in visited], key = lambda x:x[1])
        total += dist
        if path:
            p.append(nxt)
        current = nxt
        visited.append(nxt)
    #add distance to node 0 to complete the tour
    total += G[current][0][1]
    if path:
        return total, p
    return total



# =============================================================================
#%% functions to read example graph data (in examples/)

#load data from txt file, each line is the (x,y)-coordinates of a node on the Cartesian plane 
def loadGraph(path): 
    with open(path) as file:
        coord = file.readlines()
        coord = [[float(n) for n in coord[i].split()[1:]] for i in range(len(coord))]
    return coord


from math import sqrt
#make adjacency list representation from the coordinates.
#return a list of n lists, each list i=1,2,...,n contains n-1 2-element tuples (h,d),
#where h is a node that i point to, and d is distance between i and h.
def makeList(coord):
    n=len(coord)
    adjlist=[[] for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            #compute (Euclidean) distance between i and j
            dist = sqrt((coord[i][0]-coord[j][0])**2+(coord[i][1]-coord[j][1])**2)
            #append to lists of i and j
            adjlist[i].append((j,dist))
            adjlist[j].append((i,dist))
    return adjlist   #list of lists of n-1 2-element tuples


#%% example

G = makeList(loadGraph('examples/TSPheuristic.txt'))   #file comtains coordinates of 1000 nodes
shortestDist, path = TSPheuristic(G,True)
