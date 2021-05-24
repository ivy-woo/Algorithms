# =============================================================================
# Kosaraju's algorithm
# Given a directed graph G=(V,E), compute the strongly connected components (SCC) in linear time.
# DFS implemented by recursion.
# =============================================================================
#%%

#Input: array E containing edges of a directed graph
#Output: dictionary where key=nodes' indices, value=SCC group of the node
#e.g. for |V|=4, {1:1,2:2,3:2,4:2} means node 1 in SCC1 and node 2,3,4 in SCC2
#Time complexity: O(m+n) (assume healthy data and hash functions for dictionaries), m=|E|, n=|V|
def Kosaraju(E):
    G = makeList(E)  #make adjacency list from edges
    seq = topoSort(G)  #topological sort for the reverse graph of G
    count = 0
    for i in reversed(seq):   #loop in order of topological order, from smallest to largest
        if G[i]['flag2']:
            count += 1
            DFSscc(G,count,i)
    output = {}
    for i in list(G.keys()):
        output[i] = G[i]['scc']
    return output


#convert list of edges to adjacency list representation
#return a dictionary of dictionaries, one for each node, with global key being some node i,
#secondary keys 'in' for tails of i's incoming edges, 'out' for heads of i's outgoing edges,
#'flag1' and 'flag2' for signaling whether i is not yet visited in the upcoming 1st and 2nd DFS
def makeList(E):
    adjlist = {}
    for edge in E:
        #for tail i of the edge
        try:   #if dict for i already exists, append to list 'out'
            adjlist[edge[0]]['out'].append(edge[1])
        except KeyError:   #else instantiate dict for i
            adjlist[edge[0]] = {}
            adjlist[edge[0]]['out'] = [edge[1]]   #heads of i's outgoing edges
            adjlist[edge[0]]['in'] = []   #tails of i's incoming edges
            adjlist[edge[0]]['flag1'] = True   #to mark i is not yet visited in 1st DFS
            adjlist[edge[0]]['flag2'] = True   #to mark i is not yet visited in 2nd DFS
        #do the same for head of the edge
        try:
            adjlist[edge[1]]['in'].append(edge[0])
        except KeyError:
            adjlist[edge[1]] = {}
            adjlist[edge[1]]['out'] = []
            adjlist[edge[1]]['in'] = [edge[0]]
            adjlist[edge[1]]['flag1'] = True
            adjlist[edge[1]]['flag2'] = True
    return adjlist   #dictionary of dictionaries, one for each node


#variant of the topological ordering algorithm
#input adjacency list, return a list 'seq' of the sequence of nodes when sorting by their 
#topological order from largest to smallest. 
def topoSort(G):
    seq = []
    for i in list(G.keys()):
        if G[i]['flag1']:
            DFStopo(G,seq,i)
    return seq


#DFS recursion, to append nodes to 'seq' in decreasing order of nodes' topological order
def DFStopo(G,seq,i):
    G[i]['flag1'] = False   #mark i as visited in 1st round
    #loop list of *incoming* edges since considering the reversed graph
    for j in G[i]['in']:
        if G[j]['flag1']:
            DFStopo(G,seq,j)
    seq.append(i)   #append i to 'seq'
    return 


#recursive DFS to search and mark the scc group for all nodes in node i's group
def DFSscc(G,count,i):
    G[i]['flag2'] = False   #mark i as visited in 2nd round
    G[i]['scc'] = count   #new key for i recording its scc group
    for j in G[i]['out']:
        if G[j]['flag2']:
            DFSscc(G,count,j)
    return



#%% additional function

from collections import Counter
#return the sizes of the biggest 5 SCC, append 0 if there exist <5 SCC
def topSize(scc):
    size = [0]*5
    cnt = Counter(scc.values())
    n = min(5,max(cnt))
    size[:n] = [i for _,i in cnt.most_common()[:n]]
    return size


# =============================================================================
#%% function to read example data (in examples/)

#each line "i j" in txt file is an edge from node i to j, edges sorted by the tail i's index
#nodes' indices can be anything hashable
def loadGraph(path): 
    with open(path) as file:
        E = file.readlines()
        E = [[int(n) for n in E[i].split()] for i in range(len(E))]
    return E


#%% example

#see plot in examples/ for visualization of the graph
G = loadGraph('examples/Kosaraju.txt')   #file contains edges of a graph with 200 nodes
scc = Kosaraju(G)   #dictionary, key=node, value=SCC group
topSize(scc)   #sizes of the 4 SCC in the graph
