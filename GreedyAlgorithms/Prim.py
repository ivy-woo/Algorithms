# =============================================================================
# Prim's minimum spanning tree 
# Problem: given a connected undirected graph G=(V,E) and some real-valued cost C_e for each 
# edge e in E, compute the spanning tree T with the minimum total cost = sum_{e in T}C_e.
# =============================================================================

import heapdict   #use library heap

#Prim's algorithm implemented with heap
#Input: array G being a graph in adjacency list representation
#Output: minimum spanning tree T and the corresponding total edge cost
#Time complexity: O(mnlogn) where m=|E| and n=|V| 
def Prim(G):
    n = len(G)   #number of nodes
    T = []
    costSum=0
    H = heapdict.heapdict()   #intialize heap
    visited = [True]+[False]*(n-1)   #arbitrarily pick the first node as starting point (marked True)
    minEdge = [None]*n   #to record the edge with lowest cost for each node
    for i in range(2,n+1):
        try:
            idx = G[0]['head'].index(i)   #if there is edge between node 0 and i
            H[i] = G[0]['cost'][idx]   #insert i into heap with key=cost of edge (0,i)
            minEdge[i-1] = (G[0]['node'],i)   #edge from 0 has lowest cost.  #-1 for indexing from 0
        except ValueError:
            H[i] = 999999   #else insert i with key representing infinite cost
    while H.__len__()>0:
        v, cost = H.popitem()  #pop node v which has lowest cost from heap
        visited[v-1] = True   #mark v as visited
        T.append(minEdge[v-1])  #add v to T
        costSum += cost   #add cost of v to total cost
        nhead = len(G[v-1]['head'])
        for i in range(nhead):   #for each head i connected to v
            head = G[v-1]['head'][i]
            #if i is not yet visited and its cost from v is lower than its existing key
            if not visited[head-1] and G[v-1]['cost'][i]<H.get(head):
                H[head] = G[v-1]['cost'][i]   #update key with cost from v
                minEdge[head-1] = (v,head)  #edge from v now has lowest cost
    return T, costSum



# =============================================================================
#%% function to read example graph data (in examples/) 

#file contains edges of an undirected graph and their costs (sorted by index of the edge's tail)
#i.e. a line 'i j k' means node i is connected to node j with edge cost=k
def loadGraph(path):
    G = []
    with open(path) as file:
        for line in file:
            values = [int(n) for n in line.split()]  #split string
            try:
                idx = [i['node'] for i in G].index(values[0])   #if node already in G
                if values[1] not in G[idx]['head']:
                    G[idx]['head'].append(values[1])  #append new head and cost
                    G[idx]['cost'].append(values[2])
            except ValueError:
                G.append({'node':values[0], 'head':[values[1]], 'cost':[values[2]]})  #else append new dict 
            #undirected graph, so do the same for reverse direction
            try:
                idx = [i['node'] for i in G].index(values[1])   
                if values[0] not in G[idx]['head']:
                    G[idx]['head'].append(values[0])  #append new head and cost
                    G[idx]['cost'].append(values[2])
            except ValueError:
                G.append({'node':values[1], 'head':[values[0]], 'cost':[values[2]]})
    G = sorted(G, key=lambda x:x['node'])     #sort according to node indices
    return G  #return graph in adjacency list representation, a list of dictionaries


#%% example

#see plot in examples/ for visualization of the graph and the computed spanning tree
G = loadGraph('examples/Prim.txt')   #file contains graph with 40 nodes and 55 edges
T, totalCost = Prim(G)   #spanning tree T with 39 edges and min total edge cost -41633

