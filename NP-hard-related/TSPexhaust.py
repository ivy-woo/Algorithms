# =============================================================================
# Traveling Salesman Problem
# Given a complete undirected graph G=(V,E) and the edge distance for all e in E,
# the function in this script *exhaustively* searches for the tour with the minimum path distance.
# =============================================================================
#%%
import itertools   #use library function to get all permutations

#Input: array G being adjacency list representation of a graph
#Output: the minimum tour distance. If path, return also the corresponding tour as tuple.
#Time complexity: O(n!), n=|V|
def TSPexhaust(G, path=False):
    n = len(G)
    perm = list(itertools.permutations([i for i in range(n)]))
    A = []
    for temp in perm:
        dist = 0
        for i in range(n):
            current = temp[i]
            if i!=(n-1):
                nxt = temp[i+1]
            else:
                nxt = temp[0]
            dist += G[current]['dist'][G[current]['head'].index(nxt)]
        A.append(dist)
    if path:
        return min(A), perm[A.index(min(A))]
    return min(A)



# =============================================================================
#%% functions to read example graph data (in examples/)

#load data from txt file, each line is the (x,y)-coordinates of a node on the Cartesian plane 
def loadGraph(path): 
    with open(path) as file:
        coord = file.readlines()
        coord = [[float(n) for n in coord[i].split()] for i in range(len(coord))]
    return coord


from math import sqrt
#make adjacency list representation from the coordinates.
#return list of dictionaries, one for each node i, with three keys 'node', 'head' and 'dist',
#corresponding to node index i, list of nodes j that i point to, and list of distance from i to each j.
def makeList(coord):
    n=len(coord)
    adjlist = []
    for i in range(n):
        adjlist.append({'node':i, 'head':[], 'dist':[]})
    for i in range(n):
        for j in range(i+1,n):
            #compute (Euclidean) distance between i and j
            dist = sqrt((coord[i][0]-coord[j][0])**2+(coord[i][1]-coord[j][1])**2)
            #append j and distance to dict of i
            adjlist[i]['head'].append(j)
            adjlist[i]['dist'].append(dist)
            #repeat for dict of j
            adjlist[j]['head'].append(i)
            adjlist[j]['dist'].append(dist)
    return adjlist   #list of dictionaries of form {'node':i, 'head':[...], 'dist':[...]}


#%% example

G = makeList(loadGraph('examples/TSPexhaust.txt'))   #file comtains coordinates of 8 nodes
shortestDist, path = TSPexhaust(G,True)   #path is (0,1,2,5,7,6,4,3)
#see plot in examples/ for visualization of the coordinates and shortest tour