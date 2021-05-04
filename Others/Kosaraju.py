# =============================================================================
# Kosaraju's algorithm
# Compute the strongly connected components (SCC) in a directed graph in linear time
# =============================================================================

#read in data in txt file. #file contains directed edges of a graph
def loadGraph(path): 
    with open(path) as file:
        G = file.readlines()
#        G = [[int(n) for n in re.split('\t|,\d*|\n',G[i]) if n] for i in range(len(G))]
        G = [[int(n) for n in G[i].split()] for i in range(len(G))]
    return G

#from itertools import chain
#node = set(chain(*G))
#n = len(node)


#preprocessing functions

#make adjacency list from input G being edges
def makeList(G):
    adjlist = []
    idx=1
    i=0
    for idx in range(1,G[-1][0]+1):
        adjlist.append([idx])
        while G[i][0]==idx:
            adjlist[idx-1].append(G[i][1])
            i+=1
            if i==len(G):
                break
    return adjlist


#reverse the edges
def revEdges(G):
    rev = [G[i][::-1] for i in range(len(G))]  #reverse edges
    rev.sort(key=lambda x: x[0])
    return rev


#make adjacency list for graph with reversed edges
def revList(G):
    rev = revEdges(G)
    return makeList(rev)


#compute SCC

#Kosaraju algorithm using 2 DFS to compute SCC in a graph
#Input: array G containing edges of an undirected graph
#Output: list representing the repective SCC each node belongs to
#e.g. for G with 4 nodes, scc=[1,2,2,2] means node 1 in SCC1 and node 2,3,4 in SCC2
def Kosaraju(G):
    Glist = makeList(G)  #make adjacency list for G
    Grev = revList(G)  #make adjacency list for G with reversed edges
    n = Glist[-1][0]  #number of nodes
    order = TopoSort(Grev,n)  #topological sort for Grev
    unexplored = [True for i in range(n)]
    scc = [0]*n
    count = 0
    for i in order:
        if unexplored[i]:
            count+=1
            DFSscc(Glist,scc,unexplored,count,i)
    return scc


#input adjacency list and node i, search for and mark all nodes in the same SCC as i by DFS
def DFSscc(G,scc,unexplored,count,i):
    unexplored[i] = False
    scc[i] = count
    for j in G[i][1:]:
        if unexplored[j-1]:
            DFSscc(G,scc,unexplored,count,j-1)
    return


#input adjacency list, return topological ordering for all nodes with values 0:n-1 by DFS
def TopoSort(G,n):
    order = [0]*n
    unexplored = [True for i in range(n)]
    label = [n-1]  #as list for convenience of passing with ref
    for i in range(n):
        if unexplored[i]:
            DFStopo(G,order,unexplored,label,i)
    return order
    

def DFStopo(G,order,unexplored,label,i):
    unexplored[i] = False
    for j in G[i][1:]:
        if unexplored[j-1]:
            DFStopo(G,order,unexplored,label,j-1)
    order[i] = label[0]
    label[0] -= 1
    return 


from collections import Counter
#return sizes of the biggest 5 SCC, append 0 if there exist <5 SCC
def topsize(scc):
    size = [0]*5
    cnt = Counter(scc)
    n = min(5,max(cnt))
    size[:n] = [i for _,i in cnt.most_common()[:n]]
    return size


#example
G = loadGraph('examples\SCC3.txt')
scc = Kosaraju(G)
topsize(scc)

