# =============================================================================
# the Weighted Independent Set (MWIS) problem for path graphs
# Given a path graph G=(V,E) and some non-negative weight for each v in V, compute the
# maximum-weight independent set of G and its total weight.
# =============================================================================
#%%

#Input: array G containing the weight of all node v in V
#Output: the nodes (indexing from 0) in the maximum-weight independent set and their total weight
#Time complexity: O(n), n=|V|
def WIS(G):
    n = len(G)
    A = [0] + [G[0]] + [0]*(n-1)   #base cases + cache the n-1 subproblem results
    inS = [False]*(n-1)   #cache the n-1 comparison results below, wether a node is in MWIS
    for i in range(2,n+1):
        if A[i-2]+G[i-1] > A[i-1]:
            A[i] = A[i-2]+G[i-1]   #case 1: node i in MWIS
            inS[i-2] = True
        else:
            A[i] = A[i-1]    #case 2: node i not in MWIS
    i = n-1  #-1 for indexing from 0
    S = []
    while i>=1:   #reconstruct the MWIS from inS
        if inS[i-1]:
            S.append(i)
            i -= 2
        else:
            i -= 1
    if i==0:  #base case
        S.append(0)    
    return S, A[n]



#%% example

from random import sample
G = sample(range(1,1000),50)   #50 nodes, random weight in [1,999]
mwis, weight = WIS(G)   #mwis= set of all nodes in MWIS, weight= total weight of the set
