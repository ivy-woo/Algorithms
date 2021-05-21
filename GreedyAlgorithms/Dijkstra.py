# =============================================================================
# Dijkstra's shortest distance algorithm
# Given a directed graph G=(V,E) and non-negative edge distance for all e in E, compute the 
# shortest distance from one given node to all nodes in G in quasi-linear time. 
# =============================================================================
#%%
import heapdict  #use library heap

#Input: adjacency list of graph G and some node k
#Output: shortest distance from node k to all other nodes (distance=999999 if not accessible)
#Time complexity: O((m+n)logn), m=|E|, n=|V|
def Dijkstra(G,k):
    n = len(G)
    path = [0 for i in range(n)]
    scanned = [False for i in range(n)]   #recording nodes scanned
    H = heapdict.heapdict()   #initialize heap
    for i in range(n):   #set key for each node
        if i==k:
            H[i] = 0   #starting node k has distance 0
        else:
            H[i] = 999999   #set key for other nodes temporarily as inaccessible
    while H.__len__()>0:
        node, path[node-1] = H.popitem()   #get node with smallest key
        scanned[node-1] = True   #set node as scanned
        nhead = len(G[node-1]['head'])
        for i in range(nhead):   #update keys for all head i from node
            oldkey = H.get(G[node-1]['head'][i],'none')
            if oldkey!='none':   #if head i in H, update key
                H[G[node-1]['head'][i]] = min(oldkey, path[node-1] + G[node-1]['dist'][i])
    return path



# =============================================================================
#%% function to read example graph data (in examples/)

#file contains a directed graph in adjacency list representation, sorted by node index
#e.g. a line '1 45,493 62,98' means node 1 is connected to node 45 with distance=493 inbetween 
#and to node 62 with distance=98 
import re
def loadGraph(path):
    G = []
    idx = 0
    with open(path) as file:
        for line in file:
            values = [int(n) for n in re.split('\t|,|\n',line) if n]   #split string
            G.append({'node':values[0], 'head':[], 'dist':[]})   #append dict for each node
            if len(values)>1:   #if pointing to other nodes
                G[idx]['head'] = values[1::2]   #heads that node is pointing to
                G[idx]['dist'] = values[2::2]   #distance from node to heads
            idx+=1
    return G   #return list of dictionaries, one for each node


#%% example

G = loadGraph('examples/Dijkstra8.txt')   #file contains graph with 200 nodes + 1200 edges
d = Dijkstra(G,1)   #list of distance from node 1 to node v for all v in V

