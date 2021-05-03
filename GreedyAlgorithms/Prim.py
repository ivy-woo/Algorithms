# =============================================================================
# Prim's minimum spanning tree 
# Problem: given a connected undirected graph G=(V,E) and some real-valued cost C_e for each 
# edge e in E, compute the spanning tree T with the minimum total cost = sum_{e in T}C_e.
# =============================================================================

import heapdict   #use heap in library

#Prim's algorithm implemented with heap
#Input: graph G in adjacency list representation
#Output: minimum spanning tree T and corresponding total edge cost
#Time complexity: O(mnlogn) where m=|E| and n=|V| 
def Prim(G):
    n = len(G)
    T = []
    costsum=0
    H = heapdict.heapdict()   #intialize heap
    scanned = [True]+[False]*(n-1)   #arbitrarily pick the first node as starting point (marked T)
    minedge = [None]*n   #to record the other endpoint of the edge with lowest cost for each node
    for i in range(2,n+1):
        try:
            idx = G[0]['head'].index(i)   #if there is edge between node 0 and i
            H[i] = G[0]['cost'][idx]   #insert i into heap with key=cost
            minedge[i-1] = (G[0]['node'],i)   #edge from 0 has lowest cost.  #-1 for indexing from 0
        except ValueError:
            H[i] = 999999   #else insert i with key representing infinite cost
    while H.__len__()>0:
        v, cost = H.popitem()  #pop node v with lowest cost from heap
        scanned[v-1] = True   #mark v as scanned
        T.append(minedge[v-1])  #add v to T
        costsum += cost   #add cost of v to total cost
        nhead = len(G[v-1]['head'])
        for i in range(nhead):   #for each head i connected to v
            head = G[v-1]['head'][i]
            #if i is not yet scanned and its cost from v is lower than its existing key
            if not scanned[head-1] and G[v-1]['cost'][i]<H.get(head):
                H[head] = G[v-1]['cost'][i]   #update key with cost from v
                minedge[head-1] = (v,head)  #edge from v now has lowest cost
    return T, costsum



# =============================================================================
# example

#see plot in the example folder for visualization
G = loadGraph('example/Prim.txt')   #example data contains graph with 40 nodes and 55 edges
T, totalCost = Prim(G)   #spanning tree T with 39 edges and min total edge cost -41633


#function to read in data in txt file. #file contains edges of an undirected graph with their costs.
#e.g. a line '1 2 438' means node 1 is connected to node 2 with edge cost=438 
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
    return G  #return graph in adjacenc list representation, in form of list of dictionaries

