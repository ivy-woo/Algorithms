# =============================================================================
# Huffman code
# Given some symbols of an alphabet sigma and their weights, compute the sigma-tree
# with minimum average leaf depth, which represents the prefix-free binary code with
# minimum average encoding length 
# =============================================================================
#%%
import heapdict   #use heap from library

#Input: array A containing weight of each symbol
#Output: a binary tree structure T with min average leaf depth
#Time complexity: O(nlogn)
def Huffman(A):
    #initialize a binary tree structure, where each symbol is a node and an individual tree
    T = binaryTrees(A)   #see script '../Others/binaryTrees.py'
    H = heapdict.heapdict()   #initialize heap
    for i in range(len(A)):
        H[i] = A[i]   #push all nodes into heap, key of node is its weight
    while T.ntree>1:
        t1,_ = H.popitem()   #pop 2 roots with least weight        
        t2,_ = H.popitem()
        T.combine(t1,t2)   #combine into one tree with new root
        H[T.nnode-1] = T.weights[T.nnode-1]   #push new root with key being its weight
    return T
    

# =============================================================================
#%% example

from random import sample
n = 20  #set number of symbols
A = sample(range(1,100),n)
T = Huffman(A)
code, length, avglength = T.traverse()
#code, length = binary code and encoding length for each symbol (in order of appearance in A), 
#avglength = the (minimum) weighted average encoding length
